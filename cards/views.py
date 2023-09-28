from django.shortcuts import render
from django.views.generic import ListView

from cards.models import Card


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")  # for more control over the items that the database
    # returns; get all cards first ordered by their box in ascending order, then by their creation date in
    # descending order
