from django.db import models

class Note(models.Model):
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.content[:50]

    class Meta:
        ordering = ['-updated_on']