from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_1.models import Comic, Horror, History, Adventure
from django.core.files.storage import FileSystemStorage

class NewUser(UserCreationForm):
    email = forms.EmailField()
    phone = forms.IntegerField(widget=forms.TextInput)
    class Meta:
        model = User
        fields = {"username","email","phone","password1","password2"} 

    def save(self,commit=True):
        user = super(NewUser,self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        return user


class Horrorform(forms.ModelForm):
    class Meta:
        model=Horror
        fields='__all__'

class Comicform(forms.ModelForm):
    class Meta:
        model=Comic
        fields='__all__'

class Historyform(forms.ModelForm):
    class Meta:
        model=History
        fields='__all__'

class Adventureform(forms.ModelForm):
    class Meta:
        model=Adventure
        fields='__all__'