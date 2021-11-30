#to give us the ability to reroute urls
from django.urls import path
from django.views.generic.base import TemplateView 
from . import views 
from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'home_page')),
    path('login/', views.login_view, name = "user-login")
] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)