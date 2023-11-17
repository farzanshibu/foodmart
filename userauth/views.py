from django.shortcuts import render


# Create your views here.
def LoginView(request):
    return render(request, "auth/login.html")


def RegisterView(request):
    return render(request, "auth/register.html")


def ProfileView(request):
    return render(request, "auth/my-account.html")


def LogoutView(request):
    pass


def ChangePasswordView(request):
    return render(request, "auth/change-password.html")


def ForgotPasswordView(request):
    return render(request, "auth/forgot-password.html")


def ResetPasswordView(request):
    return render(request, "auth/reset-password.html")


def VerifyEmailView(request):
    return render(request, "auth/verify-email.html")


def TwoFAView(request):
    return render(request, "auth/2fa.html")


def ResendVerifyEmailView(request):
    pass
