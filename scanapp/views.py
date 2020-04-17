from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def demo(request):
    name=request.POST.get('name')
    passw=request.POST.get("pass")
    
    
    print(name)
    print(passw)
    data = {
        'msg': "success"
    }
    return JsonResponse(data)

# Create your views here.
