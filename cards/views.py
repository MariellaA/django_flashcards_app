from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from cards.models import Card


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")  # for more control over the items that the database
    # returns; get all cards first ordered by their box in ascending order, then by their creation date in
    # descending order


class CardCreateView(CreateView):  # the web page where new cards are created will contain a form with fields that must be filled out
    model = Card
    fields = ["question", "answer", "box"]  # define the fields that the form should show
    success_url = reverse_lazy("card-create")  # When the form is sent, Django will check the form and return the
    # request to the URL that is set for success_url. In this case, it’s the same view again. That way, cards can be
    # created one after another without navigating back and forth.


class CardUpdateView(CardCreateView, UpdateView):  # creating a subclass of CardCreateView and UpdateView to inherit the
    # class attributes from both parent classes and modify the attributes
    success_url = reverse_lazy("card-list")  # returning to the card-list page after editing a card


class BoxView(CardListView):    # creating BoxView as a subclass of CardListView. Django would serve the card_list.html
    # template for a CardListView by default. So the template_name is overwritten to point to the box.html template.
    template_name = "cards/box.html"

    # Instead of listing all cards, .get_queryset() is used to adjust the query set that BoxView returns.
    # returns the cards where the box number matches the box_num value.
    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_num"])

    # the value of box_num is passed as a keyword argument in the GET request. To use the box number in the
    def get_context_data(self, **kwargs):
        # template, .get_context_data() is used and box_num is added as box_number to the view’s context.
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]  # used the variable name box_number to differentiate it from
        # the box_num keyword argument
        return context
