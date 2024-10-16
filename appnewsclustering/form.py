from django import forms
from .models import Company  # Company 모델 임포트

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company  # Company 모델 기반
        fields = ['name', 'description1', 'description2', 'founded_date', 'headquarters']  # 필요한 필드 추가
