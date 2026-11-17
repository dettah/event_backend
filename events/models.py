from django.db import models

# Create your models here.


class Event(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    venue = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    ticket_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    available_tickets = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title