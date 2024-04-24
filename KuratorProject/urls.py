from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from KuratorProject.settings import MEDIA_URL, MEDIA_ROOT
from groups.views import main_page_view
from users.views import register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
    path('users/', include("users.urls")),
    path('accaounts/', include("django.contrib.auth.urls"))
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)