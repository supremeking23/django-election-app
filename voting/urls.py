from django.urls import path

from . import views

#app_name = 'voting'
urlpatterns = [
	path('',views.home, name="home"),
	path('candidate_list/',views.candidate_list,name="candidate_list"),
	path('vote_president/',views.vote_president,name="vote_president"),
	path('president/',views.president,name="president"),
	path('vice-president/',views.vice_president,name="vice_president"),
	path('vote_vice_president/',views.vote_vice_president,name="vote_vice_president"),
	path('senators/',views.senators,name="senators"),
	path('vote_senators/',views.vote_senators,name="vote_senators"),
	
]