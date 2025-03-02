
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ImageUploadView, AllImagesView, UserImagesView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('upload/', ImageUploadView.as_view(), name='image_upload'),
    path("all-images/", AllImagesView.as_view(), name="all_images"), 
    path("user-images/<str:username>/", UserImagesView.as_view(), name="user_images"),
] 

