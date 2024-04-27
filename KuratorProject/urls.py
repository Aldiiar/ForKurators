from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from KuratorProject.settings import MEDIA_URL, MEDIA_ROOT
from users.views import profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profile_view),
    path('users/', include("users.urls")),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)