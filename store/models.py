from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255,unique=True)
    
    def __str__(self) -> str:
        return self.name
    
    # class Meta:
    #     verbose_name_plural = 'categories'


class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(null=True, blank=True)
    price=models.FloatField()
    # price=models.DecimalField(max_digits=6,decimal_places=2)
    discounted_price=models.FloatField()    
    # sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    inventory=models.IntegerField(default=0)
    is_sale = models.BooleanField(default=False)
    new_arrival = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    

# class Address(models.Model):
#     customer = models.OneToOneField('Customer', on_delete=models.CASCADE, primary_key=True)
#     street_name=models.CharField(max_length=255, blank=False)
#     tole_name=models.CharField(max_length=255, blank=False)


class Customer(models.Model):
    BRONZE_MEMBER='B'
    SILVER_MEMBER='S'
    GOLD_MEMBER='G'
    
    MEMBERSHIP=[
        (BRONZE_MEMBER,'Bronze'),
        (SILVER_MEMBER,'Silver'),
        (GOLD_MEMBER,'Gold'),
    ]
    
    MALE_CHOICE='M'
    FEMALE_CHOICE='F'
    OTHER_CHOICE='O'

    GENDER_CHOICE=[
        (MALE_CHOICE,'MALE'),
        (FEMALE_CHOICE,'FEMALE'),
        (OTHER_CHOICE,'OTHER'), 
    ]
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE)
    age = models.IntegerField(default = 18,null =True,blank =True)
    address = models.CharField(max_length=255)
    # address = models.ForeignKey(Address,on_delete=models.PROTECT, related_name="customer_address")
    contact = models.CharField(max_length=20)
    membership=models.CharField(max_length=1,choices=MEMBERSHIP,default=BRONZE_MEMBER)
    # customer=models.ForeignKey(User,on_delete=models.CASCADE, primary_key = True)
    # customer=models.ForeignKey(User,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.first_name} ({self.contact})"
 

class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    # user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="users_cart")
    # customer=models.ForeignKey(Customer,on_delete=models.CASCADE, primary_key = True)


class CartItem(models.Model):
    cart=models.ForeignKey("Cart",on_delete=models.CASCADE)
    product=models.ForeignKey("Product",on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField(default=1)
    # cart=models.ForeignKey("Cart",on_delete=models.CASCADE,related_name="cart_items")
    # product=models.ForeignKey("Product",on_delete=models.CASCADE,related_name="cart_products")
    # price=models.FloatField()


class Order(models.Model):
    PENDING_STATUS='P'
    CONFORMED_STATUS='CF'
    CANCLED_STATUS='CP'
    COMPLETED_STATUS='C'
    
    STATUS_CHOICES=[
        (PENDING_STATUS,"Pending"),
        (CONFORMED_STATUS,"Conformed"),
        (COMPLETED_STATUS,'Completed'),
        (CANCLED_STATUS,"Cancled")
    ]
    # customer=models.ForeignKey(Customer,on_delete=models.PROTECT, primary_key= True)
    # user=models.ForeignKey(User,on_delete=models.PROTECT)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    place_at=models.DateTimeField(auto_now=True)
    status_choices=models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING_STATUS)
    payment_status=models.BooleanField(default=False)
    shipping_address=models.CharField(max_length=255,default='', blank=False)
    # payment_status = models.BooleanField(default = False)


class OrderItem(models.Model):
    PENDING_STATUS='P'
    CONFORMED_STATUS='CF'
    CANCLED_STATUS='CP'
    COMPLETED_STATUS='C'
    
    STATUS_CHOICES=[
        (PENDING_STATUS,"Pending"),
        (CONFORMED_STATUS,"Conformed"),
        (COMPLETED_STATUS,'Completed'),
        (CANCLED_STATUS,"Cancled")
    ]
    order=models.ForeignKey("Order",on_delete=models.PROTECT)
    product=models.ForeignKey("Product",on_delete=models.PROTECT)
    price=models.FloatField()
    quantity=models.PositiveSmallIntegerField(default=1)
    status_CHOICES=models.CharField(max_length=2,choices=STATUS_CHOICES,default=PENDING_STATUS)

class Review(models.Model):
    STAR_RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    PRICE_RATING_CHOICES = (
        (1, '$'),
        (2, '$$'),
        (3, '$$$'),
        (4, '$$$$'),
        (5, '$$$$$'),

    )

    product=models.ForeignKey("Product",on_delete=models.CASCADE)
    Customer=models.ForeignKey("Customer",on_delete=models.CASCADE)
    product_rating  = models.IntegerField(choices=STAR_RATING_CHOICES)
    price_rating= models.IntegerField(choices=PRICE_RATING_CHOICES)

    def __str__(self):
        return self.product_rating

