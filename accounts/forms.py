from django.contrib.auth import get_user_model # returns user model currently active in this project
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields # built in creation form

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2') # confirmation of pw
        model = get_user_model()

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = "Email Address"