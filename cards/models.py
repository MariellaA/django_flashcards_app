from django.db import models

NUM_BOXES = 5  # number of boxes wanted in the app
BOXES = range(1, NUM_BOXES + 1)  # for looping through the boxes, beginning from 1 instead of 0


class Card(models.Model):  # The Card model defines that the database should contain a table, which stores cards
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    box = models.IntegerField(  # keeps track of the box number where each card sits
        choices=zip(BOXES, BOXES),  # makes sure models.IntegerField must contain a number that’s within the BOXES range
        default=BOXES[0],  # By default, the created flashcard is in the first box
    )
    date_created = models.DateTimeField(auto_now_add=True)  # With the date_created field, the newest cards can be shown
    # first in the card overview

    def __str__(self):  # Used to control the string representation of the Card objects
        return self.question
