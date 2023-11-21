from django.http import HttpResponse
from django.template import loader
from .models import Login

def main(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def idiot(request):
  mymembers = Login.objects.all().values()
  template = loader.get_template("idiot.html")
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))