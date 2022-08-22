from django.urls import path
from authentication.views import SignupUserViewset
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('signup/', SignupUserViewset.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
