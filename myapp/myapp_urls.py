from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.home),
    path('privacy-policy', views.privacy),
    path('admin-rupali-login', views.adminLogin),
    path('site-admin-rupali', views.adminPanel),
    path('service-images', views.adminServiceImages),
    path('admin-messages', views.adminMessages),
    path('delete-message/<id>', views.deleteMessages),
    path('delete-image/<id>', views.deleteImage),
    path('delete-service-image/<id>', views.deleteImageFromOurServices),
    path('logout-admin/', views.adminLogout),
] 

from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)