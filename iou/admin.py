from django.contrib import admin
from .models import Ledger,IouUser
# Register your models here.

admin.site.register(Ledger)
admin.site.register(IouUser)