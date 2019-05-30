from django.db import models
from tournament.models import Tournament, Round
from golf_course.models import GolfCourse
from operator import itemgetter

class Golfer(models.Model):
    golfer_id = models.IntegerField(primary_key=True)
    golfer_name = models.TextField()
    golfer_birthdate = models.DateField()
    golfer_city = models.TextField(default="unknown", blank=True)

    class Meta:
        managed = True
        db_table = 'Golfer'
    
    def __str__(self):
        return self.golfer_name


class TournGolfer(models.Model):
    tg_id = models.IntegerField(primary_key=True)
    tg_tourn = models.ForeignKey(Tournament, models.DO_NOTHING)
    tg_golfer = models.ForeignKey(Golfer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TournGolfer'
        verbose_name = "Tournament Golfer"
        verbose_name_plural = "Tournament Golfers"
    
    def getGolferName(self):
        return self.tg_golfer.golfer_name
    
    def getTournName(self):
        return self.tg_tourn.tourn_name
    
    def __str__(self):
        return "{} {}".format (self.tg_tourn.tourn_name, 
                               self.tg_golfer.golfer_name)

class GolferRoundScores(models.Model):
    grs_id = models.IntegerField(primary_key=True)
    grs_tourn_golfer = models.ForeignKey(TournGolfer, models.DO_NOTHING)
    grs_round = models.ForeignKey(Round, models.DO_NOTHING)
    grs_total_score = models.IntegerField()
    grs_hole1_score = models.IntegerField()
    grs_hole2_score = models.IntegerField()
    grs_hole3_score = models.IntegerField()
    grs_hole4_score = models.IntegerField()
    grs_hole5_score = models.IntegerField()
    grs_hole6_score = models.IntegerField()
    grs_hole7_score = models.IntegerField()
    grs_hole8_score = models.IntegerField()
    grs_hole9_score = models.IntegerField()
    grs_hole10_score = models.IntegerField()
    grs_hole11_score = models.IntegerField()
    grs_hole12_score = models.IntegerField()
    grs_hole13_score = models.IntegerField()
    grs_hole14_score = models.IntegerField()
    grs_hole15_score = models.IntegerField()
    grs_hole16_score = models.IntegerField()
    grs_hole17_score = models.IntegerField()
    grs_hole18_score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'GolferRoundScores'
        verbose_name = "Golfer Round Scores"
        verbose_name_plural = "Golfers Round Scores"
        
    def getTournScores(tourn_id):
        # the list to return
        tournament_scores = list();
        
        # get the list of tourn golfers for this tournament # using the filter method of TournGolfer.objects
        # with the tg_tourn equal to the passed in tourn_id 
        tourn_golfers = TournGolfer.objects.filter(tg_tourn = tourn_id)
        
        # loop through the tourngolfer objects,
        # get the golfer name, tournament name
        # (use the helper functions) and the scores for # that golfer for each round of the tournament, 
        
        for tourn_golfer in tourn_golfers:
        # clear total score and create new dictionary object
            total_score = 0
            gts = dict()
            
            # get the golfer name and tournament name
            # using the tourn_golfer key and the helper
            # methods created above
            gts["golfer_name"] = tourn_golfer.getGolferName()
            gts["tournament_name"] = tourn_golfer.getTournName()
            
            # store the tourn_golfer_id for indexing later
            gts["tourn_golfer_id"] = tourn_golfer.tg_id
            
            # get the scores for this tourn_golfer from
            # the GolferRoundScores
            scores = GolferRoundScores.objects.filter(grs_tourn_golfer = tourn_golfer,).order_by('grs_round')
            
            # loop through the scores for each round,
            # putting the score in the dict and adding
            # it to the total score for the tournament
            for i in range(1, len(scores)+1):
                round_score = scores[i-1].grs_total_score
                gts["round{}_score".format(i)] = round_score
                total_score = total_score + round_score
                
            # store the total score
            gts["total_score"] = total_score

            # add the disctionary entry to the list
            tournament_scores.append(gts)
    
        # return the list sorted by "total_score"
        return sorted(tournament_scores, key=itemgetter('total_score'))
        
    
    def getTournScoresByGolfer(golfer_id):
        tournament_scores = list();
        tourn_golfers = TournGolfer.objects.filter(tg_golfer = golfer_id)
        
        for tourn_golfer in tourn_golfers:
            total_score = 0
            gts = dict()
            
            gts["golfer_name"] = tourn_golfer.getGolferName()
            gts["tournament_name"] = tourn_golfer.getTournName()
            
            gts["tourn_golfer_id"] = tourn_golfer.tg_id
            
            scores = GolferRoundScores.objects.filter (grs_tourn_golfer = tourn_golfer,).order_by('grs_round')
            
            for i in range(1, len(scores)+1):
                round_score = scores[i-1].grs_total_score
                total_score = total_score + round_score
                
            gts["total_score"] = total_score

            tournament_scores.append(gts)
            
        return sorted(tournament_scores, key=itemgetter('total_score'))

    def getParDiffs(self):
        scoreList = [] 
        for i in range(18):
            score = getattr(self,"grs_hole{}_score".format(i+1))
            scoreList.append(score)    
        parList = self.grs_tourn_golfer.tg_tourn.tourn_course.getParList()
        round_scores_diff = []
        for i in range(18):
            hole_score_par_diff = []
            hole_score = scoreList[i]
            par = parList[i]
            par_diff = hole_score - par
            hole_score_par_diff.append(hole_score)
            hole_score_par_diff.append(par_diff)
            round_scores_diff.append(hole_score_par_diff)
        return round_scores_diff
   
    def __str__(self):
        return "{} {} {} {}".format (self.grs_tourn_golfer.tg_golfer, 
                                     self.grs_tourn_golfer.tg_tourn,  
                                     self.grs_round, self.grs_total_score)