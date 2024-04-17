from django.urls import path, include
from . import views

# from django.contrib.auth import views as auth_views

urlpatterns = [
    # custom login view
    # path("login/", views.user_login, name="login")
    # django login/logout view
    # path('login/', auth_views.LoginView.as_view(), name="login"),
    # path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    # change password urls
    # path('password-change/', auth_views.PasswordChangeView.as_view(), name='password-change'),
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset password urls
    # path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
    #     name='password_reset_confirm'),
    # path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # using django contrib auth urls views
    path("", include("django.contrib.auth.urls")),
    path("", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("edit/", views.edit, name="edit"),
    path("users/", views.user_list, name="user_list"),
    path("users/<username>/", views.user_detail, name="user_detail"),
]
