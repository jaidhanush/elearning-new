from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import TutorViewSet

router=DefaultRouter()
router.register('',TutorViewSet,basename='tutor')
app_name='tutor'


urlpatterns = [
    path('',include(router.urls))
]
