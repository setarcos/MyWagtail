from django.http import HttpResponseRedirect

def auth(request):
    print(request.GET.get('token',''))
    return HttpResponseRedirect('/')
