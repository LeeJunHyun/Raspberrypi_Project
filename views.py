from django.shortcuts import render,get_object_or_404
from .models import Dancer,Program,Timetable,Style,Main
import RPi.GPIO as GPIO
import time
from .DoorLock import OpenDoor

def home(request):
    main = Main.objects.all()[0]
    return render(request,'homepage/home.html',{
        'main':main,
        })

def rent(request):
 	return render(request,'homepage/rent.html')


def dancers(request):
    opendoor = OpenDoor(GPIO,18)
    opendoor.open()
    qs = Dancer.objects.all()
    return render(request,'homepage/dancers.html', {
        'dancer_list': qs
         })


def program(request):
    style_list = Style.objects.all()
    timetable = Timetable.objects.all()[0]
	
    return render(request,'homepage/program.html',{
    	'timetable':timetable,
    	'style_list':style_list,
    	})

def dancer_detail(request,id):
     dancer = get_object_or_404(Dancer,id=id)
     return render(request,'homepage/dancer_detail.html', {
     	'dancer': dancer,
     	})


def program_detail(request,id):
    program = get_object_or_404(Program,id=id)
    return render(request,'homepage/program_detail.html',{
 		'program':program,
 		})
