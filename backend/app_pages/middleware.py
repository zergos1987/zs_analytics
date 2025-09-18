from django.http import HttpResponseForbidden
from django.conf import settings
from django.urls import resolve

class StreamlitAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Checking if we call to Streamlit
        if request.path.startswith(settings.STREAMLIT_PUBLIC_URL):
            # Check auth user 
            if not request.user.is_authenticated:
                return HttpResponseForbidden(
                    "Доступ к Streamlit приложению запрещен. Требуется авторизация."
                )
                
            # Additional access checking
            if not self.has_streamlit_access(request.user):
                return HttpResponseForbidden(
                    "Недостаточно прав для доступа к Streamlit приложению."
                )
                
            # loggin acces for audit
            self.log_streamlit_access(request.user, request.path)
                
        return self.get_response(request)
    
    def has_streamlit_access(self, user):
        """Checking user access rights to Streamlit"""
        # Example: access only for staff or some groups
        if hasattr(user, 'profile') and user.profile.has_streamlit_access:
            return True
            
        # Checking access by groups
        if user.groups.filter(name='Streamlit Users').exists():
            return True
            
        return user.is_staff or user.is_superuser
    
    def log_streamlit_access(self, user, path):
        """Logging access to Streamlit"""
        # Here can make add logging to database or monitoring system
        print(f"User {user.username} accessed Streamlit: {path}")