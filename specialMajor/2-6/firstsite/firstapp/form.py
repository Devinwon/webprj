# 从views.py中分离出来，然后再views.py中引入即可
from django import forms
from django.core.exceptions import ValidationError

def words_validator(comment):
    if len(comment)<4:
        raise ValidationError('words not enought')

def nosuchwords_validator(comment):
    if 'A' in comment:
        raise ValidationError('Do not use that words')
# Create your views here.
class CommentForm(forms.Form):
    name=forms.CharField(max_length=50)
    comment=forms.CharField(
        widget=forms.Textarea(),
        error_messages={
        'required':'wow,such words'},
        validators=[words_validator,nosuchwords_validator]#验证器，列表构造
    )#改变窄条
