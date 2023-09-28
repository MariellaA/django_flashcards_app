from django.urls import path

from cards import views

# REMOVED: from django.views.generic import TemplateView

urlpatterns = [
    path(
        "",
        #TemplateView.as_view(template_name="cards/base.html"),
        # REPLACE WITH
        views.CardListView.as_view(),
        name="card-list"     # with the name attribute, views can be referenced more conveniently
    ),
    path(
        "new",
        views.CardCreateView.as_view(),
        name="card-create"
    ),
    path(
        "edit/<int:pk>", # Since an existing card is being edited, a primary key (pk) is needed to identify which card
        # to update
        views.CardUpdateView.as_view(),
        name="card-update"
    )
]
