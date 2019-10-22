# import json

from django.db.models import Q
from django.shortcuts import get_object_or_404
# from django.http import HttpResponse

# from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt
# from django.http import Http404
# from django.utils.decorators import method_decorator

from rest_framework import mixins, status, generics
from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import IsAdminUser

from myapp import serializers
from myapp import models
from myapp.core.pagination import CustomPagination


class CorporateMainBranchCreateList(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):

    permission_classes = ()

    def get_queryset(self):
        return models.MainBranch.objects.all()

    def filter_queryset(self, queryset, corporate=None):
        q = Q()

        if corporate is not None:
            q &= Q(corporate=corporate)

        return queryset.filter(q)

    def get_serializer_class(self):
        return serializers.MainBranchSerializer

    def get_pagination_class(self, request):
        return CustomPagination

    def get(self, request, corporate):
        if request.GET.get('verbose') == "true":
            queryset = self.filter_queryset(self.get_queryset(), corporate)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        queryset = self.filter_queryset(self.get_queryset(), corporate)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, corporate):
        serializer_class = self.get_serializer_class()
        data = request.data

        if type(data) is not dict:
            data._mutable = True

        data['corporate'] = corporate
        serializer = serializer_class(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # NOQA
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CorporateMainBranchRetriveUpdateDelete(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView):

    permission_classes = ()

    def get_queryset(self):
        return models.MainBranch.objects.all()

    def filter_queryset(self, queryset, corporate=None):
        q = Q()

        if corporate is not None:
            q &= Q(corporate=corporate)

        return queryset.filter(q)

    def get_object(self, corporate=None, main_branch=None):

        if corporate is None and main_branch is None:
            return True

        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset, corporate)
        model = get_object_or_404(queryset, id=main_branch)
        return model

    def get_serializer_class(self):
        return serializers.MainBranchSerializer

    def get(self, request, corporate, main_branch):
        model = self.get_object(corporate, main_branch)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(model)
        return Response(serializer.data)

    def put(self, request, corporate, main_branch):
        model = self.get_object(corporate, main_branch)
        serializer_class = self.get_serializer_class()
        data = request.data

        if type(data) is not dict:
            data._mutable = True

        data['corporate'] = corporate
        serializer = serializer_class(model, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # NOQA
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, corporate, main_branch):
        model = self.get_object(corporate, main_branch)
        serializer_class = self.get_serializer_class()
        data = request.data

        if type(data) is not dict:
            data._mutable = True

        data['corporate'] = corporate
        serializer = serializer_class(model, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # NOQA
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, corporate, main_branch):
        model = self.get_object(corporate, main_branch)
        # model.delete()
        model.deleted = True
        model.save()
        return Response(status=status.HTTP_205_RESET_CONTENT)
