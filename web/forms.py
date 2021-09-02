from django import forms

class resume_create_form(forms.Form):

    first_name = forms.CharField(max_length=255, required=True, label="نام:",
    widget=(forms.TextInput(attrs={'class':'form-control m-2', 'autocomplete':'off'})))


    last_name = forms.CharField(max_length=255, required=True, label="نام خانوادگی:",
    widget=(forms.TextInput(attrs={'class':'form-control m-2', 'autocomplete':'off'})))


    description = forms.CharField(required=True, label="درباره شما:",
    widget=(forms.Textarea(attrs={'class':'form-control m-2', 'autocomplete':'off'})))

