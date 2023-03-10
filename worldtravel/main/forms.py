from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import EmailSubscription, Help


class SignUpForm(UserCreationForm):
    """
    Form for singn up page, where user can sign up
    It contains fields such as username, first name, last name,
    Email, password, password confirmation
    """

    class Meta:
        """
        We are declaring the fields and defining with which
        model we are going to work
        """
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'email',
                  'password1',
                  'password2')

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ваше Имя'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ваше Фамилия'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))

    confirming_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтвердите пароль'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ваш Email'
    }))


class LoginForm(AuthenticationForm):
    """
    Form for login page, where user can log in.
    it contains fields such as username and password.
    """

    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))


class EmailSubscriptionForm(forms.Form):
    """
    Form for email subscription page, where user can type his email
    """

    class Meta:
        """
        This class works with EmailSubscription model
        and has only one field to fill email
        """
        model = EmailSubscription
        fields = ('email',)

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите свой email'
    }))


class HelpForm(forms.Form):
    """
    Form that users fill in page Help in order to get help from administrators,
    all his information will be registered in database
    """

    class Meta:
        """
        Class works with Help model
        fields are name, email, phone_number, problem
        """
        model = Help
        fields = ('name',
                  'email',
                  'phone_number',
                  'problem')

    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Как к вам обращаться'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ваш email'
    }))

    phone_number = forms.CharField(max_length=17, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholeder': 'Номер телефона'
    }))

    problem = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'place-holder': 'Опишите свою проблему'
    }))


