from django.contrib import admin
from testapp.models import EmployeeRecord
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','eno','ename','esal','eadd']



admin.site.register(EmployeeRecord)
