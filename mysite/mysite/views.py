from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworld(request):
  return HttpResponse('Hello World!')

class HelloWorld(TemplateView):
  template_name = 'hello.html' # htmlファイルの指定(別途作成する必要あり)