# from django.urls import path

from rest_framework.routers import SimpleRouter

from .services import ModuleServiceViewSet, LessonServiceViewSet

router = SimpleRouter()
router.register("modules", ModuleServiceViewSet)
router.register("lessons", LessonServiceViewSet)
