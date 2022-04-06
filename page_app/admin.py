from django.contrib import admin
from .models import *


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass 
class PublicationAdmin(admin.ModelAdmin):
    pass 
class CategoryAdmin(admin.ModelAdmin):
    pass 
class BookAdmin(admin.ModelAdmin):
    pass 
class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Customer, CustomerAdmin)
