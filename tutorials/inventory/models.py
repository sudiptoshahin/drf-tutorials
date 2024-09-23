from django.db import models
import uuid


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=False)


class SeasonalEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Product(models.Model):

    IN_STOCK = "IS",
    OUT_OF_STOCK = "OOS",
    BACKORDERED = "BO"

    STOCK_STATUS = {
        IN_STOCK: "In Stock",
        OUT_OF_STOCK: "Out Of Stock",
        BACKORDERED: "Back Ordered"
    }
    
    pid = models.CharField(max_length=255)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True)
    is_digital = models.BooleanField(default=False)
    is_active = models.BooleanField()
    # Add by default while product will add `auto_now_add`  
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # update by default while product will add `auto_now`
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    stock_status = models.CharField(
        max_length=3,
        choices=STOCK_STATUS,
        default=OUT_OF_STOCK
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seasonal_events = models.ForeignKey(SeasonalEvents,
                                        on_delete=models.CASCADE)


class ProductLine(models.Model):
    price = models.DecimalField()
    sku = models.UUIDField(default=uuid.uuid4)
    stock_qty = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    order = models.IntegerField()
    weight = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField()

