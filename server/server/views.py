from django.http import HttpResponse
from django.template import RequestContext, loader
# from google_calendar import *


def index(request):
	print "It worked !"
	template = loader.get_template('index.html')
	context = RequestContext(request, {})
	# event = get_next_event()
	return HttpResponse(template.render(context))