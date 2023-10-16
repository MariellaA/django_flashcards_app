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

    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]  # evaluating whether the card should be moved forward into the
        # next box or back to the first box.

        # Note that new_box could even be 6 if the answer to a card that resided in your fifth box is correct.
        # That’s why the new self.box value is saved only when new_box is a number from 1 to 5.
        # If the answer for a card in the fifth box is guessed, then the card stays in the fifth box and doesn’t move.
        if new_box in BOXES:
            self.box = new_box
            self.save()

        return self

    def __str__(self):  # Used to control the string representation of the Card objects
        return self.question

