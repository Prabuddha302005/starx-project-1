from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.home),
    path('privacy-policy', views.privacy),
    path('admin-login', views.adminLogin),
    path('adminpanel', views.adminPanel),
    path('admin-messages', views.adminMessages),
    path('delete-message/<id>', views.deleteMessages),
    path('delete-image/<id>', views.deleteImage),
    path('logout', views.adminLogout),
] 

from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)