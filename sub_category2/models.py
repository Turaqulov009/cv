from django.db import models

# Create your models here.

class SubCategory2(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey('Category2', on_delete=models.CASCADE, related_name='subcategories')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
