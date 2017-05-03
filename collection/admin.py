from django.contrib import admin

# import your model
from collection.models import Blogpost

#set up automated slug creation
class BlogpostAdmin(admin.ModelAdmin):
    model = Blogpost
    list_display = ('title', 'author', 'posted')
    prepopulated_fields = {'slug': ('title',)}
# and register it
admin.site.register(Blogpost, BlogpostAdmin)
