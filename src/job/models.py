from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.


############################
# Job Type Chocies

JOB_TYPE = (
    ('Part Time', 'Part Time'),
    ('Full Time', 'Full Time'),

)

##########################
# Image Upload


def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "jobs/%s.%s" % (instance.title, extension)

##################################################################
# Table Jobs


class job(models.Model):
    owner = models.ForeignKey(
        User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    salary = models.IntegerField(default=0)
    vacancy = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
    published_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(job, self).save(*args, **kwargs)

    def __str__(self):

        return self.title

#####################################################################
# Table Category


class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#####################################################################
# Table Form ApplyForm


class apply(models.Model):
    Job = models.ForeignKey(
        job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField('apply/')
    cove_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
