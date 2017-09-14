from django.db import models
from django.utils import timezone


class Post(models.Model):  #models.Model significa che il Post è un modello Django, quindi Django sa che dovrebbe essere salvato nel database
    author = models.ForeignKey('auth.User')			#models.ForeignKey= link a un altro modello
    title = models.CharField(max_length=200)		#models.CharField = testo con un numero limitato di lettere
    text = models.TextField()						#models.TextField = testo senza un limite
    created_date = models.DateTimeField(			#models.DateTimeField = data ed l'ora
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title