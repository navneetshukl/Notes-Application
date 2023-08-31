from django.http import JsonResponse
from django.shortcuts import render

import utils

def Home(request):
    collection=utils.Connect_To_DB()
    post={"name":"Ram","email":"ram.com","address":"Ayodhya"}

    collection.insert_one(post)
    return JsonResponse({'Message': "Connected to Database"})
