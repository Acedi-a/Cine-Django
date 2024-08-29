from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User


class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirmar_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'confirmar_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmar_password = cleaned_data.get("confirmar_password")

        if password != confirmar_password:
            raise ValidationError("Las contraseñas no coinciden")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo electrónico ya está registrado.")
        return email

    def clean_username(self):
        user = self.cleaned_data.get('username')
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError("El nombre de usuario ya existe.")
        if user.isnumeric():
            raise forms.ValidationError("El nombre de usuario no puede ser solo numerico")
        if len(user) < 4 or len(user) > 20:
            raise forms.ValidationError("El nombre de usuario debe tener entre 4 y 20 caracteres")
        return user

    def clean_first_name(self):
        nombre = self.cleaned_data.get('first_name')
        if not self.verificar_caracteres(nombre):
            raise forms.ValidationError("El nombre no puede contener caracteres numericos o especiales")
        return nombre

    def clean_last_name(self):
        apellido = self.cleaned_data.get('last_name')
        if not self.verificar_caracteres(apellido):
            raise forms.ValidationError("El apellido no puede tener caracteres numericos o especiales")
        return apellido

    def save(self, commit=True):
        user = super().save(commit=False)
        user.FechaRegistro = timezone.now()
        if commit:
            user.save()
        return user


    def verificar_caracteres(self, campo):
        special_chars = set('!@#$%^&*()-_=+[]{}|;:\",.<>?/`~1234567890')
        print(campo)
        for char in campo:
            if char in special_chars:
                return False
        return True



class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    confirmar_password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmar_password = cleaned_data.get("confirmar_password")

        if password and password != confirmar_password:
            raise ValidationError("Las contraseñas no coinciden")

        return cleaned_data