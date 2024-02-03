from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import CustomUser


class MyCustomJWTAuthentication(JWTAuthentication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_model = CustomUser
