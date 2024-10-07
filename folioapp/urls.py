from django.urls import path
from folioapp.views import HomeView, MyProfileView, MyProfileUpdateView, ContactView


app_name = 'folioapp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', MyProfileView.as_view(), name='profile'),
    path('profile/update/<int:pk>/', MyProfileUpdateView.as_view(), name='profile_update'),
    path('profile/contact/', ContactView.as_view(), name='contact')
]
