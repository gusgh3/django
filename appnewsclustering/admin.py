from django.contrib import admin
from .models import Company

# Register your models here.
# appnewsclustering/admin.py

admin.site.register(Company)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description1', 'description2', 'founded_date', 'headquarters')  # description2 추가
    search_fields = ('name', 'description1', 'description2', 'founded_date', 'headquarters')  # description2 검색 가능
    list_filter = ('headquarters') # 소재지를 기준으로 기업(company)을 필터링(분류)
