from django.contrib import admin
from .models import User, Listing, Category

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	pass

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
	pass
