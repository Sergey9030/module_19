from django.contrib import admin
from .models import Buyer, Game, News


# Register your models here.
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age') #Поля для отображения в списке
    search_fields = ('name',) #Поле для поиска
    list_filter = ('balance', 'age') #Поля для фильтрации
    list_per_page = 30 #Количество записей на странице
    readonly_fields = ('balance',) #Поле только для чтения


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')  # Поля для отображения в списке
    search_fields = ('title',)  # Поле для поиска
    list_filter = ('size', 'cost')  # Поля для фильтрации
    list_per_page = 20  # Количество записей на странице


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date')  # Поля для отображения в списке
