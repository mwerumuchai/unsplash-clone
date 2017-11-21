from django.contrib import admin
from .models  import User, Gallery, Tags

class UnsplashAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

# Register your models here.
admin.site.register(User)
admin.site.register(Gallery,UnsplashAdmin)
admin.site.register(Tags)
