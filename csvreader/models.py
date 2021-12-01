from django.db import models


class CSVdata(models.Model):
    filename = models.CharField(max_length=50, unique=True)
    dataresult = models.DecimalField(max_digits=20, decimal_places=16, blank=True, null=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return str(self.filename)




