from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ipware import get_client_ip

name = ""
passw = ""
ip = ""

@csrf_exempt
def demo(request):

    global name, passw, ip

    name = request.POST.get('name')
    passw = request.POST.get('pass')
    ip = request.POST.get('ip')
    
    
    print(name)
    print(passw)
    print(ip)
    
    data = {
        'msg': "success"
    }
    return JsonResponse(data)

# def connect(request):

#     global name, passw, ip

#     if ip == "":
#         return JsonResponse(None)
    
#     else:
#         data = {
#         'name': name,
#         'pass': passw
#         }
#         name = ""
#         passw = ""
#         ip = ""

#         return JsonResponse(data)

def check_ip(request):
    client_ip, is_routable = get_client_ip(request)
    if client_ip is None:
        print("Unable to get the client's IP address")
    else:
        # We got the client's IP address
        if is_routable:
            print("Routable :  ")
            print(client_ip)
        else:
            print(client_ip)

    data = {
        'msg': "success"
    }
    return JsonResponse(data)



    



# Create your views here.
