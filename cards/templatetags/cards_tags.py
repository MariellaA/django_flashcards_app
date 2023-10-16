from django import template

from cards.models import BOXES, Card

# create an instance of Library used for registering the template tags
register = template.Library()

# uses the Library instance’s .inclusion_tag() as a decorator. This tells Django that boxes_as_links is an inclusion ta
@register.inclusion_tag("cards/box_links.html")
def boxes_as_links():
    boxes = []

    for box_num in BOXES:   # loops over BOXES
        # defines card_count to keep track of the number of cards in the current box
        card_count = Card.objects.filter(box=box_num).count()
        # append a dictionary with the box number as key and the number of cards in the box as the value to the boxes list
        boxes.append({
            "number": box_num,
            "card_count": card_count,
        })

    # returns a dictionary with the boxes data
    return {"boxes", boxes}
