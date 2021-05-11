from django.contrib import admin
from . models import  PatientVisit, Patient, PatientBill
from . models import   Appointment, HealthHistory

# Register your models here.


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "phone", "email", "date_recorded")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "description", "date_requested", "approved")

@admin.register(PatientVisit)
class PatientVisitAdmin(admin.ModelAdmin):
    list_display = ("patient", "visit_date")

@admin.register(PatientBill)
class PatientBillAdmin(admin.ModelAdmin):
    list_display = ("patient", "treatment_date", "amount", "payment_date")


@admin.register(HealthHistory)
class HealthHistoryAdmin(admin.ModelAdmin):
    list_display = ("patient", "history")

admin.site.site_title = "CLINIC MANAGEMENT SYSTEM"
admin.site.site_header = "CLINIC MANAGEMENT SYSTEM"






