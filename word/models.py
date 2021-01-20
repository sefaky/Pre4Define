from django.db import models



class WordsDefining(models.Model):
    word = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    pegi = models.CharField(max_length=3)
    commentCount = models.CharField(max_length=11)
    downloads = models.CharField(max_length=12)
    ranking = models.CharField(max_length=4)

    def __str__(self):
        return self.word + "" + self.category