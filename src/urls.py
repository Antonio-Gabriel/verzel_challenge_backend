from django.urls import path

from rest_framework.routers import SimpleRouter

from .services import ModuleServiceViewSet, LessonServiceViewSet, UserServiceViewSet

from .services.user_service import UserLoginAPIView

router = SimpleRouter()
router.register("modules", ModuleServiceViewSet)
router.register("lessons", LessonServiceViewSet)
router.register("users", UserServiceViewSet)

urlpatterns = [
    path("user/login/", UserLoginAPIView.as_view()),
]
