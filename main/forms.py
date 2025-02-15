from django import forms

class JobApplicationForm(forms.Form):
    full_name = forms.CharField(
        max_length=100, 
        label='Full Name', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email', 
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        max_length=15, 
        label='Phone Number', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    resume = forms.FileField(
        label='Upload Resume', 
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    cover_letter = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        label='Cover Letter'
    )
