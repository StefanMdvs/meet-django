from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    # after this, create the table in db using command python3 manage.py makemigrations
    # first run it with --dry-run to check the changes we want to make
    # manage.py showmigrations will show unaplied migrations
    # to apply the migrations run python3 manage.py migrate --plan first then
    # if it looks good procede with migrate

    def __str__(self):
        return self.name
        # this method overwrites the model method and returns the name we give to our items as 
        # opposed to generig name: Object