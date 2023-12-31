from django.db import models

# allows you to specify text form of output
# from django.utils.translation import gettext_lazy as _

# Allows you to work with arrays in postgres
# from django.contrib.postgres import fields as PostgresFields


class PersonDetail(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name} - {self.userid}"
