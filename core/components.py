from django_web_components import component


@component.register("slider")
class Slider(component.Component):
    template_name = "components/slider.html"


@component.register("superdeal")
class SuperDeal(component.Component):
    template_name = "components/superdeal.html"


@component.register("categorycard")
class CategoryCard(component.Component):
    template_name = "components/categorycard.html"


@component.register("shopcard")
class ShopCard(component.Component):
    template_name = "components/shopcard.html"


@component.register("clientcard")
class ClientCard(component.Component):
    template_name = "components/clientcard.html"


@component.register("featurecard")
class FeatureCard(component.Component):
    template_name = "components/featurecard.html"


@component.register("shopcardsmall")
class ShopCardSmall(component.Component):
    template_name = "components/shopcard_small.html"


@component.register("brandcard")
class BrandCard(component.Component):
    template_name = "components/brandcard.html"


@component.register("blogcard")
class BlogCard(component.Component):
    template_name = "components/blogcard.html"


@component.register("ourofferings")
class OurOfferings(component.Component):
    template_name = "components/our_offerings.html"


@component.register("introcard")
class IntroCard(component.Component):
    template_name = "components/introcard_about.html"


@component.register("teamcard")
class TeamCard(component.Component):
    template_name = "components/teamcard.html"


@component.register("card1")
class Card1(component.Component):
    template_name = "components/shop/card1.html"


@component.register("card2")
class Card2(component.Component):
    template_name = "components/shop/card2.html"


@component.register("card3")
class Card1(component.Component):
    template_name = "components/shop/card3.html"


@component.register("reviewcard")
class ReviewCard(component.Component):
    template_name = "components/shop/reviewcard.html"


@component.register("faqcard")
class FaqCard(component.Component):
    template_name = "components/faqcard.html"


@component.register("bloglistcard")
class BlogListCard(component.Component):
    template_name = "components/blog/bloglistcard.html"


@component.register("bloglistcard2")
class BlogListCard2(component.Component):
    template_name = "components/blog/bloglistcard2.html"


@component.register("commentcard")
class CommentCard(component.Component):
    template_name = "components/blog/commentcard.html"
