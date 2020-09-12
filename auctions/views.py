from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import User, Listing, Category 


def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def watchlist(request, username):
	return render(request,'auctions/watchlist.html')


class CategoriesListView(generic.ListView):
    model=Category
    def get_context_data(self, **kwargs):
        context=super(CategoriesListView, self).get_context_data(**kwargs)
        context['items']=Category.objects.all()

        return context


def create_listing(request, username):
    if request.method == 'GET':
        return render(request, 'auctions/create_listing.html',{'form':ListingForm(),"new":True})
    else:
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "auctions/create_listing.html",{'form':ListingForm(), 'saved': True})
        else:
            return render(request, "auctions/create_listing.html",{'form':form, 'saved':False})


class ListingDetailView(generic.DetailView):
    model= Listing
    context_object_name='item'