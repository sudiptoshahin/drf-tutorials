from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.pagination import PageNumberPagination
from book_warehouse.serializers import BookSerializer
from book_warehouse.models import Book
# from utils.custom_paginations import LargeResultsSetPagination
from tutorials.utils.custom_paginations import CustomPagination


def warehouse_home(request):
    return render(request, 'book_warehouse/index.html', {})


class BookList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # pagination_class = LargeResultsSetPagination
    # custom
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('create-successfully')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(f'SERIALIZER-ERROR: {serializer.errors}')
            serializer_errors = serializer.errors
            errors = {}
            if 'invalid pk' in serializer_errors['publisher_fk'][0].lower():
                errors['message'] = "Not found Publisher or Author"
                
            return Response(
                errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def put(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print('INVALID...')
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class BookDetailView(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get(self, request, *args, **kwargs):
        print(f'---------->{request}<---------------')
        
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer