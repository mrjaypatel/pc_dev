from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

from .serializers import NoteSerializer, CustomUserSerializer, StatusSerializer
from .serializers import PersonalInfoSerializer, RoleSerializer, DrawSerializer
from .serializers import GroupSerializer, SubscriptionSerializer
from .serializers import InvestmentSerializer

from base.models import Note, CustomUser, Status, PersonalInfo, Role
from base.models import Group, Subscription, Investment, Draw

from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password


# @permission_classes([IsAuthenticated])
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


# @permission_classes([IsAuthenticated])
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    # permission_classes = (IsAuthenticated)

    # def get_object(self, queryset=None):
    #     obj = self.request.user
    #     return obj

    # def get_permissions(self):
    #     if self.action in ('create',):
    #         self.permission_classes = [AllowAny,]
    #     return super(self.__class__, self).get_permissions()

    # def create(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     serializer = CustomUserSerializer(data=request.data)  
    #     if serializer.is_valid():
    #         self.object.set_password(serializer.data.get("password"))
    #         # user = serializer.create(serializer.validated_data)
    #         self.object.save()
         
    #         return Response({"success": True})
    #     else:
    #         return Response(serializer.errors)

# @csrf_exempt
# def createUser(request):
#     phoneNo = request.POST.get('phone_no')  
#     username = request.POST.get('username')  
#     password = request.POST.get('password')
#     email = request.POST.get('email')
#     print("REQUEST FROM POSTMAN", request.raw_post_data)
#     user = CustomUser.objects.create_user(
#             phone_no=phoneNo,
#             email=email,
#             name=username,
#             password=password,
#         )
#     user.set_password(password)
#     user.save()
#     Response({"success": True})


# @permission_classes([IsAuthenticated])
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


# @permission_classes([IsAuthenticated])
class PersonalInfoViewSet(viewsets.ModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer


# @permission_classes([IsAuthenticated])
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


# @permission_classes([IsAuthenticated])
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# @permission_classes([IsAuthenticated])
class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


# @permission_classes([IsAuthenticated])
class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer


# @permission_classes([IsAuthenticated])
class DrawViewSet(viewsets.ModelViewSet):
    queryset = Draw.objects.all()
    serializer_class = DrawSerializer
