from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt

from django.views.generic import View


class ApiView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ApiView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        print(request.POST['message'])
        return HttpResponse('')
