from django.shortcuts import render
from django.http import HttpResponse
import sys
from getRefrain.signalProcess import spectrogram


def index(request):
    return render(request,'index.html')

def getRefrain(request):
    filepath = request.POST['filepath']
    filename = request.POST['filename']
    
    st,ed = spectrogram.process_audio(filename = filename ,path= filepath)
    return HttpResponse(str(st)+str(ed))
# Create your views here.
