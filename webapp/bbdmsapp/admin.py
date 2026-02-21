from django.contrib import admin
from . import models

admin.site.register(models.CustomUser)
admin.site.register(models.Bloodgroup)
admin.site.register(models.DonorReg)
admin.site.register(models.BloodRequest)
admin.site.register(models.Contact)
