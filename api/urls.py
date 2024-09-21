from django.urls import path
from . import views
urlpatterns = [
    path('xyz.xyz.in/service-api/api/v1/service/aeps/kyc/Twofactorkyc/registration', views.registration),
    path('xyz.xyz.in/service-api/api/v1/service/aeps/kyc/Twofactorkyc/authentication', views.authentication),
    path('xyz.xyz.in/service-api/api/v1/service/aeps/v3/authcashwithdraw/index', views.authcashwithdraw),
]