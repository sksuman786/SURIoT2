


from django.http import HttpResponse
from django.shortcuts import render

import requests as rq

def home(request):


	return HttpResponse('Hello SUR TECH')



def details(request):

	d = {
			'title':'Signup',
			'head':'Student Information'
	}


	n = request.POST.get('name')
	e = request.POST.get('email')
	p = request.POST.get('ph')

	print(n,e,p)
	# auth()
	# insert(n,e,p)



	return render(request,'index.html',d)



def auth():

	payload = {
	        'email':'sksuman13@gmail.com',
	        'password':'1234567',
	        'returnSecureToken':True
	}

	key = 'AIzaSyAekjavxkvaskuSDqmjW1SKKRGlXUf9jYkMVuKOrGe6s'
	api = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key='+key

	response = rq.post(api,json=payload).text

	print(response)



def insert(name,email,ph):

	data = {	"name" : name,
	            "mail" : email,
	            "Mob"  : ph
	        }
	api = 'https://sur-iot-6kuycxk/BIUUXJVH-default-rtdb.firebaseio.com/info3.json'

	#response = rq.post(api,json=data).text
	response = rq.put(api,json=data).text

	print(response)