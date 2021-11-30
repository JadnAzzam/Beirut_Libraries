#to give us the ability to reroute urls
from django.urls import path
from django.views.generic.base import TemplateView 
from . import views 
from django.conf import settings
# from django.conf.urls.static import static

app_name = 'library'

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'home_page'), name = 'home'),
    path('login-user/', views.login_user_view, name = "login-user"),
    path('logout-user/', views.logout_user_views, name = "logout-user"),
    # path('register-user/', views.register_user_views, name = "register-user"),
    # path('login-admin/', views.librarian_login, name = "login-librarian"),
    # path('logout-admin/', views.logout_librarian_views, name = "logout-librarian"),
    # path('register-admin/', views.register_librarian_views, name = "register-librarian"),
    # path('list/', views.book_list_view, name = 'book_list'),
    # path('create/', views.book_create_view, name='create-book'),
    # path('<int:book_id>/', views.book_detail_view, name="book-detail"),
    # path('<int:book_id>/delete/', views.book_delete_view, name='book-delete'),
    # path('<int:book_id>/update/', views.book_update_view, name='book-update'),
] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)