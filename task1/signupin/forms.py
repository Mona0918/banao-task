from django import forms
from .models import SignUpModel,UTModel
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

class UserTypeForm(forms.ModelForm):
    class Meta:
        model=UTModel
        fields='__all__'
        labels={'usertype':'What Type of User You Are?'}
        user_types=[('Patient','Patient'),('Doctor','Doctor')]
        widget={'usertype':forms.RadioSelect(choices=user_types)}

class RegisterForm(forms.ModelForm):
    class Meta:
        model=SignUpModel
        fields=['first_name','last_name','ProfilePic','username','email','password','ConfirmPassword','Address']
    
    def clean(self):
        cleaned_data = super(RegisterForm,self).clean()
        password1=cleaned_data.get('password')
        password2=cleaned_data.get('ConfirmPassword')
        if password1 != password2:
            self.add_error('ConfirmPassword', "Password Mismatch")
        return cleaned_data
        

