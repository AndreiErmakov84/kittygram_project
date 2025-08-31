# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import generics
# from rest_framework import status
from rest_framework import viewsets

from .models import Cat
from .serializers import CatSerializer


# Универсальные низкоуровневые классы
# class APICat(APIView):
#     def get(self, request):
#         cats = Cat.objects.all()
#         serializer = CatSerializer(cats, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class APIPostDetail(APIView):
#     def get(self, request, pk):
#         post = Post.objects.get(id=pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         post = Post.objects.get(id=pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk):
#         post = Post.objects.get(id=pk)
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#     def delete(self, request, pk):
#         post = Post.objects.get(id=pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Дженерики
# class CatList(generics.ListCreateAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


# class CatDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


# Если бы пользователи могли оставлять комментарии к котикам,
# то эндпоинт для работы с комментариями выглядел бы примерно так:
# cats/{cat_id}/comments/

# class CommentViewSet(viewsets.ModelViewSet):
#     serializer_class = CommentSerializer
#     # queryset во вьюсете не указываем
#     # Нам тут нужны не все комментарии, а связанные с котом с id=cat_id
#     # Поэтому нужно переопределить метод get_queryset и применить фильтр
#     def get_queryset(self):
#         # Получаем id котика из эндпоинта
#         cat_id = self.kwargs.get("cat_id")
#         # И отбираем только нужные комментарии
#         new_queryset = Comment.objects.filter(cat=cat_id)
#         return new_queryset
# В этом случае роутере обязательно нужно указать префикс basename


"""
view-функции

from rest_framework import status
from rest_framework.decorators import api_view  # Импортировали декоратор
from rest_framework.response import Response  # Импортировали класс Response

from .models import Cat
from .serializers import CatSerializer


@api_view(['GET', 'POST'])  # Применили декоратор и указали разрешённые методы
def hello(request):
    # По задумке, в ответ на POST-запрос нужно вернуть JSON с теми данными,
    # которые получены в запросе.
    # Для этого в объект Response() передаём словарь request.data.
    if request.method == 'POST':
        return Response({'message': 'Получены данные', 'data': request.data})

    # В ответ на GET-запрос нужно вернуть JSON
    # Он тоже будет создан из словаря, переданного в Response()
    return Response({'message': 'Это был GET-запрос!'})


@api_view(['GET', 'POST'])
def cat_list(request):
    if request.method == 'POST':
        # Создаём объект сериализатора
        # и передаём в него данные из POST-запроса
        # Чтобы сериализатор был готов принять список объектов, в конструктор
        # сериализатора нужно передать именованный параметр many=True.
        serializer = CatSerializer(data=request.data, many=True)
        # cat = Cat.objects.get(id=id)
        # serializer = CatSerializer(cat, data=request.data)
        # Если вызвать serializer.save(), будет обновлён существующий Cat
        # Если при создании экземпляра сериализатора указать partial=True —
        # отсутствие в запросе обязательных полей не приведёт к ошибке.
        # serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            # Если полученные данные валидны —
            # сохраняем данные в базу через save().
            serializer.save()
            # Возвращаем JSON со всеми данными нового объекта
            # и статус-код 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Если данные не прошли валидацию —
        # возвращаем информацию об ошибках и соответствующий статус-код:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    cats = Cat.objects.all()
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)
"""
