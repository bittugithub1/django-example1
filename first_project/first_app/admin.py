from django.contrib import admin

from first_app.models import AccessRecord,Topic,Webpage

admin.site.register(Webpage)
admin.site.register(Topic)
admin.site.register(AccessRecord)


# Register your models here.
