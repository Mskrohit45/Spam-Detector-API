from django.urls import path
from .views import RegisterUserView, MarkSpamView, SearchView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('mark-spam/', MarkSpamView.as_view(), name='mark_spam'),
    path('search/', SearchView.as_view(), name='search'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
