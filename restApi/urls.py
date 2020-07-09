from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from cart.views import export
from languages.urls import router

urlpatterns = [
    # path('', export),
    path('admin/', admin.site.urls),
    # path('api/', include('languages.urls')),
    # path('api/', include('cart.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "restAPi Admin"
admin.site.site_title = "restAPi Admin Panel"
admin.site.index_title = "Dashboard"
