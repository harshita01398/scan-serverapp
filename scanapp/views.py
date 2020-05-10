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

def connect(request):

    global name, passw, ip
    print(ip)

    if ip == "":
        print("no ip")
        return JsonResponse(None)
    
    else:
        data = {
        'name': name,
        'pass': passw
        }
        name = ""
        passw = ""
        ip = ""

        return JsonResponse(data)

def check_ip(request):
    client_ip, is_routable= get_client_ip(request)
    if client_ip is None:
        print("Unable to get the client's IP address")
    else:

        # We got the client's IP address
        # if is_routable:
        #     print("Routable :  " + str(client_ip))
        #     print(client_ip)
        # else:
        #     print(client_ip)

        data = {
            'ip': client_ip,
            # 'realip': rip
        }
        return JsonResponse(data)

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        print("returning FORWARDED_FOR")
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        print("returning REAL_IP")
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        print("returning REMOTE_ADDR")
        ip = request.META.get('REMOTE_ADDR')
    data = {
        'ip': ip
            # 'realip': rip
    }
    return JsonResponse(data)


    



# Create your views here.
