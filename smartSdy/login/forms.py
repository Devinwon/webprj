from django import forms

class Regfm(forms.Form):
    username = forms.CharField(
      widget=forms.TextInput(attrs={"placeholder": "用户名", "required": "required",}),
      max_length=10,
      min_length=5,
      error_messages={"required": "用户名不能为空",},
      label="注册用户"
      )
    email = forms.EmailField(
      widget=forms.TextInput(attrs={"placeholder": "邮箱",}),
      max_length=50,
      min_length=7,
      error_messages={"required": "邮箱不能为空",},
      label="输入邮箱",
      required=True,
      )
    password_set = forms.CharField(
      widget=forms.PasswordInput(attrs={"placeholder": "设置密码", "required": "required",}),
      max_length=20,
      min_length=6,
      error_messages={"required": "密码不能为空",},
      label="输入密码")
    password_confirm = forms.CharField(
      widget=forms.PasswordInput(attrs={"placeholder": "确认密码", "required": "required",}),
      max_length=20,
      min_length=6,
      error_messages={"required": "密码不能为空",},
      label="确认密码")



'''
class Regfm(forms.ModelForm):
	class Meta():
		model=User
		fields=('username','password','email')
		# exclude=('id',)
		无法取出中文字段在模板中显示
'''
'''
    url = forms.URLField(widget=forms.TextInput(attrs={"placeholder": "Url", }),
                              max_length=100, required=False)
'''