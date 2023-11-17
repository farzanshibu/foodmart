from django.shortcuts import render


# Create your views here.
def HomeView(request):
    return render(request, "home/home.html")


def AboutView(request):
    return render(request, "home/about.html")


def CartView(request):
    return render(request, "home/cart.html")


def CheckOutView(request):
    return render(request, "home/checkout.html")


def CompareView(request):
    return render(request, "home/compare.html")


def ContactView(request):
    return render(request, "home/contact.html")


def FAQView(request):
    return render(request, "home/faq.html")


def WishlistView(request):
    return render(request, "home/wishlist.html")


def TagsView(request):
    return render(request, "others/tags.html")


def SingleShopView(request):
    return render(request, "shop/single-shop.html")


def SingleProductView(request):
    return render(request, "product/single-product.html")


def BlogDetailsView(request):
    return render(request, "blog/blog-detail.html")


def BlogListView(request):
    return render(request, "blog/blog-list.html")
