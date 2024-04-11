# from django.shortcuts import render, get_object_or_404
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import action
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.status import HTTP_404_NOT_FOUND
# from rest_framework import mixins
# from rest_framework import generics
from .pagination import CustomPagination

# TO BACKUP:  python -Xutf8 dumpdata > backup.json  
# TO LOADUP BACKUP: python manage.py loaddata backup.json

# Create your views here.

class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
#     # if u wish to make new viewset use decorators bata action 
#     @action(detail=True,methods=['GET'])
#     def verify(self, request, pk=None):
#         return Response("ok")
 
class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.select_related('category').all()
    serializer_class=ProductSerializer
    pagination_class=CustomPagination




# GENERICS
# class CategoryList(generics.ListCreateAPIView):
#     queryset=Category.objects.all()
#     serializer_class=CategorySerializer

# #     def get(self, request, *args, **kwargs):
# #         self.queryset
# #         self.serializer_class(self.queryset,many=True)

# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Category.objects.all()
#     serializer_class=CategorySerializer







# MIXIN METHODS:
# class CategoryList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Category.objects.all()
#     serializer_class=CategorySerializer

#     def get(self,request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)
    
# class CategoryDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
    
#     queryset=Category.objects.all()
#     serializer_class=CategorySerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)






# class CategoryList(APIView):     
        # def get(self, request):
        #     categories=Category.objects.all()
        #     serializer=CategorySerializer(categories,many=True)
        #     return Response(serializer.data)
     
        # def post(self, request):
        #     serializer=CategorySerializer(data=request.data)
        #     serializer.is_valid(raise_exception=True)
        #     serializer.save()
        #     return Response({
        #         'details': "New Category created",
        #     },
        #     status=status.HTTP_201_CREATED)
     
# class CategoryDetail(APIView):
        # def get_object(self,pk):
        #     try:
        #         return Category.objects.get(pk=pk)
        #     except Category.DoesNotExist:
        #         raise HTTP_404_NOT_FOUND

        # def get(self, request, pk):
        #     category=self.get_object(pk)
        #     serializer=CategorySerializer(category)
        #     return Response(
        #         serializer.data
        #     )

        # def put(self, request, pk):
        #     category=self.get_object(pk)
        #     serializer=CategorySerializer(category,data=request.data)
        #     serializer.is_valid(raise_exception=True) 
        #     serializer.save()
        #     return Response({
        #             'details': 'data have been updated'
        #     })            

        # def delete(self, request, pk):
        #     category=self.get_object(pk) 
        #     category.delete()
        #     return Response(
        #         status=status.HTTP_204_NO_CONTENT
        #     )







# @api_view(['GET','POST'])
# def category_list(request):

#     if request.method == 'GET':
#         categories=Category.objects.all()
#         serailizer=CategorySerializer(categories, many=True)
#         return Response(serailizer.data)
#     else:
#         serializer=CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             'details': "New Category created",
#         },
#         status=status.HTTP_201_CREATED)
    
#         # else:
#     #     serializer=CategorySerializer(data=request.data)

#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response({
#     #             'details': "New Category created",
#     #         })
        
#     #     return Response({
#     #         'error': "Error in creating category",
#     #     })


# # @api_view(['GET','DELETE'])
# # def category_detail(request,pk):
# #     try:
# #         category=Category.objects.get(pk=pk)
# #         if request.method == 'GET':
# #             serializer=CategorySerializer(category)
# #             return Response(
# #                 serializer.data,
# #             )
# #         if request.method=="DELETE":
# #             category.delete()
# #             return Response(
# #                 status=status.HTTP_204_NO_CONTENT
# #             )
# #     except Category.DoesNotExist:
# #         return Response({
# #             'details': 'data not found',
# #         },
# #             'data not found',
# #             status= status.HTTP_404_NOT_FOUND
# #         )
    
# @api_view(['GET','DELETE','PUT'])
# def category_detail(request,pk):
#         category=get_object_or_404(Category,pk=pk)
#         if request.method == 'GET':
#             serializer=CategorySerializer(category)
#             return Response(
#                 serializer.data,
#             )
#         if request.method=="DELETE":
#             category.delete()
#             return Response(
#                 status=status.HTTP_204_NO_CONTENT
#             )
#             )
#     except Category.DoesNotExist:
#         return Response({
#             'details': 'data not found',
#         },
#             'data not found',
#             status= status.HTTP_404_NOT_FOUND
#         )
#             )                                               
#     except Category.DoesNotExist:
#         return Response({
#             'details': 'data not found',
#         },
#             'data not found',
#             status= status.HTTP_404_NOT_FOUND
#         )
        
#         if request.method=='PUT':
#             serializer=CategorySerializer(category,data=request.data)
#             serializer.is_valid(raise_exception=True) 
#             serializer.save()
#             return Response({
#                  'details': 'data have been updated'
#             })            
