from django.http import HttpResponse
from django.template import RequestContext, loader
import urllib2
import json


#api_url = "https://api.particle.io"
api_url = "http://postcatcher.in/catchers/5561126b111b370300000250"

data = {'test': 'fuck'}
url = api_url
#brew_url = "/v1/devices/54ff65066672524826511967/brew"




"""A quickstart example showing usage of the Google Calendar API."""
from datetime import datetime
import os

from apiclient.discovery import build
from httplib2 import Http
import oauth2client
from oauth2client import client
from oauth2client import tools


def index(request):
	print "It worked !"
	template = loader.get_template('login.html')
	context = RequestContext(request, {})
	#event = get_next_event()
	return HttpResponse(template.render(context))

def brew(request):
    """
    At this url, we issue a RPC to the spark brew function
    """
    template = loader.get_template('brew.html')
    context = RequestContext(request, {})
    # create my own request to be sent to Particle
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request2 = urllib2.Request(url , data=json.dumps(data))
    request2.add_header("Authorization", "4e11cb75ca89569de04867ca8e765cdc797e48a3") #Header, Value
    opener.open(request2)

    return HttpResponse(template.render(context))

