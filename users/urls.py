from django.urls import path
from django.conf.urls.static import static
from KuratorProject.settings import MEDIA_URL, MEDIA_ROOT
from .views import profile_view
app_name = "users"

urlpatterns = [
    path('profile', profile_view, name='profile')
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)