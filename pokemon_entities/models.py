from django.db import models  # noqa F401


# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="pokemon_images", blank=True, null=True)

    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()  # широта
    lon = models.FloatField()  # долгота
    appear_at = models.DateTimeField()
    disappear_at = models.DateTimeField()
