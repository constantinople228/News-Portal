from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('Post', 'PostCategory', 'Author')
    list_filter = ('category', 'post_type', 'time_create')
    search_fields = ('author', 'post_type', 'category', 'heading')


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
