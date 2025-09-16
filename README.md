<h1 align="center">
  <br>
  <a href=""><img src="https://github.com/zergos1987/zs_analytics/blob/zs_analytics/backend/app/media/screenshots/logo.png" alt="zs_analytics" width="200"></a>
  <br>
  zs_analytics
  <br>
</h1>

<h4 align="center">it's a set of integrated tools for data analysis or low-code site development</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#screenshots">Screenshots</a> •
  <a href="#installation">Installation</a> •
  <a href="#license">License</a> •
  <a href="#links">Links</a>
</p>

![screenshot](https://github.com/zergos1987/zs_analytics/blob/zs_analytics/backend/app/media/screenshots/01.png)


## Key Features


<details><summary>Tool #1. Backend on Django</summary> 

    - Backend includes API endpoints
    - Backend have Custom-User-Model extend base model
    - Backend have dynamic urls (CRUD) with no-code
    - Backend have Authentication with JWT Tokens

</details>

<details><summary>Tool #2. Frontend on iframed Streamlit</summary>

    - Frontend have custom UI components

</details>

<details><summary>Tool #3. Database on PostgreSQL/SQLite</summary>

    - ...

</details>

<details><summary>Tool #4. Iframed dashboards on DataLens</summary>

    - ...

</details>

<details><summary>Tool #5. Iframed dashboards on Apache Superset</summary>

    - ...

</details>

<details><summary>Tool #6. ETL on Apache Airflow</summary>

    - ...

</details>

<details><summary>Tool #7. Caching on Redis</summary>

    - ...

</details>

<details><summary>Tool #8. Deployment on Docker and Nginx</summary>

    - Docker containers for every tools in zs_analytics
    - Nginx as webserver

</details>


## Screenshots

### [Click to see more](https://github.com/zergos1987/zs_analytics/tree/zs_analytics/backend/app/media/screenshots)
![image](https://github.com/zergos1987/zs_analytics/blob/zs_analytics/backend/app/media/screenshots/01.png)


## Installation

1. Clone the repository to use it localy:

        git clone https://github.com/zergos1987/zs_analytics.git
        
2. In project folder write command:

  For `Mac Users`

        ([ -d venv  ] && echo venv_activated || (python3 -m pip install virtualenv && python3 -m virtualenv venv && echo venv_created)) && source venv/bin/activate && pip install -r backend/requirements.txt && echo venv_activated && ([ -d app  ] && echo project dir exists || (source venv/bin/activate && django-admin startproject app && cd app && python3 manage.py startapp app_api && python3 manage.py startapp app_spa && django-admin startapp app_accounts && cd .. && cp -R backend/app . && cp -R frontend/app . && ([ -f .env  ] && echo 1 || cp -R .env.example .env) && python3 app/manage.py makemigrations && python3 app/manage.py migrate && python3 app/manage.py collectstatic --no-input && (echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(username='admin', email='admin@dj_zs.com', password='dj_zs12345')" | python3 app/manage.py shell) && echo init project dir done))

  For `Win Users`

        python -m venv venv && venv\Scripts\Activate && pip install -r backend/requirements.txt --no-cache-dir --no-deps && django-admin startproject app && cd app && django-admin startapp app_spa && django-admin startapp app_api && django-admin startapp app_accounts && cd .. && xcopy "backend/app" "app" /c /i /e /h /y && xcopy "frontend/app" "app" /c /i /e /h /y && (if not exist .env copy .env.example .env) && python app/manage.py makemigrations && python app/manage.py migrate && python app/manage.py collectstatic --no-input && python app/manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser((username='admin', email='admin@dj_zs.com', password='dj_zs12345')"
        
3. Run backend command (User: admin, password: dj_zs12345):

        python app/manage.py runserver

## License

The zs_analytics is licensed under the terms of the MIT License and is available for free.

## Links

* [Web site](https://zs-analytics.com/)
* [Documentation](https://zs-analytics.com//docs/)
* [Issue tracker](https://github.com/zergos1987/zs_analytics/issues)
* [Source code](https://github.com/zergos1987/zs_analytics)