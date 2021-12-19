from rest_framework import serializers
from .models import User, JuristicPerson, Department


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['user_id', 'phone', 'first_name', 'last_name', 'middle_name', 'is_active']

        # fields = ['user_id', 'phone', 'additional_phone_numbers', 'first_name', 'last_name',
        #           'middle_name', 'email', 'is_active', 'type', 'sex', 'timezone', 'vk', 'fb',
        #           'ok', 'instagram', 'telegram', 'whats_app', 'viber', 'created_at', 'updated_at']


class JuristicPersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = JuristicPerson
        fields = ['jurist_id', 'full_name', 'abbreviation', 'inn', 'kpp', 'created_at', 'updated_at', 'department']
        depth = 7


class DepartmentSerializer(serializers.ModelSerializer):

    # clients = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ['department_id', 'name', 'parent', 'clients']
        depth = 7
