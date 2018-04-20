from django.db import models

class Text(models.Model):
  body = models.CharField(max_length=200, blank=True)

  def __str__(self):
    return self.body


class Blog(models.Model):
  body = models.ForeignKey(Text, on_delete=models.CASCADE, default=1)
  title = models.CharField(max_length=200, blank=True)
  created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

  def __str__(self):
    return self.title