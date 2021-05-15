from django.contrib import admin
from home.models import formed,academy,stu_info,student_add

# Register your models here.

admin.site.register(formed)
admin.site.register(academy)
admin.site.register(stu_info)

@admin.register(student_add)
class Adminstudent_add(admin.ModelAdmin):
    list_display = ('id','name','number')