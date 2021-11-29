from django.db import models


class CSVdata(models.Model):
    filename = models.CharField(max_length=50)
    dataresult = models.DecimalField(max_digits=20, decimal_places=16)

    def __str__(self):
        return str(self.filename)




