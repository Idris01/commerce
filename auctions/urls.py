from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<str:username>/watchlist", views.watchlist, name="watchlist"),
    path("categories", views.CategoriesListView.as_view(template_name='auctions/categories.html'), name="categories"),
    path("<str:username>/create_listing", views.create_listing, name="create_listing"),
    path('listing/<int:pk>', views.ListingDetailView.as_view(), name='listing_detail'), 
    
]