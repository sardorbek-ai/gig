from django.urls import path
from .views import MainIndex, UploadPost
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path("", MainIndex.as_view(), name="index"),
    path("upload/", UploadPost.as_view(), name="upload"),
    path("cat/<int:id>/", MainIndex.as_view(), name="cat")
]+ static(settings.MEDIA_URL, documen_root=settings.MEDIA_URL)
