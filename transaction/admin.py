from django.contrib import admin

from transaction.models import *

admin.site.register(TA_transaction)
admin.site.register(TA_transaction_processed)
admin.site.register(Statistics)