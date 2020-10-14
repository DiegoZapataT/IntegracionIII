from djongo import models

class Posts(models.Model):
    _id = models.ObjectIdField()
    post_title = models.CharField(max_length = 255)
    post_description = models.TextField()
    comment = models.JSONField()
    tags = models.JSONField()
    objects = models.DjongoManager()

class Prueba1(models.Model):
    _id = models.ObjectIdField()
    dias = models.JSONField()
    casos = models.JSONField()
    objects = models.DjongoManager()