from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from .views import TagViewSet, IngredientViewSet, RecipeViewSet, UserViewSet


router = DefaultRouter()

router.register("tags", viewset=TagViewSet, basename="tag")
router.register(
    "ingredients", viewset=IngredientViewSet, basename="ingredient"
)
router.register("recipes", viewset=RecipeViewSet, basename="recipe")
router.register("users", viewset=UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls.authtoken")),
    path(
        "redoc/",
        TemplateView.as_view(
            template_name="redoc.html",
            extra_context={"schema_url": "openapi-schema"}
        ),
        name="redoc",
    ),
]
