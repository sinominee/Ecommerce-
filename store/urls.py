from django.urls import path
from .views import *

from rest_framework.routers import SimpleRouter
routers=SimpleRouter()
routers.register('categories',CategoryViewset,basename='category')
routers.register('products',ProductViewset,basename='product')


urlpatterns = [
    # path('categories',category_list),
    # path('categories/<pk>',category_detail),

    # path('categories',CategoryList.as_view()),
    # path('categories/<pk>',CategoryDetail.as_view()),

    # path('categories',CategoryViewset.as_view({
    #     'get':'list',
    #     'post':'create',       
    # }),name="categories"),
    # path('categories/<pk>',CategoryViewset.as_view({
    #     'get':'retrieve',
    #     'put':'update',
    #     'delete':'destroy',
    # })),
    
]+ routers.urls