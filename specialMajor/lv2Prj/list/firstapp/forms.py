from django import forms
from django.core.exceptions import ValidationError

class UserinfoForm(forms.Form):
    realname=forms.CharField(max_length=50,required=False)
    # username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50,required=False)
    profile_image=forms.FileField(required=False)
    GENDER_CHOICES=(
        ('male','男'),
        ('female','女'),
    )
    gender_choice=forms.ChoiceField(choices=GENDER_CHOICES,required=False)

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

def words_validation(content):
    if len(content)<4:
        raise ValidationError('not enough words')

def nosuchwords_validation(content):
    nowords=['发票','钱']
    for words in nowords:
        if words  in content:
            raise ValidationError('「Your comment contains invalid words,please check it again.」')

class CommentForm(forms.Form):
    name=forms.CharField(max_length=50)
    content=forms.CharField(
    widget=forms.Textarea(),
    error_messages={
    'required':'wow,such words'
    },
    validators=[words_validation,nosuchwords_validation]
    )
