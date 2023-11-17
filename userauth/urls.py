from django.urls import path
from .views import (
    LoginView,
    RegisterView,
    ProfileView,
    LogoutView,
    ChangePasswordView,
    ForgotPasswordView,
    ResetPasswordView,
    VerifyEmailView,
    ResendVerifyEmailView,
    TwoFAView,
)

app_name = "userauth"

urlpatterns = [
    path("login/", LoginView, name="login"),
    path("register/", RegisterView, name="register"),
    path("profile/", ProfileView, name="profile"),
    path("logout/", LogoutView, name="logout"),
    path("change-password/", ChangePasswordView, name="change-password"),
    path("forgot-password/", ForgotPasswordView, name="forgot-password"),
    path("reset-password/", ResetPasswordView, name="reset-password"),
    path("resend-verify-email/", ResendVerifyEmailView, name="resend-verify-email"),
    path("verify-email/<str:key>/", VerifyEmailView, name="verify-email"),
    path("2fa/", TwoFAView, name="2fa"),
]
