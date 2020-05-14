from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

hotspot_name = ""
password = ""
scanned_ip = ""

@csrf_exempt
def receive(request):

    global hotspot_name, password, scanned_ip

    hotspot_name = request.POST.get('name')
    password = request.POST.get('pass')
    scanned_ip = request.POST.get('ip')

    if str(hotspot_name) == "" or str(scanned_ip) == "":

        response = {
            'status' : "false",
            'message' : "Invalid request. Please check."
        }

        return JsonResponse(response, status = 500)
    
    else:

        print(hotspot_name)
        print(password)
        print(scanned_ip)
        
        response = {
            'message' : "Request received."
        }
        return JsonResponse(response)

def connect(request):

    global hotspot_name, password, scanned_ip

    current_ip = request.GET.get('my_ip')

    if scanned_ip == "" or str(scanned_ip) != str(current_ip):
        print("Waiting for device to connect.")

        response = {
            'status' : "false",
            'message' : "No requesting device."
        }

        return JsonResponse(response, status = 500)
    
    else:
        print("IP matched!")

        response = {
        'hotspot_name' : hotspot_name,
        'pass' : password
        }

        hotspot_name = ""
        password = ""
        scanned_ip = ""

        return JsonResponse(response)

