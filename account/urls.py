from django.urls import path
from .views import *


urlpatterns = [
path('signup/', SignUpView.as_view(), name='signup'),
path('edit_profile/', edit_profileView.as_view(), name='edit_profile'),
path('user/', USER.as_view(), name='user_profile')
]