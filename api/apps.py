from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class MyAPIAdminSiteConfig(AdminConfig):
    default_site = 'website.admin.MyAPIAdminSiteConfig'

class ApiConfig(AppConfig):
    name = 'api'
