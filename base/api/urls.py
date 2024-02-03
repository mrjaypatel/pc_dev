from django.urls import path, include
from rest_framework import routers
from base.api.views import NoteViewSet, CustomUserViewSet, StatusViewSet
from base.api.views import RoleViewSet, PersonalInfoViewSet, GroupViewSet
from base.api.views import DrawViewSet, InvestmentViewSet, SubscriptionViewSet
router = routers.DefaultRouter()
router.register(r'note', NoteViewSet)
router.register(r'user', CustomUserViewSet)
router.register(r'status', StatusViewSet)
router.register(r'personalInfo', PersonalInfoViewSet)
router.register(r'role', RoleViewSet)
router.register(r'group', GroupViewSet)
router.register(r'subscription', SubscriptionViewSet)
router.register(r'investment', InvestmentViewSet)
router.register(r'draw', DrawViewSet)


urlpatterns = [
       path('', include(router.urls)),
       # path('create/', createUser)

]
