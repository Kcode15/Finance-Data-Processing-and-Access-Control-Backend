from rest_framework.routers import DefaultRouter
from .views import UserViewSet , FinancialRecordViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('records', FinancialRecordViewSet)
urlpatterns = router.urls