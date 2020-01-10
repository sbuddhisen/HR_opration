from django import forms

class ApplicantResume(forms.Form):
    file = forms.FileField()