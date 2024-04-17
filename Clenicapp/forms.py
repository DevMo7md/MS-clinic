from django import forms
from .models import Add_user

class AddUsers(forms.ModelForm):
    class Meta:
        model = Add_user
        fields = "__all__" 