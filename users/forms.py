from django import forms
from django.core.exceptions import ValidationError

from .models import User

def check_consecutive(value, n=3):
    # 내가 3개의 연속된 수를 검사하는것이라고 했기 때문에 원래는 1칸짜리 검사가 검사당 3칸짜리가 된다.
    # 따라서 마지막 2개까지 하게되면 2칸만큼 인덱스 오버가 되기때문에 사실상 길이에서 2를 빼주는 것이다.
    for i in range(len(value) - (n-1)):
        # 내가 지정한 알고리즘이 연속된 3개라고 했으니깐 i~i+3이면 i가 0일때 0:3임. 결국 0,1,2 3개의 인덱스가 긁히는 것이고
        # set은 중복 허용이 안되기에 길이가 1이라는말은 0,1,2내부의 값이 1개라는 소리. 즉, 3개 연속이라는 소리로써 문제값
        if len(set(value[i:i+n])) == 1:
            return True
    return False

class SignupForm(forms.Form):
    username = forms.CharField(
        label = "아이디",
        min_length=4,
        help_text="4자 이상 입력"
    )
    password1 = forms.CharField(
        label = "비밀번호1",
        min_length=8,
        widget=forms.PasswordInput,
        help_text="8자 이상 입력"
    )
    password2 = forms.CharField(
        label = "비밀번호2",
        min_length=8,
        widget=forms.PasswordInput,
        help_text="8자 이상 입력"
    )
    profile_image = forms.ImageField(label="프로필 이미지", required=False)
    short_description = forms.CharField(label = "소개글", required=False)
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        if check_consecutive(username, 3):
            raise ValidationError("아이디에 같은 입력값이 3번 이상 나왔습니다.")
        
        if not username.isalnum():
            raise ValidationError("아이디에 특수문자나 공백 사용을 피해주세요")

        if User.objects.filter(username = username).exists():
            raise ValidationError("이미 존재하는 계정입니다.")
        
        return username
        
    def clean_password1(self):
        password = self.cleaned_data["password1"]
        
        if check_consecutive(password, 3):
            raise ValidationError("같은 수 3개 이상 입력 불가")
        
        if password.isalnum():
            raise ValidationError("비밀번호는 특수문자를 1개 이상 포함 해야함")
        
        return password
    
    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2:
            if password1 != password2:
                self.add_error("password2", "일치하지 않습니다.")
        
        return self.cleaned_data
    
    def save(self):
        username = self.cleaned_data["username"]
        password1 = self.cleaned_data["password1"]
        profile_image = self.cleaned_data.get("profile_image")
        short_description = self.cleaned_data.get("short_description")
        
        user = User.objects.create_user(
            username = username,
            password = password1,
            profile_image = profile_image,
            short_description = short_description
        )
        return user
    
class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=4,
        widget=forms.TextInput(
            attrs={"placeholder": "사용자명 (4자리 이상)"},
        ),
        )
    password = forms.CharField(
        min_length=4,
        widget = forms.PasswordInput(
            attrs = {"placeholder": "비밀번호 (4자리 이상)"},
        ),
        )