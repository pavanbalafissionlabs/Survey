from django.contrib import admin
from surveyapi.models import Survey


class SurveyAdmin(admin.ModelAdmin):
    list_display=['id','Name','Branch','Highercollagename','Can_you_writecode','TechinalSkills','yourworkDomain','yearofExp']


admin.site.register(Survey,SurveyAdmin)