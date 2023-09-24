from django.contrib import admin
from vege.models import *
admin.site.register(Recepe)
admin.site.register(student)
admin.site.register(studentId)
admin.site.register(Department)
admin.site.register(Subject)

class modelsubjectAdmin(admin.ModelAdmin):
    list_display=['students','subject','marks']

admin.site.register(Subject_Marks,modelsubjectAdmin)
