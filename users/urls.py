from django.urls import path
from django.conf.urls.static import static
from KuratorProject.settings import MEDIA_URL, MEDIA_ROOT
from .views import profile_view, login_view, logout_view, register_view

app_name = "users"

urlpatterns = [
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('registration/', register_view, name='registration'),  # Добавлен URL-шаблон для регистрации
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)