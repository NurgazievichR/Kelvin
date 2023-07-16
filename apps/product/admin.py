from django.contrib import admin

from apps.product.models import Product, ProductImage, ProductSize

admin.site.register(ProductImage)

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductSizeInline(admin.TabularInline):
    model = ProductSize

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    inlines = (ProductImageInline, ProductSizeInline)
