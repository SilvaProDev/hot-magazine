from django.contrib import admin

# Register your models here.
from .models import Category, Produit

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["titre", "date_add", "status"]
    list_filter = ["status"]
    list_search = ["titre"]
    prepopulated_fields = {'slug': ('titre',)}

    list_per_page = 10
    date_hierarchy = "date_add"
    fieldsets = [
        ('Info', {
            'fields':[
                "titre",
                "description",
                "image",
                "details",
                "slug",
                
                
            ]
        }),
        ('Status et Activation', {
            'fields':[
                "status",
            
            ]
        })

    ]

class ProduitAdmin(admin.ModelAdmin):
    list_display = ["titre", "categorie", "date_add", "status"]
    list_filter = ["status"]
    prepopulated_fields = {'slug': ('titre',)}

    list_per_page = 10
    date_hierarchy = "date_add"
    fieldsets = [
        ('Info', {
            'fields':[
                "categorie",
                "titre",
                "description",
                "image",
                "prix",
                "details",
                "slug",
                
            ]
        }),
        ('Status et Activation', {
            'fields':[
                "status",

            ]
        })

    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Produit, ProduitAdmin)