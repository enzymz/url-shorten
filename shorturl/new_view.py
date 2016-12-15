from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from shorturl.models import UserAgent
from shorturl.serializers import AgentSerializers

class JSONResponse(HttpResponse):
    '''

    '''
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def agent_list(request):
    if request.method == 'GET':
        useragent = UserAgent.objects.all()
        agentserializer = AgentSerializers(shorturl)
        return JSONResponse(agentserializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        agentserializer = AgentSerializers(data=data)
        if agentserializer.is_valid():
            agentserializer.save()
            return JSONResponse(agentserializer.data, status=201)
        return JSONResponse(agentserializer.errors, status=400)

@csrf_exempt
def agent_detail(request, pk):
    try:
        useragent = UserAgent.objects.get(pk=pk)
    except UserAgent.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        agentserializer = AgentSerializers(useragent)
        return JSONResponse(agentserializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        agentserializer = AgentSerializers(useragent, data=data)
