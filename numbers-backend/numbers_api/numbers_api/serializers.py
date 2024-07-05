from rest_framework import serializers
from numbers_dashboard.models import NumberM


class NumberMSerializer(serializers.ModelSerializer):
    class Meta:
        model=NumberM
        fields = '__all__'
        # read_only_fields = fields

