from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ESPObject
from datetime import datetime, timedelta, timezone


# Create your views here.
def set_aps(request, unique_id):
    # try:
    esp = ESPObject.objects.get(unique_id=unique_id)
    aps = esp.last_ips
    if (datetime.now(timezone.utc) - esp.last_location_time) > timedelta(seconds=100):
        aps = {}
    aps[request.GET['SSID'] + " " + request.GET['BSSID']] = int(request.GET['RSSI'])
    esp.last_ips = aps
    esp.last_location_time = datetime.now(timezone.utc)
    esp.save()
    return JsonResponse({'status': 'ok'})


# except:
#     return JsonResponse({'status': 'error'})


def view_aps(request, unique_id):
    try:
        esp = ESPObject.objects.get(unique_id=unique_id)
        aps = esp.last_ips
        return JsonResponse(aps)
    except:
        return JsonResponse({'status': 'error'})


def view_aps_gui(request, unique_id):
    esp = ESPObject.objects.get(unique_id=unique_id)
    aps = esp.last_ips
    arr = []
    for key in aps:
        temp = []
        temp = temp + key.split(" ")
        temp.append(aps[key])
        arr.append(temp)
    print(arr)
    return render(request, 'view_aps.html', {"values": arr, "time": esp.last_location_time})
    # except:
    #     return JsonResponse({'status': 'error'})
