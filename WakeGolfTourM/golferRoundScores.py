class GolferRoundScores:
    """
    GolferRoundScores object derived from data in the roundScoresInput.csv
    Holds the scores for a single round of golf for a golfer in a tournament

    Instance variables:
        golfer_round_id    a unique id for this golfer round score object (to be used as a primary key when stored in the database)
        tourn_golfer_id    the id of the tournament golfer that the scores are for
        round_id           the id of the tournament round that the scores are for
        total_round_score  total score for this round
        hole1_score        score for hole number 1 for this round
        hole2_score        score for hole number 2 for this round
         ...
        hole18_score       score for hole number 18 for this round

    """
    
    def __init__(self, golfer_round_id, tourn_golfer_id, round_id,
                 tot_round_score, scores):
        """
        constructor of class Tournament
        """
        self.__golfer_round_id = golfer_round_id
        self.__tourn_golfer_id = tourn_golfer_id
        self.__round_id = round_id
        self.__total_round_score = tot_round_score
        self.__hole1_score = scores[0]
        self.__hole2_score = scores[1]
        self.__hole3_score = scores[2]
        self.__hole4_score = scores[3]
        self.__hole5_score = scores[4]
        self.__hole6_score = scores[5]
        self.__hole7_score = scores[6]
        self.__hole8_score = scores[7]
        self.__hole9_score = scores[8]
        self.__hole10_score = scores[9]
        self.__hole11_score = scores[10]
        self.__hole12_score = scores[11]
        self.__hole13_score = scores[12]
        self.__hole14_score = scores[13]
        self.__hole15_score = scores[14]
        self.__hole16_score = scores[15]
        self.__hole17_score = scores[16]
        self.__hole18_score = scores[17]

    def get_golfer_round_id(self):    # golfer_round_id
        """ 
        return the golfer_round_id to the caller 
        """
        return self.__golfer_round_id
                          
    def get_tourn_golfer_id(self):    # tourn_id
        """ 
        return the tourn_golfer_id to the caller
        """
        return self.__tourn_golfer_id
        
    def get_round_id(self):    # round_id
        """ 
        return the round_id to the caller 
        """
        return self.__round_id

    def total_round_score(self):    # total_round_score
        """ 
        return the total_round_score to the caller 
        """
        return self.__total_round_score

    def get_hole1_score(self):  # hole1_score
        """
        return the hole1_score to the caller
        """
        return self.__hole1_score

    def get_hole2_score(self):   # hole2_score
        """
        return the hole2_score to the caller
        """
        return self.__hole2_score

    def get_hole3_score(self):   # hole3_score
        """
        return the hole3_score to the caller
        """
        return self.__hole3_score

    def get_hole4_score(self):   # hole4_score
        """
        return the hole4_score to the caller
        """
        return self.__hole4_score

    def get_hole5_score(self):   # hole5_score
        """
        return the hole5_score to the caller
        """
        return self.__hole5_score

    def get_hole6_score(self):   # hole6_score
        """
        return the hole6_score to the caller
        """
        return self.__hole6_score

    def get_hole7_score(self):   # hole7_score
        """
        return the hole7_score to the caller
        """
        return self.__hole7_score

    def get_hole8_score(self):   # hole8_score
        """
        return the hole8_score to the caller
        """
        return self.__hole8_score

    def get_hole9_score(self):   # hole9_score
        """
        return the hole9_score to the caller
        """
        return self.__hole9_score

    def get_hole10_score(self):   # hole10_score
        """
        return the hole10_score to the caller
        """
        return self.__hole10_score

    def get_hole11_score(self):   # hole11_score
        """
        return the hole11_score to the caller
        """
        return self.__hole11_score

    def get_hole12_score(self):   # hole12_score
        """
        return the hole12_score to the caller
        """
        return self.__hole12_score

    def get_hole13_score(self):   # hole13_score
        """
        return the hole13_score to the caller
        """
        return self.__hole13_score

    def get_hole14_score(self):   # hole14_score
        """
        return the hole14_score to the caller
        """
        return self.__hole14_score

    def get_hole15_score(self):   # hole15_score
        """
        return the hole15_score to the caller
        """
        return self.__hole15_score

    def get_hole16_score(self):   # hole16_score
        """
        return the hole16_score to the caller
        """
        return self.__hole16_score

    def get_hole17_score(self):   # hole17_score
        """
        return the hole17_score to the caller
        """
        return self.__hole17_score

    def get_hole18_score(self):   # hole18_score
        """ 
        return the hole18_score to the caller
        """
        return self.__hole18_score
            
    def __str__(self):
        """ 
        create a comma-delimiter string 
        of the instance variable values 
        """
        csv_str = "{},{},{},{}".format(
            self.__golfer_round_id,  self.__tourn_golfer_id, 
            self.__round_id,  self.__total_round_score)

        csv_str += ",{}".format(self.__hole1_score)  
        csv_str += ",{}".format(self.__hole2_score)  
        csv_str += ",{}".format(self.__hole3_score)  
        csv_str += ",{}".format(self.__hole4_score)  
        csv_str += ",{}".format(self.__hole5_score)  
        csv_str += ",{}".format(self.__hole6_score)  
        csv_str += ",{}".format(self.__hole7_score)  
        csv_str += ",{}".format(self.__hole8_score)  
        csv_str += ",{}".format(self.__hole9_score)  
        csv_str += ",{}".format(self.__hole10_score)
        csv_str += ",{}".format(self.__hole11_score)
        csv_str += ",{}".format(self.__hole12_score)
        csv_str += ",{}".format(self.__hole13_score)
        csv_str += ",{}".format(self.__hole14_score)
        csv_str += ",{}".format(self.__hole15_score)
        csv_str += ",{}".format(self.__hole16_score)
        csv_str += ",{}".format(self.__hole17_score)
        csv_str += ",{}".format(self.__hole18_score)
                  
        return csv_str
