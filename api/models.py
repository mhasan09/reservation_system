from django.db import models
import random

class VACANCY_LIMIT(models.Model):
    DATE = models.DateField()
    LIMIT = models.IntegerField()

    def __str__(self):
        return "%s" % (self.DATE)

class RESERVATION(models.Model):
    VACANT = 0
    RESERVED = 1
    STATUS = (
        (VACANT, "Vacant"),
        (RESERVED, "Reserved"),
    )
    # START_DATE = models.DateField()
    START_DATE = models.ForeignKey(VACANCY_LIMIT, on_delete=models.CASCADE)
    END_DATE = models.DateField()
    STATUS = models.SmallIntegerField(choices=STATUS, default=VACANT)
    RESERVED_BY = models.TextField("RESERVED_BY", null=True, blank=True)
    TOTAL_AMOUNT = models.CharField(max_length=256,null=True, blank=True)


    def __str__(self):
        # return "(%s to %s)" % (self.START_DATE.strftime("%Y/%m/%d %H:%S"), self.END_DATE.strftime("%Y/%m/%d %H:%S"))
        return "(%s to %s)" % (self.START_DATE.DATE.strftime("%Y/%m/%d %H:%S"), self.END_DATE.strftime("%Y/%m/%d %H:%S"))



class VACANCY(models.Model):

    RESERVATION = models.ForeignKey(RESERVATION,  on_delete=models.CASCADE)


    def __str__(self):
        return "%s" % (self.RESERVATION.RESERVED_BY)


