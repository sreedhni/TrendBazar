from django.urls import path

from store import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[

        path("signup/",views.SignUpView.as_view()),
        path("token/",obtain_auth_token)

]