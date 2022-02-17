from xml.parsers.expat import model
from django import forms
from app.psf_app.models import Author

class AuthorCreationModelForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['name', 'email', 'mobile', 'salary']
    
    def __init__(self, *args, **kwargs):
        super(AuthorCreationModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control', 'placeholder': 'Author Name'})
        self.fields['name'].required = False
        self.fields['email'].widget.attrs.update({'class' : 'form-control', 'placeholder': 'Email', 'autocomplete':'off'})
        self.fields['mobile'].widget.attrs.update({'class' : 'form-control', 'placeholder': 'mobile', 'autocomplete':'off'})
        self.fields['mobile'].help_text = 'Valid only BD number'
        self.fields['salary'].widget.attrs.update({'class' : 'form-control', 'placeholder': '0.0'})
    
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 4:
            raise forms.ValidationError("Minimum 4 characters")
        return name
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if len(email) < 4:
            raise forms.ValidationError("Minimum 4 characters")
        return email