class Round:
    """
    Round object derived from data in the tournamentInput.csv

    Instance variables:
        round_id        a unique id for this round (to be used as a primary key when stored in the database)
        tourn_id        the id of the tournament for this round
        day             the day that the round was played ('Thu', 'Fri', 'Sat', 'Sun')
    """
    ### Please complete this class  

    def __init__(self, round_id, tourn_id, day):

        self.__round_id = round_id
        self.__tourn_id = tourn_id
        self.__day = day

    def get_round_id(self):

        return self.__round_id

    def get_tourn_id(self):

        return self.__tourn_id

    def get_day(self):

        return self.__day

    def __str__(self):

        csv_str = "{0},{1},{2}".format(
            self.__round_id,  self.__tourn_id, self.__day)

        return csv_str
