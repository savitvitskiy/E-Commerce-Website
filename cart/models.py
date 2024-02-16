# from django.db import models
# from products.models import Product


# # Create your models here.
# class OrderItem(models.Model):
#     product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return self.product.name


# class Order(models.Model):
#     ref_code = models.CharField(max_length=15)
#     items = models.ManyToManyField(OrderItem)

#     def get_cart_items(self):
#         return self.items.all()

#     def get_cart_total(self):
#         return sum([item.product.price for item in self.items.all()])
