"""
URL configuration for instagram_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return HttpResponse('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Instagram Clone</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #fafafa; }
            .container { max-width: 400px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { text-align: center; color: #333; }
            .nav { text-align: center; margin: 20px 0; }
            .nav a { margin: 0 10px; padding: 10px 20px; background: #0095f6; color: white; text-decoration: none; border-radius: 4px; }
            .nav a:hover { background: #0077cc; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📸 Instagram Clone</h1>
            <div class="nav">
                <a href="/app/">Open App</a>
            </div>
            <p style="text-align: center; color: #666;">
                API endpoints available at /api/<br>
                Frontend app available at /app/
            </p>
        </div>
    </body>
    </html>
    ''')

urlpatterns = [
    path('api/', include('instagram_app.urls')),
    path('app/', include('instagram_app.frontend_urls')),
    path('', home, name='home'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
