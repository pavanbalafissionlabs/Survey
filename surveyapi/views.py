from django.shortcuts import render
from django.views.generic import View
from django.core.serializers import serialize
from surveyapi.utils import is_json
from django.http import HttpResponse
import json
from surveyapi.models import Survey
from surveyapi.forms import SurveyForm


class Surveyall(View):
    def get_object_by_id(self, id):

        try:
            suv = Survey.objects.get(id=id)
        except Survey.DoesNotExist:
            suv = None
        return suv
    

    def get(self,request,id):
        suv = self.get_object_by_id(id)
        if suv is None:
            json_data = json.dumps(
                {'msg': 'no match is found or record is not in db'})
            return HttpResponse(json_data, content_type='application/json', status=400)
        
        json_dat = serialize('json', [suv])
        p_dict = json.loads(json_dat)
        finallist = []
        for obj in p_dict:
            emp_data = obj['fields']
            finallist.append(emp_data)
        json_dat = json.dumps(finallist)

        return HttpResponse(json_dat, content_type='application/json')

    
    def put(self, request, id):
        suv = self.get_object_by_id(id)
        if suv is None:
            json_dat = json.dumps(
                {'msg': 'the id did not  match recored not possible to update'})
            return HttpResponse(json_dat, content_type='application/json')

        data = request.body
        print(data)
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps(
                {'msg': 'please send the valid json data only'})
            return HttpResponse(json_data, content_type='application/json', status=400)
        provided_data = json.loads(data)
        orginal_data = {

            'Name':suv.Name,
            'Branch':suv.Branch,
            'Highercollagename':suv.Highercollagename,
            'Can_you_writecode':suv.Can_you_writecode,
            'TechinalSkills':suv.TechinalSkills,
            'yourworkDomain':suv.yourworkDomain,
            'yearofExp':suv.yearofExp,
            
        }
        orginal_data.update(provided_data)
        form = SurveyForm(orginal_data, instance=suv)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps(
                {'msg': 'survey data is updated'})
            return HttpResponse(json_data, content_type='application/json')
        if form.errors:
            json_data = json.dumps(form.errors)
            return HttpResponse(json_data, content_type='application/json', status=400)


    def delete(self, request, id ):
        suv = self.get_object_by_id(id)
        if suv is None:
            json_dat = json.dumps(
                {'msg': 'To perform deleting id should be present in db'})
            return HttpResponse(json_dat, content_type='application/json')
        status, deleted_item = suv.delete()
        print(status, deleted_item)
       
        if status == 1:
            json_data = json.dumps(
                {'msg': 'Data is deleted from db'})
            return HttpResponse(json_data, content_type='application/json')
        




class Survey_all(View):
    def get(self, request):
        sr = Survey.objects.all()
        json_dat = serialize('json', sr)
        p_dict = json.loads(json_dat)
        finallist = []
        for obj in p_dict:
            suv_data = obj['fields']
            finallist.append(suv_data)
        json_dat = json.dumps(finallist)

        return HttpResponse(json_dat, content_type='application/json')


    def post(self, request):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps(
                {'msg': 'please send the valid json data  only check the format in schema'})
            return HttpResponse(json_data, content_type='application/json', status=400)
        json_data =json.loads(data)
        form =SurveyForm(json_data)  

        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps(
                {'msg': 'resource data is created succesfully'})
            return HttpResponse(json_data, content_type='application/json',status=201)
        if form.errors:
            json_data = json.dumps(form.errors)
            return HttpResponse(json_data, content_type='application/json', status=400)
