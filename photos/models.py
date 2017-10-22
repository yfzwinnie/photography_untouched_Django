from django.db import models

categories= (
    ('G', 'Gallery'),
    ('N', 'Nature'),
    ('C', 'City'),
    ('P', 'Portraits'),
    ('A', 'Animals')
)

class Photo(models.Model):
    title = models.CharField(max_length=200)
    width = models.IntegerField(default=400)
    height = models.IntegerField(default=400)
    image = models.ImageField(null=False, blank=False, width_field="width", height_field="height")
    description = models.CharField(max_length=400, default='F-stop | Shutter Speed | ISO')
    category = models.CharField(max_length=1, default='', blank=False, choices=categories)
    location = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=200, default='')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return '%s %s' % (self.title, self.category)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["timestamp"]
