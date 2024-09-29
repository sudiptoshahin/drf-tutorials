from django.contrib import admin
from book_warehouse.models import Author, Publisher, Warehouse, Customer
from book_warehouse.models import ShoppingBasket, Book, ShoppingBasket_Book
from book_warehouse.models import Warehouse_Book


admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Warehouse)
admin.site.register(Customer)


class ShoppingBasketAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email')
    
    def customer_name(self, obj):
        return obj.basket_owner.name
    
    def customer_email(self, obj):
        return obj.basket_owner.email


admin.site.register(ShoppingBasket, ShoppingBasketAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'year', 'title', 'price', 'publisher_fk',
                    'author_fk')
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'publisher_fk':
            publishers = Publisher.objects.all()
            # publishers_fks = [publisher.name for publisher in publishers]
            kwargs['queryset'] = publishers
        if db_field.name == 'author_fk':
            authors = Author.objects.all()
            # authors_fks = [author.name for author in authors]
            kwargs['queryset'] = authors
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Book, BookAdmin)


class ShoppingBasket_BookAdmin(admin.ModelAdmin):
    list_display = ('book_isbn', 'count')
    

admin.site.register(ShoppingBasket_Book)


class Warehouse_BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'warehouse_address', 'count')
    
    def book_name(self, obj):
        return obj.book_isbn.title
    
    def warehouse_address(self, obj):
        return obj.warehouse.address
    
    def formfield_for_foreignkey(self, db_fields, request, **kwargs):
        if db_fields.name == 'book_isbn':
            kwargs['queryset'] = Book.objects.all()
        if db_fields.name == 'warehouse':
            kwargs['queryset'] = Warehouse.objects.all()
        
        return super().formfield_for_foreignkey(db_fields, request, **kwargs)
        

admin.site.register(Warehouse_Book)
