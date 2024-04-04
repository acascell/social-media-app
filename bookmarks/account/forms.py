from django import forms


class LoginForm(forms.Form):
    """This form is used to authenticate the user against the database"""

    username = forms.CharField(password=forms.CharField(widget=forms.PasswordInput))
