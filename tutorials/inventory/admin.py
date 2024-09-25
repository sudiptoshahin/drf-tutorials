from django.contrib import admin
from inventory.models import Category, Product, ProductType


# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name',)}

# admin.site.register(Category, CategoryAdmin)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ['name', 'slug']
    

class ProductAdmin(admin.ModelAdmin):
    list_filter = ("stock_status",)
    
    
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)