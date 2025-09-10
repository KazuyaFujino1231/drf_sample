from rest_framework import serializers
from sample.model.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'birthday', 'email')
    
    def save(self, **kwargs):
        return super().save(**kwargs)
