from django.contrib.auth.models import User

from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields = '__all__'


class CobSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    # {{my_custom_field_name}} = serializers.SerializerMethodField()

    # def get_{{my_custom_field_name}}(self, model):
    #   return NewModel.objects.all().filter(model=model).count()

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.Cob
        fields = '__all__'
        # fields = ( 'id', 'name', 'created_at', 'modified_at', )
        # extra_fields = ('{{my_custom_field_name}}', )
        # read_only_fields = ( 'created_at', 'modified_at', )


class CorporateSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    # {{my_custom_field_name}} = serializers.SerializerMethodField()

    # def get_{{my_custom_field_name}}(self, model):
    #   return NewModel.objects.all().filter(model=model).count()

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.Corporate
        fields = '__all__'
        # fields = ( 'mainbranch>', 'id', 'name', 'created_at', 'modified_at', ) # NOQA
        # extra_fields = ('{{my_custom_field_name}}', )
        # read_only_fields = ( 'created_at', 'modified_at', )


class MainBranchSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    # {{my_custom_field_name}} = serializers.SerializerMethodField()

    # def get_{{my_custom_field_name}}(self, model):
    #   return NewModel.objects.all().filter(model=model).count()

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.MainBranch
        fields = '__all__'
        # fields = ( 'branch>', 'id', 'name', 'created_at', 'modified_at', 'corporate', ) # NOQA
        # extra_fields = ('{{my_custom_field_name}}', )
        # read_only_fields = ( 'created_at', 'modified_at', )


class SubDomainSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    # {{my_custom_field_name}} = serializers.SerializerMethodField()

    # def get_{{my_custom_field_name}}(self, model):
    #   return NewModel.objects.all().filter(model=model).count()

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.SubDomain
        fields = '__all__'
        # fields = ( 'user>', 'notification>', 'id', 'name', 'created_at', 'modified_at', 'branch', ) # NOQA
        # extra_fields = ('{{my_custom_field_name}}', )
        # read_only_fields = ( 'created_at', 'modified_at', )


class RoleSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    # {{my_custom_field_name}} = serializers.SerializerMethodField()

    # def get_{{my_custom_field_name}}(self, model):
    #   return NewModel.objects.all().filter(model=model).count()

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.Role
        fields = '__all__'
        # fields = ( 'user>', 'id', 'name', )
        # extra_fields = ('{{my_custom_field_name}}', )
        # read_only_fields = ( )


class NotificationSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    # {{my_custom_field_name}} = serializers.SerializerMethodField()

    # def get_{{my_custom_field_name}}(self, model):
    #   return NewModel.objects.all().filter(model=model).count()

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.Notification
        fields = '__all__'
        # fields = ( 'notificationuser>', 'id', 'message', 'created_at', 'modified_at', 'sub_domain', ) # NOQA
        # extra_fields = ('{{my_custom_field_name}}', )
        # read_only_fields = ( 'created_at', 'modified_at', )


class CompanySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    # {{my_custom_field_name}} = serializers.SerializerMethodField()

    # def get_{{my_custom_field_name}}(self, model):
    #   return NewModel.objects.all().filter(model=model).count()

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.Company
        fields = '__all__'
        # fields = ( 'subdomain>', 'user>', 'id', 'name', 'created_at', 'modified_at', 'main_branch', ) # NOQA
        # extra_fields = ('{{my_custom_field_name}}', )
        # read_only_fields = ( 'created_at', 'modified_at', )


class UserNotificationSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    # {{my_custom_field_name}} = serializers.SerializerMethodField()

    # def get_{{my_custom_field_name}}(self, model):
    #   return NewModel.objects.all().filter(model=model).count()

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.UserNotification
        fields = '__all__'
        # fields = ( 'id', 'notification', 'user', 'has_readed_at', 'readed_at', 'created_at', 'modified_at', ) # NOQA
        # extra_fields = ('{{my_custom_field_name}}', )
        # read_only_fields = ( 'created_at', 'modified_at', )
