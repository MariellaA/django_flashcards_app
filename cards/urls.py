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
]
