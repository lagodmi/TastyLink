from django.conf import settings
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from .views import (
    TagViewSet,
    IngredientViewSet,
    RecipeViewSet,
    UserViewSet,
    RedocView
)


router = DefaultRouter()

router.register("tags", viewset=TagViewSet, basename="tag")
router.register("ingredients", viewset=IngredientViewSet,
                basename="ingredient")
router.register("recipes", viewset=RecipeViewSet, basename="recipe")
router.register("users", viewset=UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls.authtoken")),
    path("redoc/", RedocView.as_view(), name="redoc"),
    path(
        "redoc/openapi-schema.yml",
        TemplateView.as_view(
            template_name=settings.BASE_DIR / "docs" / "openapi-schema.yml",
            content_type="text/yaml",
        ),
    ),
]
