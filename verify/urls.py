from django.urls import path
from verify.views import PasswordView

urlpatterns = [
    path('', PasswordView.as_view(), name='password'),
]