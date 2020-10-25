from django.contrib import admin

from .models import Question , Destination , Choice, Oxes


admin.site.register( Question)
admin.site.register(Destination)
admin.site.register( Choice)
admin.site.register( Oxes)
