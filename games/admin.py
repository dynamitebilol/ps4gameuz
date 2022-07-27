from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Game, Category, HeroSection, Review

class CategoryAdmin(admin.ModelAdmin):

    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}  # new

admin.site.register(Category, CategoryAdmin)

@admin.register(Game)
class GameAdmin(TranslationAdmin):
    list_display = ("title", "description",)
    prepopulated_fields = {"slug": ("title",)}  # new

@admin.register(HeroSection)
class HeroAdmin(TranslationAdmin):
    list_display = ("title", "intro", "image", "category")



admin.site.register(Review)
