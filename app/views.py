from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
from django.views.generic import View,TemplateView,FormView
# Create your views here.
class templatedatarender(TemplateView):
    template_name='templatedatarender.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='mounika'
        return context


class temp_insert(TemplateView):
    template_name='temp_insert.html'
    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        SFO=studentForm()
        ECDO['SFO']=SFO
        return ECDO

    def post(self,request):
        SFD=studentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('data is inserted')

class studentformview(FormView):
    template_name='studentformview.html'
    form_class=studentForm
    def form_valid(self,form):
        form.save()
        return HttpResponse('data is insert')

        
