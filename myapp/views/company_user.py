import json

from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers

from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.utils.decorators import method_decorator

from rest_framework import mixins, status, viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import IsAdminUser

from myapp import serializers
from myapp import models
from myapp.core.pagination import CustomPagination


class CompanyUserCreateList(
		mixins.ListModelMixin,
		mixins.CreateModelMixin,
		generics.GenericAPIView
	):

	permission_classes = ()

	def get_queryset(self):
		return models.User.objects.all()

	def filter_queryset(self, queryset, company=None):
		q = Q()

		if not company == None:
			q &= Q(company=company)

		return queryset.filter(q)

	def get_serializer_class(self):
		return serializers.UserSerializer

	def get_pagination_class(self, request):
		return CustomPagination

	def get(self, request, company):
		
		if request.GET.get('verbose') == "true":
			queryset = self.filter_queryset(self.get_queryset(), company)
			serializer = self.get_serializer(queryset, many=True)
			return Response(serializer.data)

		queryset = self.filter_queryset(self.get_queryset(), company)
		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)
		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request, company):
		serializer_class = self.get_serializer_class()
		data = request.data

		if type(data) is not dict:
			data._mutable = True

		data['company'] = company
		serializer = serializer_class(data=data)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class CompanyUserRetriveUpdateDelete(
		mixins.RetrieveModelMixin,
		mixins.UpdateModelMixin,
		mixins.DestroyModelMixin,
		generics.GenericAPIView
	):

	permission_classes = ()

	def get_queryset(self):
		return models.User.objects.all()

	def filter_queryset(self, queryset, company=None):
		q = Q()

		if not company == None:
			q &= Q(company=company)

		return queryset.filter(q)

	def get_object(self, company=None, user=None):

		if  company is None and user is None:
			return True

		queryset = self.get_queryset()
		queryset = self.filter_queryset(queryset, company)
		model = get_object_or_404(queryset, id=user)
		return model

	def get_serializer_class(self):
		return serializers.UserSerializer

	def get(self, request, company, user):
		model = self.get_object(company, user)
		serializer_class = self.get_serializer_class()
		serializer = serializer_class(model)
		return Response(serializer.data)

	def put(self, request, company, user):
		model = self.get_object(company, user)
		serializer_class = self.get_serializer_class()
		data = request.data

		if type(data) is not dict:
			data._mutable = True

		data['company'] = company
		serializer = serializer_class(model, data=data)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)

	def patch(self, request, company, user):
		model = self.get_object(company, user)
		serializer_class = self.get_serializer_class()
		data = request.data

		if type(data) is not dict:
			data._mutable = True

		data['company'] = company
		serializer = serializer_class(model, data=data, partial=True)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request, company, user):
		model = self.get_object(company, user)
		# model.delete()
		model.deleted = True
		model.save()
		return Response(status=status.HTTP_205_RESET_CONTENT)
