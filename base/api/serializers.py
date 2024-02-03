from rest_framework.serializers import ModelSerializer
from base.models import Note, CustomUser, Status, PersonalInfo
from base.models import Role, Group, Subscription, Investment, Draw


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'phone_no', 'email', 'password', 'full_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            phone_no=validated_data['phone_no'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class PersonalInfoSerializer(ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class InvestmentSerializer(ModelSerializer):
    class Meta:
        model = Investment
        fields = '__all__'


class DrawSerializer(ModelSerializer):
    class Meta:
        model = Draw
        fields = '__all__'
