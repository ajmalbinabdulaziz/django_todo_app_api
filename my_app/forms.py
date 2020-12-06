from django import forms
from my_app.models import ToDo


class ToDO_Form(forms.ModelForm):
    class Meta():
        model = ToDo
        fields = ('title', 'memo','important')
