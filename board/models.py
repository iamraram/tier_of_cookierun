from django.db import models


class Board(models.Model):
    subject = models.CharField(max_length=128)
    description = models.TextField()
    create_date = models.DateTimeField()
    comment = models.TextField()
    view = models.IntegerField()
    category = models.IntegerField()
    def __str__(self):
        return self.subject
