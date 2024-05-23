from django.contrib import admin
from .models import Translate

@admin.register(Translate)
class TranslateAdmin(admin.ModelAdmin):
    list_display = ('french_text', 'english_text', 'image')
