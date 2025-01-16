from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import CourseViewSet

router=DefaultRouter()
router.register('',CourseViewSet,basename='courses')
app_name='courses'


urlpatterns = [
    path('',include(router.urls))
]
