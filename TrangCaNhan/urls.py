from rest_framework.routers import DefaultRouter
from .views import ThongtincanhanViewset, BantinViewset


router = DefaultRouter()
router.register(r'Thongtincanhan', ThongtincanhanViewset, basename='Thong tin ca nhan')
router.register(r'Bantin', BantinViewset, basename='Ban tin')

urlpatterns = router.urls