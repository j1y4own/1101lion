from django import forms
from .models import Cashbook, Comment, Hashtag

class CashbookForm(forms.ModelForm):
    class Meta:
        model = Cashbook
        fields = ['title', 'content', 'image','hashtags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class HashtagForm(forms.ModelForm):
    class Meta :
        model = Hashtag
        fields = ['name']