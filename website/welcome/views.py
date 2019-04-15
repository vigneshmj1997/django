from django.shortcuts import render

# Create your views here.
def display(req,username,festival):
	print(username)
	return render(req,"home.html",{"username":username,"festival":festival})