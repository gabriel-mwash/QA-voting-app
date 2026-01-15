from django import forms
from .models import user_data


class userForm(forms.ModelForm):
    class Meta:
        model = user_data
        fields = ["first_name", "second_name", "age", "nationality"]
