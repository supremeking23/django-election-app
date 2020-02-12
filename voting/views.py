from django.shortcuts import render

from .models import Person, Position

# Create your views here.


def home(request):
	return render(request,'voting/home.html')


def candidate_list(request):
	position_list = Position.objects
	candidate_list = Person.objects
	return render(request,'voting/candidate_list.html',{'position_list': position_list,'candidate_list':candidate_list })


def vote_president(request):

	if request.method == 'POST':

		selected_candidate = Person.objects.get(pk=request.POST['president'])
		message = "Your vote has been saved"
		selected_candidate.votes += 1
		selected_candidate.save()
		return render(request,'voting/home.html',{'message':message})

	else:
		president_list = Person.objects.filter(title=1)
		return render(request,'voting/president.html',{'president_list':president_list})

def president(request):
	#filter
	president_list = Person.objects.filter(title=1)
	return render(request,'voting/president.html',{'president_list':president_list})







def vice_president(request):
	vice_president_list = Person.objects.filter(title=2)
	return render(request,'voting/vice_president.html',{'vice_president_list':vice_president_list})


def vote_vice_president(request):


	if request.method == 'POST':

		selected_candidate = Person.objects.get(pk=request.POST['vice_president'])
		message = "Your vote has been saved"
		selected_candidate.votes += 1
		selected_candidate.save()
		return render(request,'voting/home.html',{'message':message})

	else:
		president_list = Person.objects.filter(title=1)
		return render(request,'voting/vote_vice_president.html',{'vice_president':vice_president})



def senators(request):
	senator_list = Person.objects.filter(title=3)
	return render(request,'voting/senators.html',{'senator_list':senator_list})


def vote_senators(request):

	if request.method == 'POST': 
		senators = request.POST.getlist('senator')
		message = "Your vote has been saved %s"%(senators)
		for senator in senators:
			selected_candidate = Person.objects.get(pk=senator)
			selected_candidate.votes +=1
			selected_candidate.save()
		return render(request,'voting/home.html',{'message':message,'senators':senators})
