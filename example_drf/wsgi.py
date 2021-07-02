import os  # Не уверен что папке example_drf тут место

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example_drf.settings')

application = get_wsgi_application()
