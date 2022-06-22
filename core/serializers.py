from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseSerializer

class UserCreateSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']