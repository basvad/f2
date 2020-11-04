from django import forms    
from django.contrib.auth.forms import AuthenticationForm, UsernameField

#настледуемся от стандартной формы
class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Логин',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label= 'Пароль',
        strip=False,
        widget=forms.PasswordInput,
    )
