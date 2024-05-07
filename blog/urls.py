from django.urls import path
from . import views
from django.contrib import messages
from .views import *
from django.contrib.auth import views as auth
# from .views import SignUpView
from django.views.static import serve
from django.conf import settings
from django.contrib.auth import views as authViews
urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('register_done', views.register, name='register_done'),
    # dddddddddddd
    path('', views.users_login, name="login_sn"),
	# path('logout', views.signout, name="signout"),
	path('forgot-password', views.forgot_password, name="forgot-password"),

    path('home', views.home, name='home'),
    path('product', views.product, name='product'),
    path('product_detail/<int:id>', views.product_detail, name='product_detail'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('login_sn/', views.login_sg, name="login_sn"),
    path('login_admins', views.admin_login, name="login_admin"),
    
    path('logout', views.signout, name="signout"),
    path('add_book', views.add_book, name='add_book'),
    path('change_password', views.PasswordChange, name='change_password'),
    path('changepassword/done', PasswordChangeDone, name='change-password-done'),

    path('passwordreset/', authViews.PasswordResetView.as_view(), name='password_reset'),
	path('passwordreset/done', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('passwordreset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('passwordreset/complete', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('password-change/done/', auth_views)
    # path('forgot-password', views.forgot_password, name='forgot-password'),
    # path('', views.index_users, name='index_user'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('chat', views.chat_user, name='chat'),

    # path('reset-password', views.PasswordResetView, name='reset-password'),
    # path('forgot-password/', views.forgot_password, name='forgot_password'),
   
    path('homes', views.your_view, name='homes'),
    # path('download', views.download, name='download'),
    # path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),


    
    
]