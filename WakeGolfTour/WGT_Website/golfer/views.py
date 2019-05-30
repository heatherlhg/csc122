from django.shortcuts import render

# Create your views here.
from django.views import generic
from golfer.models import Golfer, TournGolfer, GolferRoundScores
from tournament.models import Tournament
from golf_course.models import GolfCourse, Hole

# First view:
# List golfer from home page hyperlinks navigation panel

class GolferListView(generic.ListView):
    model = Golfer
    template_name = 'golfer/golfer_list.html'
    context_object_name = 'golfers'
    
# Second view:
# Detail view from list view on home page

class GolferDetailView(generic.DetailView):
    model = Golfer
    template_name = 'golfer/golfer_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super (GolferDetailView, self).get_context_data (**kwargs)
        
        golfer = self.get_object()
        
        context['golfer'] = golfer
        context['scores'] = GolferRoundScores.getTournScoresByGolfer(golfer.golfer_id)
        
        return context
class GolferRoundScoresView(generic.DetailView):
    # since a tourn_golfer id is used as the primary key (pk)
    # specify that by assigning the model to be TournGolfer
    model = TournGolfer
    # assign the template name
    template_name ='golfer/golfer_round_scores.html'
    
    # Just like in the views from Project 2B, override the get_context_data method:
    
    def get_context_data(self, **kwargs):
        # this is how to get the context dictionary
        context = super(GolferRoundScoresView, self).get_context_data(**kwargs)
        
        # we specified the queryset to be a TournGolfer set, so the 
        # object will be a tourn_golfer_set
        tourn_golfer = self.get_object()
        
        # we are passed in the tourn_golfer id in the 'pk' argument
        # pull it out into a local variable
        tg_id = self.kwargs.get('pk')
        
        # Retreive a queryset list of the GolferRoundScores objects
        # from the database, filtered to only get the 
        # GolferRoundScores objects, whose TournGolfer id is equal
        # to the TournGolfer id we retrieved from the arguments
        # above (grs_tourn_goler_id = tg_id).
        # Call the objects.filter function to retrieve the list.
        
        scores = GolferRoundScores.objects.filter(grs_tourn_golfer_id = tg_id)
        
        # we also want the tournament, golf_course and holes
        # Get the Tournament object, (tournament), whose primary
        # key is equal to the Tournament id retrieved via the
        # tourn_golfer object retrieved above
        # (pk = tourn_golfer.tg_tourn.tourn_id).
        # The filter method returns a list, but we just need
        # one tournament object, so use the .get() method
        # to retrieve the one and only tournament object.
        
        tournament = Tournament.objects.filter(pk=tourn_golfer.tg_tourn.tourn_id).get()

        # Now that we have a the tournament object, get the
        # golf course it was played at.
        # Get the GolfCourse object, (golf_course), whose primary
        # key is equal to the GolfCourse id retrieved via the
        # tournament object retrieved above
        # (pk = tournament.tourn_course.course_id).
        # Once again use .get() to retrieve the single golf_course
        
        golf_course = GolfCourse.objects.filter(pk=tournament.tourn_course.course_id).get()
        
        # Get the list of Hole objects, (holes), where the
        # Hole course id is equal to the course id from the
        # golf_course object retrieved above
        # (hole_course_id = golf_course.course_id).
        
        holes = Hole.objects.filter(hole_course_id = golf_course.course_id)
        
        # add the results to the context dictionary 
        context['tourn_golfer'] = tourn_golfer
        context['golf_course'] = golf_course
        context['scores'] = scores
        context['holes'] = holes
        
        return context
    