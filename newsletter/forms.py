from django import forms

from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required= False)
    email = forms.EmailField()
    message = forms.CharField()

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        #what fields are going to be included in this form
        fields = ['full_name', 'email']
        #exclude = ['full_name'] use sparingly

    #clean_fieldname
    def clean_email(self):
        email = self.cleaned_data.get('email')
        #email_base, provider = email.split("@")
        #domain, extension = provider.split(',')
        # if not domain == "syr":
        #     raise forms.ValidationError("Please use your syrcuse email")
        # if not extension == "edu":
        # #if not "edu" in email:
        #     raise forms.ValidationError("Please use a valid .edu email address")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name
