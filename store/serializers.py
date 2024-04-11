from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name'] # "__all__ for all data"

        # def create(self, validated_data):
        #     return super().create(validated_data)

class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only =True)
    price_with_tax = serializers.SerializerMethodField()
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source ='category',
    )
    category=CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = (
            "name",
            # "description",
            # "price",
            "inventory",
            "discounted_price",
            "price_with_tax",
            "category_id",
            "category",
            # "is_sale",
            # "new_arrival",
        )

    def get_price_with_tax(self,product:Product):
        return (float(product.discounted_price) * 0.13) + float(product.discounted_price)

 
    
    # def create(self, validated_data):
    #     category=validated_data.get('category_id')
    #     validated_data.update({
    #         'category': Category.objects.get(id=category),

    #     })
    #     return super().create(validated_data)




    # class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()

    # def create(self, validated_data):
    #     # instance=Category.objects.create(name=validated_data.get("name"))
    #     instance=Category.objects.create(**validated_data)
    #     return instance

    # def update(self, instance, validated_data):
    #     instance.name=validated_data.get("name")
    #     instance.save()
    #     return instance