from django import forms

from .models import Events


class AddEventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ["title", "description", "date"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class":"form-control datepicker"}),
        }
