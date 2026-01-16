from django import forms
from .models import user_data, Question


class userForm(forms.ModelForm):
    class Meta:
        model = user_data
        fields = ["first_name", "second_name", "age", "nationality"]


class anotherForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()


class QnAForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question", "name", "institute"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].initial = ""
        self.fields["institute"].initial = ""

    def clean_name(self):
        name = self.cleaned_data.get("name")
        return name or "Anonymous"

    def clean_institute(self):
        institute = self.cleaned_data.get("institute")
        return institute or "Anonymous"
