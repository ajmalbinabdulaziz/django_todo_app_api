from rest_framework import serializers
from my_app.models import ToDo


class TodoSerialiazer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()

    class Meta:
        model = ToDo
        fields = ['id', 'title', 'memo', 'created',
                  'datecompleted', 'important']


class TodoCompleteSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        read_only_fields = ['title', 'memo', 'created',
                            'datecompleted', 'important']
        fields = ['id', ]
