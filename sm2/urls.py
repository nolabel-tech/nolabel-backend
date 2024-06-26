from django.contrib import admin
from django.urls import path, include

from api.views import RegisterView, LoginView, ContactView, SendMessageView, CheckMessagesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/contact/', ContactView.as_view(), name='contact'),
    path('api/send_message/', SendMessageView.as_view(), name='send_message'),
    path('api/check_messages/<str:unique>/', CheckMessagesView.as_view(), name='check_message'),  # Исправленный путь
]