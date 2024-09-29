from django.db import models
import uuid
from tutorials.utils.model_settings import StockStatus
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Category name',
        help_text="Enter a category name"
    )
    slug = models.SlugField(unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True,
                               blank=True)
    
    class Meta:
        verbose_name = "Inventory Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class SeasonalEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Product(models.Model):

    # STOCK_STATUS = {
    #     IN_STOCK: "In Stock",
    #     OUT_OF_STOCK: "Out Of Stock",
    #     BACKORDERED: "Back Ordered"
    # }
    
    pid = models.CharField(max_length=255)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(null=True)
    is_digital = models.BooleanField(default=False)
    is_active = models.BooleanField()
    # Add by default while product will add `auto_now_add`  
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # update by default while product will add `auto_now`
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    stock_status = models.CharField(
        max_length=3,
        choices=StockStatus,
        default=StockStatus.IN_STOCK
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True)
    seasonal_events = models.ForeignKey(SeasonalEvents,
                                        on_delete=models.CASCADE)
    product_type = models.ManyToManyField("ProductType",
                                          related_name='product_type')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    

class ProductLine(models.Model):
    price = models.DecimalField(max_digits=7, decimal_places=3)
    sku = models.UUIDField(default=uuid.uuid4)
    stock_qty = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    order = models.IntegerField()
    weight = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    attribute_values = models.ManyToManyField("AttributeValue",
                                              related_name="attribute_values")


class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField()


class Attribute(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    text = models.CharField(max_length=100, default="hello", null=True)

 
class ProductType(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True,
                               blank=True)
    
    class Meta:
        verbose_name = 'ProductType'
    
    
class AttributeValue(models.Model):
    attribute_value = models.CharField(max_length=100)
    attribute = models.ForeignKey('Attribute',
                                  related_name='attribute',
                                  on_delete=models.CASCADE)


# pivot table
class ProductLine_AttributeValue(models.Model):
    attribute_value = models.ForeignKey(AttributeValue,
                                        on_delete=models.CASCADE)
    product_line = models.ForeignKey(ProductLine, on_delete=models.CASCADE)


class Product_ProductType(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)


class StockControl(models.Model):
    stock_qty = models.IntegerField()
    name = models.CharField(max_length=100)
    stock_product = models.ForeignKey(Product, on_delete=models.CASCADE)