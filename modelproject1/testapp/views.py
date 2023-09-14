import json

from django.shortcuts import render

from django.views.generic import View
from testapp.models import EmployeeRecord
import json
from django.http import HttpResponse
from django.core.serializers import serialize

from testapp.mixins import SerializeMixin,HttpResponseMixin


# Create your views here.


# class EmployeeDetailsCBV(View):
#
#     def get(self,request,id,*args,**kwargs):
#
#
#         # emp = EmployeeRecord.objects.get(id=1)
#         # emp = EmployeeRecord.objects.get(id=3)
#         emp = EmployeeRecord.objects.get(id=id)
# # we have to conver to details to distionary format
#         #in below API method
#         #call get method
#         emp_data = {
#             'eno':emp.eno,
#             'ename': emp.ename,
#             'esal': emp.esal,
#             'eaddr': emp.eaddr,
#
#         }
#
#         emp = EmployeeRecord.objects.get(id=id)
#         #json_data=serialize('json')
#         # convert distionary to JSON Object
#         json_data = serialize('json',[emp,],fields=('eno','ename','eaddr'))
#         return HttpResponse(json_data,content_type='application/json')

# we need to get the total records
#class EmployeeListCBV(View):
# class EmployeeListCBV(View):
#
#     def get(self,request,*args,**kwargs):
#         quesry_set = EmployeeRecord.objects.all()
#
# # convert distionary to JSON Object
# #        json_data = serialize('json', quesry_set)
#
#         #we want get the perticular fields
#         #json_data = serialize('json', quesry_set,fields=('eno','ename'))
#         json_data = serialize('json', quesry_set)#, fields=('eno', 'ename'))
#         #now we have to convert the JSON Object to Distionary
#         pdict = json.loads(json_data)
#         print(pdict)
#         final_list = []
#         for obj in pdict:
#             emp_data = obj['fields']
#             final_list.append(emp_data)
#         json_data = json.dumps(final_list)
#         return HttpResponse(json_data, content_type='application/json')
#





class EmployeeDetailsCBV(HttpResponseMixin,SerializeMixin,View):

    def get(self,request,id,*args,**kwargs):
        try:
            emp = EmployeeRecord.objects.get(id=id)
        except EmployeeRecord.DoesNotExist:
            json_data = json.dumps({'msg': 'The Requested resource not available'})

            #return HttpResponse(json_data, content_type='application/json',status=404)
            return self.render_to_http_response(json_data,status=404)
        else:
            json_data = self.serialze([emp,])
        #return HttpResponse(json_data,content_type='application/json',status=200)
            return self.render_to_http_response(json_data)#,status=200)










class EmployeeListCBV(HttpResponseMixin, SerializeMixin,View):

    def get(self,request,*args,**kwargs):
        quesry_set = EmployeeRecord.objects.all()
        json_data = self.serialze(quesry_set)
        return HttpResponse(json_data, content_type='application/json')

