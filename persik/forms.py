from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()


class CityForm(forms.Form):
    city = forms.CharField(label='City', max_length=50)


class IPForm(forms.Form):
    ip = forms.CharField(label='IP', max_length=20)