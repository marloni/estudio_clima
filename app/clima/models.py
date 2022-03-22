from django.db import models

# Create your models here.


class Datos(models.Model):
    year = models.IntegerField()
    seq = models.IntegerField()
    glide = models.IntegerField()
    disaster_group = models.CharField(max_length=50)
    disaster_subgroup = models.CharField(max_length=50)
    disaster_type = models.CharField(max_length=50)
    disaster_subtype = models.CharField(max_length=50)
    event_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    iso = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    continent = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    associated_dis = models.CharField(max_length=50)
    dis_mag_value = models.IntegerField()
    dis_mag_scale = models.CharField(max_length=50)
    start_data = models.CharField(max_length=50)
    end_data = models.CharField(max_length=50)
    total_deaths = models.IntegerField()
    no_injured = models.IntegerField()
    no_affected = models.IntegerField()
    no_homeless = models.IntegerField()
    total_affected = models.IntegerField()
    total_damages = models.IntegerField()

    def __str__(self):
        return str(self.year) + " " + str(self.seq)

    class Meta:
        verbose_name = "Datos"
        verbose_name_plural = "Datos"
