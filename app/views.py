from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Companies
from .serializer import CompaniesSerializer

# class CompaniesList(mixins.ListModelMixin,
# 					mixins.CreateModelMixin,
# 					generics.GenericAPIView):
# 	queryset = Companies.objects.all()
# 	serializer_class = CompaniesSerializer

# 	def get(self, request, *args, **kwargs):
# 		return self.list(request, *args, **kwargs)

# 	def post(self, request, format=None):
# 		return self.create(request, *args, **kwargs)

# class CompanyDetail(mixins.RetrieveModelMixin,
# 					mixins.UpdateModelMixin,
# 					mixins.DestroyModelMixin,
# 					generics.GenericAPIView):
# 	queryset = Companies.objects.all()
# 	serializer_classs = CompaniesSerializer

# 	def get(self, request, *args, **kwargs):
# 		return self.retrieve(request, *args, **kwargs)
# 	def put(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)
# 	def delete(self, request, *args, **kwargs):
# 		return self.destroy(request, *args, **kwargs)	


class CompaniesList(generics.ListCreateAPIView):
	queryset = Companies.objects.all()
	serializer_class = CompaniesSerializer
class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Companies.objects.all()
	serializer_class = CompaniesSerializer
