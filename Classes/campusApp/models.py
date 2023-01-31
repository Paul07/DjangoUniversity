from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    Campus_name = models.CharField(max_length=50, default="", blank=True, null=False)
    State = models.CharField(max_length=2, default="", blank=True, null=False)
    Campus_id = models.IntegerField(default="", blank=True, null=False)

    object = models.Manager()

    def __str__(self):
        display_campus = '{0.Campus_name}' '{0.State}'
        return display_campus.format(self)

    class Meta:
        verbose_name_plural = "University Campuses"
