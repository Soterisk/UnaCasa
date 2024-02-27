from django.db import models

class ResaleThings(models.Model):
    user = models.ForeignKey('UserApp.CustomUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Item for Resale: {self.title} by User: {self.user.username}'

class ResaleImage(models.Model):
    image = models.ImageField(upload_to='resale_images/')
    item = models.ForeignKey('ResaleThings', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'Image for Item: {self.item.id}'

class ResaleComment(models.Model):
    comment = models.TextField()
    item = models.ForeignKey('ResaleThings', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('UserApp.CustomUser', on_delete=models.CASCADE)  # User who made the comment

    def __str__(self):
        return f'Comment for Item: {self.item.id} by User: {self.user.username}'