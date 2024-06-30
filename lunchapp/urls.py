from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RestaurantViewSet, MenuViewSet, VoteViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
