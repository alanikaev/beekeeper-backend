from .models import Companies
from rest_framework import serializers

class CompaniesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Companies
		fields = ('id','name','desc','date')
