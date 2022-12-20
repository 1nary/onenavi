from django import forms
from allauth.account.forms import SignupForm

class SignupUserForm(SignupForm):
  nickname = forms.CharField(max_length=30)

  def save(self, request):
    user = super(SignupUserForm, self).save(request)
    user.nickname = self.cleaned_data['nickname']
    user.save()
    return user