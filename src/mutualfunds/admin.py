from django.contrib import admin

# Register your models here.
from .models import Folio, MutualFundTransaction


admin.site.register(Folio)
admin.site.register(MutualFundTransaction)