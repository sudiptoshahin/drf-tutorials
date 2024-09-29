from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=100)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True,
                               blank=True)
    
    def __str__(self):
        return self.name


class Warehouse(models.Model):
    code = models.CharField(max_length=10)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return self.address


class Customer(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, unique=True, blank=True,
                             null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name


class ShoppingBasket(models.Model):
    basket_owner = models.ForeignKey('Customer', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True,
                               blank=True)
    
    def __str__(self):
        return f"Shopping Basket for {self.basket_owner.name}"


class Book(models.Model):
    isbn = models.CharField(max_length=255, unique=True)
    year = models.CharField(max_length=5)
    title = models.CharField(max_length=100)
    price = models.FloatField(max_length=19)
    # check to use CASCADE if PROTECT is not worked
    publisher_fk = models.ForeignKey('Publisher', on_delete=models.PROTECT,
                                     related_name='book_publisher')
    author_fk = models.ForeignKey('Author', on_delete=models.PROTECT,
                                  related_name='book_author')


class ShoppingBasket_Book(models.Model):
    # shopping basket id will provide by django
    # change model.SET_NULL <-> models.CASCADE
    shopping_basket = models.ForeignKey(ShoppingBasket,
                                        on_delete=models.CASCADE)
    book_isbn = models.ForeignKey('Book', on_delete=models.CASCADE, null=True,
                                  blank=True)
    count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        # self.book_count = self.book_isbn.count()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.book_isbn.title} | {self.count}"


class Warehouse_Book(models.Model):
    book_isbn = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True,
                                  blank=True)
    count = models.PositiveIntegerField(default=0)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.SET_NULL,
                                  null=True, blank=True)
    
    def __str__(self):
        return f"Warehouse no:{self.warehouse.code} | {self.book_isbn.title}"

    def save(self, *args, **kwargs):
        # self.count = self.book_isbn.count()
        super().save(*args, **kwargs)
    
    