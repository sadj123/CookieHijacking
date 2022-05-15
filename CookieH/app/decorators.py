from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Cookie
def brow():
    def decorator(viewfunc):
        def wrapperfunc(request, *args, **kwargs):
            data= Cookie.objects.get(user= request.user.id)
            if data.coo == request.META['HTTP_USER_AGENT']:
                return viewfunc(request, *args, **kwargs)
            else:
                return HttpResponse("No estas autorizado")
        return wrapperfunc
    return decorator