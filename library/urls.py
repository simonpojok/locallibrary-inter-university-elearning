
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from allauth.account import views as allauth_views

urlpatterns = [
    path("", allauth_views.signup, name="account_signup"),
    url(r"^login/$", allauth_views.login, name="account_login"),
    url(r"^logout/$", allauth_views.logout, name="account_logout"),

    url(r"^password/change/$", allauth_views.password_change,
        name="account_change_password"),
    url(r"^password/set/$", allauth_views.password_set, name="account_set_password"),

    url(r"^inactive/$", allauth_views.account_inactive, name="account_inactive"),

    # E-mail
    url(r"^email/$", allauth_views.email, name="account_email"),
    url(r"^confirm-email/$", allauth_views.email_verification_sent,
        name="account_email_verification_sent"),
    url(r"^confirm-email/(?P<key>[-:\w]+)/$", allauth_views.confirm_email,
        name="account_confirm_email"),

    # password reset
    url(r"^password/reset/$", allauth_views.password_reset,
        name="account_reset_password"),
    url(r"^password/reset/done/$", allauth_views.password_reset_done,
        name="account_reset_password_done"),
    url(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        allauth_views.password_reset_from_key,
        name="account_reset_password_from_key"),
    url(r"^password/reset/key/done/$", allauth_views.password_reset_from_key_done,
        name="account_reset_password_from_key_done"),
    
    path('student/', include("student.urls"))
]