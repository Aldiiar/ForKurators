from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from KuratorProject.settings import MEDIA_URL, MEDIA_ROOT
from users.views import profile_view
from groups import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profile_view),
    path('groups/', views.group_view),
    path('groups/<int:pk>/', views.group_detail_view, name='group_detail'),
    path('groups/<int:pk>/add_student/', views.add_student, name='add_student'),
    path('student/<int:pk>/', views.student_detail_view, name='student_detail'),
    path('student/<int:pk>/edit/', views.edit_student, name='edit_student'),
    path('student/<int:pk>/delete/', views.delete_student, name='delete_student'),
    path('users/', include("users.urls")),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)