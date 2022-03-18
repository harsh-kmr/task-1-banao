from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'profile_pic','first_name', 'last_name','line_1', 'city', 'state', 'pincode' )



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'profile_pic','first_name', 'last_name','line_1', 'city', 'state', 'pincode', 'is_patient', 'is_doctor' )