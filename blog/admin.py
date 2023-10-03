from django.contrib import admin
from .models import Post, Produto

class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'text', 'published_date',)
    ordering = ('title',)
    search_fields = ('title', 'text')
    list_filter = ('published_date',)
    #fields = [('title', 'author'), 'text', 'published_date']
    fieldsets = (
        (None, {
            'fields' : ('title', 'text')
        }),
        ('Publicação do post', {
            'fields': ('author', 'published_date')
        }),
    )
    
#class ProdutoAdmin(admin.ModelAdmin):
admin.site.register(Post, PostAdmin)
admin.site.register(Produto)
