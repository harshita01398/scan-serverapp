from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

hotspot_name = ""
password = ""
bike_ip = ""
android_ip = ""

status = True
request_valid = False

@csrf_exempt
def receive(request):

    global hotspot_name, password, bike_ip, android_ip, request_valid

    hotspot_name = request.POST.get('name')
    password = request.POST.get('pass')
    bike_ip = request.POST.get('bikeIP')
    android_ip = request.POST.get('androidIP')

    if hotspot_name==None or password==None or bike_ip==None or android_ip==None:

        response = {
            'status' : "false",
            'message' : "Invalid request. Please check for missing parameters."
        }

        return JsonResponse(response, status = 500)
    
    elif hotspot_name=="" or bike_ip=="" or android_ip=="":

        response = {
            'status' : "false",
            'message' : "Error. Please check value of hotspot name and/or IP address."
        }

        return JsonResponse(response, status = 500)
    
    else:

        request_valid = True

        print(hotspot_name)
        print(password)
        print(bike_ip)
        print(android_ip)
        
        response = {
            'message' : "Request received."
        }
        return JsonResponse(response)

def connect(request):

    global hotspot_name, password, bike_ip, android_ip, request_valid

    current_ip = request.GET.get('bikeIP')

    if not request_valid or bike_ip!=current_ip:
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
        'pass' : password,
        'androidIP' : android_ip
        }

        request_valid = False

        return JsonResponse(response)

def bike_status(request):

    global android_ip, status

    android_ip = request.GET.get('androidIP')
    status = False

    response = {
            'message' : "Request received."
        }
    return JsonResponse(response)


def android_status(request):

    global android_ip, status

    current_ip = request.GET.get('androidIP')
    print("android checking status")

    if status or current_ip!=android_ip:
        print("No status")

        response = {
            'status' : "false",
            'message' : "Error. Can't get status"
        }
        return JsonResponse(response, status=500)

    else:
        print("Bike can't connect.")
        response = {
            'message' : "Bike Can't connect"
        }
        status = True
        return JsonResponse(response)

