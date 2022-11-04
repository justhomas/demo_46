from django.db import models


class IouUser(models.Model):
    name = models.CharField(max_length=30,unique=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

class Ledger(models.Model):
    user = models.ForeignKey(IouUser, on_delete=models.CASCADE,related_name="owes")
    owes = models.ForeignKey(IouUser, on_delete=models.CASCADE,related_name="owed")
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    expiration = models.DateTimeField()
    def __str__(self):
        return f"{self.user.name} owes {self.owes.name} Rs {self.amount}"
