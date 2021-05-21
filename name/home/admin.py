from django.contrib import admin
from home.models import formed,academy,stu_info,student_add,certi

# Register your models here.

admin.site.register(formed)
admin.site.register(certi)
admin.site.register(stu_info)

@admin.register(student_add)
class Adminstudent_add(admin.ModelAdmin):
    list_display = ('id','name','number')

@admin.register(academy)
class Adminacademy(admin.ModelAdmin):
    list_display=('id','cgpa','percentage','subject1','subject2','subject3','subject4','subject5','kt')