from django.contrib import admin


from .models import Video, Photo


class PersikAdminVideo(admin.ModelAdmin):
    #adding aditional params for searching in admin panel
    list_display = ('id', 'title', 'description', 'create_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_filter = ('id', 'create_at')


class PersikAdminPhoto(admin.ModelAdmin):
    list_display = ('id', 'create_at')
    list_display_links = ('id', 'create_at')
    search_fields = ('id', 'create_at')
    list_filter = ('id', 'create_at')

admin.site.register(Video, PersikAdminVideo)
admin.site.register(Photo, PersikAdminPhoto)
