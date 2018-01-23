from django import forms

class Regfm(forms.Form):
    username = forms.CharField(
      widget=forms.TextInput(attrs={"placeholder": "用户名5-20位", }),
      max_length=20,
      min_length=5,
      error_messages={"required": "用户名不能为空",},
      label="注册用户"
      )
    password_set = forms.CharField(
      widget=forms.PasswordInput(attrs={"placeholder": "设置密码6-20位",}),
      max_length=20,
      min_length=6,
      error_messages={"required": "密码不能为空",},
      label="输入密码")
    password_confirm = forms.CharField(
      widget=forms.PasswordInput(attrs={"placeholder": "确认密码6-20位", "required": "required",}),
      max_length=20,
      min_length=6,
      error_messages={"required": "密码不能为空",},
      label="确认密码")
    email = forms.EmailField(
      widget=forms.EmailInput(attrs={"placeholder": "邮箱(选填)",}),
      max_length=20,
      min_length=7,
      error_messages={"required": "邮箱不能为空",},
      label="输入邮箱",
      required=False,
      )
