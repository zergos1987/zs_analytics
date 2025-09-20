from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views import View
import logging
import requests

logger = logging.getLogger(__name__)


# SPA dynamic url pages view

#@login_required
#@permission_required('app_zs_admin.view_app')
def index(request):
	context = {
		'page_settings': 0,
	}

	template = 'app_pages/index.html' 

	return render(request, template, context)


# Streamlit views
@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(require_http_methods(["GET", "POST"]), name='dispatch')
class StreamlitProxyView(View):
    """Proxy-view for Streamlit application"""
    
    def dispatch(self, request, *args, **kwargs):
        # Base access check (additionaly to middleware)
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Доступ запрещен")
        
        return super().dispatch(request, *args, **kwargs)
    
    def handle_request(self, request, path=''):
        """Processing proxy-request"""
        try:
            # Forming URL for Streamlit
            streamlit_url = f"{settings.STREAMLIT_INTERNAL_URL}{path}"
            
            # Preparing headers
            headers = self.prepare_headers(request)
            
            # Sending request to Streamlit
            response = self.send_to_streamlit(request, streamlit_url, headers)
            
            # Processing request
            return self.process_response(response)
            
        except requests.RequestException as e:
            logger.error(f"Streamlit proxy error: {str(e)}")
            return HttpResponse(
                f"Ошибка соединения с Streamlit приложением: {str(e)}",
                status=502,
                content_type='text/plain'
            )
        except Exception as e:
            logger.exception("Unexpected error in Streamlit proxy")
            return HttpResponse(
                "Внутренняя ошибка сервера",
                status=500,
                content_type='text/plain'
            )
    
    def prepare_headers(self, request):
        """Preparing headers for proxing"""
        headers = {}
        
        # Copying required headers
        for key, value in request.headers.items():
            key_lower = key.lower()
            if key_lower in ['accept', 'accept-language', 'content-type', 'user-agent']:
                headers[key] = value
        
        # Removing problem headers
        headers.pop('Host', None)
        headers.pop('Connection', None)
        
        return headers
    
    def send_to_streamlit(self, request, url, headers):
        """Sending request to Streamlit"""
        if request.method == 'GET':
            return requests.get(
                url, 
                headers=headers, 
                params=request.GET,
                timeout=30
            )
        elif request.method == 'POST':
            return requests.post(
                url,
                headers=headers,
                data=request.body,
                params=request.GET,
                timeout=30
            )
    
    def process_response(self, response):
        """Processing answer from Streamlit"""
        # Creating Django response
        django_response = HttpResponse(
            response.content,
            status=response.status_code,
            content_type=response.headers.get('content-type', 'text/html')
        )
        
        # Copying required headers
        for key, value in response.headers.items():
            key_lower = key.lower()
            if key_lower in ['content-type', 'cache-control', 'etag']:
                django_response[key] = value
        
        # Adding security headers
        django_response['X-Frame-Options'] = 'SAMEORIGIN'
        django_response['X-Content-Type-Options'] = 'nosniff'
        
        return django_response
    
    def get(self, request, path=''):
        return self.handle_request(request, path)
    
    def post(self, request, path=''):
        return self.handle_request(request, path)

# Функция-обертка для использования в urls.py
@csrf_exempt
@require_http_methods(["GET", "POST"])
def streamlit_proxy(request, path=''):
    view = StreamlitProxyView()
    view.request = request
    return view.handle_request(request, path)

# Errors handler views
def custom_permission_denied(request, exception=None):
    return HttpResponseForbidden("Доступ запрещен")

def custom_page_not_found(request, exception=None):
    return HttpResponse("Страница не найдена", status=404)

def custom_server_error(request):
    return HttpResponse("Внутренняя ошибка сервера", status=500)