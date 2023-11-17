from django.shortcuts import render


# Create your views here.


def BadRequest_400_View(request, exception):
    return render(request, "error/400.html", status=400)


def PermissionDenied_403_View(request, exception):
    return render(request, "error/403.html", status=403)


def Error_404_View(request, exception):
    return render(request, "error/404.html", status=404)


def Error_500_View(request):
    return render(request, "error/500.html", status=500)
