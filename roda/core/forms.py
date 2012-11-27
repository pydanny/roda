from django import forms

from registration.forms import RegistrationFormUniqueEmail


class WtfRegistrationForm(RegistrationFormUniqueEmail):

    def __init__(self, *args, **kwargs):
        super(WtfRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].help_text = "Don't worry, we hate spam too."
        self.fields['password2'].widget = forms.HiddenInput()
        self.fields['password2'].required = False

    def clean(self):
        return self.cleaned_data
