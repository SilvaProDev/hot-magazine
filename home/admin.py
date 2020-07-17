from django.contrib import admin

# Register your models here.
from .models import Category, Produit, UserProfile, ContactMessage

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

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "phone", "ville"]
    list_filter = ["user"]

    list_per_page = 10
    fieldsets = [
        ('Info', {
            'fields':[
                "user",
                "phone",
                "address",
                "ville",
                "image",
                
            ]
        })
        
    ]

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "date_add", "noteadmin", "status"]
    list_filter = ["status"]
    

    fieldsets = [
        ('Info', {
            'fields':[
                "status",
                "noteadmin",
                "name",
                "email",
                "message",
                
            ]
        })
    ]
    readonly_fields = (
        'name',
        'email',
        'message',
    )



admin.site.register(Category, CategoryAdmin)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)