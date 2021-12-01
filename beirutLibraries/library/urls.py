#to give us the ability to reroute urls
from django.urls import path
from django.views.generic.base import TemplateView 
from . import views 
from django.conf import settings
# from django.conf.urls.static import static

app_name = 'library'

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'home_page.html'), name = 'home'),
    path('login-user/', views.login_user_view, name = "login-user"),
    path('logout-user/', views.logout_user_view, name = "logout-user"),
    path('register-user/', views.register_user_view, name = "register-user"),
    path('login-admin/', views.login_librarian_view, name = "login-librarian"),
    path('logout-admin/', views.logout_librarian_view, name = "logout-librarian"),
    path('register-admin/', views.register_librarian_view, name = "register-librarian"),
    path('list/', views.book_list_view, name = 'book-list'),
    path('create/', views.book_create_view, name='create-book'),
    path('<int:book_id>/', views.book_detail_view, name="book-detail"),
    path('<int:book_id>/delete/', views.book_delete_view, name='book-delete'),
    path('<int:book_id>/update/', views.book_update_view, name='book-update'),
    path('user-page/', views.user_page_view, name = 'user-page'),
    path('view/<int:book_id>/', views.user_book_view, name = 'user-book-detail'),
    path('view/<int:book_id>/borrow/', views.user_borrow_view, name = 'borrow-book'),
    path('view/<int:book_id>/return/', views.user_return_view, name = 'return-book'),

] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)