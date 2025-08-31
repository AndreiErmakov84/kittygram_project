from rest_framework.routers import DefaultRouter  # SimpleRouter

from django.urls import include, path

from cats.views import CatViewSet  # CatList, CatDetail  # APICat  # cat_list

# Создаётся роутер
# router = SimpleRouter()
router = DefaultRouter()
# Вызываем метод .register с нужными параметрами
router.register('cats', CatViewSet, basename='tiger')  # Префикс 'tiger'
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('', include(router.urls)),
    # path('cats/', CatList.as_view()),
    # path('cats/<int:pk>/', CatDetail.as_view()),
    # path('cats/', APICat.as_view()),
    # path('cats/', cat_list),
]
