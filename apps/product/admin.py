from django.contrib import admin

from apps.product.models import Product, ProductImage

admin.site.register(ProductImage)

class ProductImageInline(admin.TabularInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    inlines = (ProductImageInline,)

