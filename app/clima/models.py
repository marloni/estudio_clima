from django.db import models

# Create your models here.


class Datos(models.Model):
    year = models.IntegerField(null=True, blank=True)
    seq = models.IntegerField(null=True, blank=True)
    glide = models.IntegerField(null=True, blank=True)
    disaster_group = models.CharField(max_length=50, null=True, blank=True)
    disaster_subgroup = models.CharField(max_length=50, null=True, blank=True)
    disaster_type = models.CharField(max_length=50, null=True, blank=True)
    disaster_subtype = models.CharField(max_length=50, null=True, blank=True)
    event_name = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    iso = models.CharField(max_length=50, null=True, blank=True)
    region = models.CharField(max_length=50, null=True, blank=True)
    continent = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    associated_dis = models.CharField(max_length=50, null=True, blank=True)
    dis_mag_value = models.IntegerField(null=True, blank=True)
    dis_mag_scale = models.CharField(max_length=50, null=True, blank=True)
    start_data = models.CharField(max_length=50, null=True, blank=True)
    end_data = models.CharField(max_length=50, null=True, blank=True)
    total_deaths = models.IntegerField(null=True, blank=True)
    no_injured = models.IntegerField(null=True, blank=True)
    no_affected = models.IntegerField(null=True, blank=True)
    no_homeless = models.IntegerField(null=True, blank=True)
    total_affected = models.IntegerField(null=True, blank=True)
    total_damages = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.year) + " " + str(self.seq)

    class Meta:
        verbose_name = "Datos"
        verbose_name_plural = "Datos"
