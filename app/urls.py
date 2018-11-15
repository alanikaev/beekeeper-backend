from django.contrib import admin
from django.urls import path
from app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	path('admin/', admin.site.urls),
	path('companies/', views.CompaniesList.as_view()),
	path('companies/<int:pk>/', views.CompanyDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)