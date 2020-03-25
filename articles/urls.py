"""articles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from articles import settings
from office import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.tape, name='tape'),
    path('add_article', views.write_article, name='write_art'),
    path('article/<int:pk>', views.view_article, name='article'),
    path('delete/<int:pk>', views.del_article, name='delete'),
    path('edit/<int:pk>', views.edit_article, name='edit'),
    path('period_delete/<int:pk>', views.del_period, name='period_delete'),
    path('periods_manager', views.view_periods, name='periods_view')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
