from django.shortcuts import render, get_object_or_404
from .models import Company


# Create your views here.

def home(request):
    context = {
        'app_name': 'appnewsclustering'  # 'appnewsclustering'을 적절한 키로 변환
    }
    return render(request, 'appnewsclustering/home.html', context)
    
def home(request):
    companies = Company.objects.all()  # 모든 기업 데이터를 가져옴
    return render(request, 'appnewsclustering/home.html', {'companies': companies})

def home(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    return render(request, 'appnewsclustering/home.html', {'company': company})