from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
# Register your models here.
class items(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank= True, null=True)
    price = models.FloatField()
    image = models.ImageField( upload_to='item_images', blank= True, null=True)
    isSold = models.BooleanField(default=False)
    createdBy = models.ForeignKey(User, related_name='items',  on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    itemCategory = models.ForeignKey(category, related_name='items', on_delete=models.CASCADE)
    class Meta:
        # verbose_name = _("")
        verbose_name_plural = "items"

        def __str__(self):
            return self.Name

    # def get_absolute_url(self):
        # return reverse("_detail", kwargs={"pk": self.pk})
