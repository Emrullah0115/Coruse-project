from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm
from django.forms import widgets
from django.contrib import messages
from django.contrib.auth.models import User

class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class": "form-control"})
        self.fields["password"].widget = widgets.PasswordInput(attrs={"class": "form-control"})

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if username == "admin":
            messages.success(self.request, "Hoşgeldin Admin")

        return username
    
    def confirm_login_allowed(self, user):
        if user.username.startswith("s"):
            raise forms.ValidationError("Bu kullanıcı adı ile giriş yapamazsınız")

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email","first_name","last_name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["password2"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["username"].widget = forms.TextInput(attrs={"class": "form-control"})
        self.fields["email"].widget = forms.EmailInput(attrs={"class": "form-control"})
        self.fields["email"].required = True
        self.fields["first_name"].widget = forms.TextInput(attrs={"class": "form-control"})
        self.fields["last_name"].widget = forms.TextInput(attrs={"class": "form-control"})


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            self.add_error("email","email daha önce kullanılmış")   
        return email     
    

class UserPasswordChangeForm(PasswordChangeForm):
   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password2"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["old_password"].widget = forms.PasswordInput(attrs={"class": "form-control"})
       

