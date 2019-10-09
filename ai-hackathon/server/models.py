from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


class Education(models.Model):
    user = models.ForeignKey("User", related_name="edu", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50, default="Bachelor of Life Science")
    eduLevel = models.IntegerField(default=3)
    reqLevel = models.IntegerField(default=3)


class Skills(models.Model):
    user = models.ForeignKey("User", related_name="skills", on_delete=models.DO_NOTHING)
    skills = models.TextField()
