from django.http import HttpResponse


def index(request):
	return HttpResponse('index')


def hh():
	print('kkkkk')