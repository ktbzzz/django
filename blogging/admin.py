from django.contrib import admin
from blogging.models import Post, Category

# and a new admin registration
#admin.site.register(Post)

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts', )

admin.site.register(Category, CategoryAdmin)

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, ]