from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', views.ProductView)
router.register('projects', views.ProjectView)
router.register('requisitions', views.RequisitionView)
router.register('requisition_items', views.RequisitionMetaView)

urlpatterns = [
    path('', include(router.urls)),
]
