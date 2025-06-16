from django.shortcuts import render
from django.http import HttpResponse
from google import genai
import time

# Create your views here.
client=genai.Client(api_key="YOUR_API_KEY_HERE")
chat=client.chats.create(model="gemini-2.0-flash")

def index(request):
    x = "Explain Like I'm Five"
    return render(request, 'index.html', {'para': x})

def result(request):
    text=request.GET['prompt']
    if text!='':
        response=chat.send_message(text+"\n Explain this text like im a five year old, in a big paragraph please. with proper indentation \n")
        return render(request, 'result.html', {'response':response.text})

