from django.urls import path

from store import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
router=DefaultRouter()
router.register("products",views.ProductsView,basename="products")
router.register("baskets",views.BasketView,basename="baskets")

urlpatterns=[

        path("signup/",views.SignUpView.as_view()),
        path("token/",obtain_auth_token)

]+router.urls
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)