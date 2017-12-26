from django import forms
from .models import Post

class NameForm(forms.Form):
    city = forms.CharField(label='city', max_length=100)
    school = forms.CharField(label = 'school', max_length = 100)
    school_year = forms.CharField(label = 'school_year', max_length = 100)
    groups = forms.CharField(label='groups', max_length=10000,widget=forms.Textarea)
    help_text =  {
            'groups': 'Group to which this message belongs to',
        }

class Login(forms.Form):
    at = forms.CharField(label = 'at', max_length=1000)

class Info(forms.Form):
    user_id = forms.CharField(label='user_id', max_length=1000)
    about = forms.CharField(label='about', max_length=1000)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
