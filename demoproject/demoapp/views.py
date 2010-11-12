from django.shortcuts import render_to_response

def homepage(request, **kwargs):
    return render_to_response('homepage.html')
