from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

hotspot_name = ""
password = ""
scanned_ip = ""
request_valid = False

@csrf_exempt
def receive(request):

    global hotspot_name, password, scanned_ip, request_valid

    hotspot_name = request.POST.get('name')
    password = request.POST.get('pass')
    scanned_ip = request.POST.get('ip')

    if hotspot_name == None or password == None or scanned_ip == None:

        response = {
            'status' : "false",
            'message' : "Invalid request. Please check for missing parameters."
        }

        return JsonResponse(response, status = 500)
    
    elif hotspot_name == "" or scanned_ip == "" :

        response = {
            'status' : "false",
            'message' : "Invalid request. Please check value of hotspot name and/or IP address."
        }

        return JsonResponse(response, status = 500)
    
    else:

        request_valid = True

        print(hotspot_name)
        print(password)
        print(scanned_ip)
        
        response = {
            'message' : "Request received."
        }
        return JsonResponse(response)

def connect(request):

    global hotspot_name, password, scanned_ip, request_valid

    current_ip = request.GET.get('my_ip')

    if not request_valid or scanned_ip != current_ip:
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

        request_valid = False

        return JsonResponse(response)

