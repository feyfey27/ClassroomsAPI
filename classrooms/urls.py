
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views as views1
from api_app import views as views2
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views1.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views1.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views1.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views1.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views1.classroom_delete, name='classroom-delete'),

    path('api/classrooms/', views2.ClassroomsList.as_view(), name="classrooms-list"), 
    path('api/classrooms/create/', views2.ClassroomCreateView.as_view(), name="classrooms-create"), 
    path('api/detail/<int:classroom_id>/', views2.ClassroomDetailView.as_view(), name="classroom-details"), 
    path('api/detail/<int:classroom_id>/update/', views2.ClassroomUpdateView.as_view(), name="update-classroom"), 
    path('api/detail/<int:classroom_id>/delete/', views2.ClassroomDeleteView.as_view(), name="cancel-classroom"), 

    path('login/', TokenObtainPairView.as_view(), name="login"),

]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
