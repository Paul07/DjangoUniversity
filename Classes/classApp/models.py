from django.db import models

# Create your models here.
class UniversityClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(null=True, blank=True, default=None)

# Model manager
    object = models.Manager()

    #  displays object output in string form
    def __str__(self):
        #  returns title and instructor name input value
        #  field as a tuple to display in browser instead of default titles
        display_course = '{0.title}: {0.instructor_name}'
        return display_course.format(self)

    #  removes the "s" that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Classes"
