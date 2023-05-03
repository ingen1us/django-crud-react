from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        #puedo usar esto para hacer que use todos los campos
        # fields = '__all__'
        fields = ('id', 'title', 'description', 'done')