from xml.parsers.expat import model
from django import forms
from app.psf_app.models import Author

class AuthorCreationModelForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['name', 'email', 'mobile', 'salary']