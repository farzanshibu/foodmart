from django.urls import path

from .views import (
    AboutView,
    BlogDetailsView,
    BlogListView,
    CartView,
    CheckOutView,
    CompareView,
    ContactView,
    FAQView,
    HomeView,
    SingleProductView,
    SingleShopView,
    TagsView,
    WishlistView,
)

app_name = "core"

urlpatterns = [
    path("about/", AboutView, name="about"),
    path("blog-details/", BlogDetailsView, name="blog-details"),
    path("blog-list/", BlogListView, name="blog-list"),
    path("cart/", CartView, name="cart"),
    path("checkout/", CheckOutView, name="checkout"),
    path("compare/", CompareView, name="compare"),
    path("contact/", ContactView, name="contact"),
    path("faq/", FAQView, name="faq"),
    path("", HomeView, name="home"),
    path("single-product/", SingleProductView, name="single-product"),
    path("single-shop/", SingleShopView, name="single-shop"),
    path("tags/", TagsView, name="tags"),
    path("wishlist/", WishlistView, name="wishlist"),
]
