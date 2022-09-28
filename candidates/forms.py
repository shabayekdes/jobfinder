from django import forms
from django.contrib.auth.forms import UserCreationForm

from candidates.models import Candidate


# Create your forms here.

class CandidateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Candidate
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CandidateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
