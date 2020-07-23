from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, db_index=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    suburb = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(null=False, blank=False, db_index=True)
    phone = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        unique_together = [["name"]]
