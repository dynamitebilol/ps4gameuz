from modeltranslation.translator import register, TranslationOptions
from .models import  Game, HeroSection

@register(Game)
class GameTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(HeroSection)
class HeroTranslationOptions(TranslationOptions):
    fields = ('intro',)