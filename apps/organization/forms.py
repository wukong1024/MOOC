from django import forms
import re

from operation.models import UserAsk


class UserAskForm(forms.ModelForm):  # ModelForm的强大
    # name = forms.CharField(required=True, min_length=2, max_length=20)
    # phone = forms.CharField(required=True, min_length=11, max_length=11)
    # course_name = forms.CharField(required=True, min_length=5, max_length=50)

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course']

    def clean_mobile(self):  # 必须以clean开头
        """
        验证手机号码是否合法
        """
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^[1](([3][0-9])|([4][5-9])|([5][0-3,5-9])|([6][5,6])|([7][0-8])|([8][0-9])|([9][1,8,9]))[0-9]{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")
