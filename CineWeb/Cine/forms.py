from django import forms
from .models import Usuario
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User


class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirmar_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password', 'confirmar_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmar_password = cleaned_data.get("confirmar_password")

        if password != confirmar_password:
            raise ValidationError("Las contraseñas no coinciden")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.FechaRegistro = timezone.now()
        if commit:
            user.save()
        return user