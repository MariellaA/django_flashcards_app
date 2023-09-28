from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from cards.models import Card


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")  # for more control over the items that the database
    # returns; get all cards first ordered by their box in ascending order, then by their creation date in
    # descending order


class CardCreateView(CreateView):   # the web page where new cards are created will contain a form with fields that must be filled out
    model = Card
    fields = ["question", "answer", "box"]  # define the fields that the form should show
    success_url = reverse_lazy("card-create")   # When the form is sent, Django will check the form and return the
    # request to the URL that is set for success_url. In this case, it’s the same view again. That way, cards can be
    # created one after another without navigating back and forth.

class CardUpdateView(CardCreateView, UpdateView): # creating a subclass of CardCreateView and UpdateView to inherit the
    # class attributes from both parent classes and modify the attributes
    success_url = reverse_lazy("card-list")  # returning to the card-list page after editing a card
