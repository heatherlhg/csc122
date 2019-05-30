class Tournament:
    """
    Tournament object derived from data in the tournamentsInput.csv

    Instance variables:
        tourn_id       a unique id for this tournament (to be used as a primary key when stored in the database)
        tourn_name     the name for the tournament
        course_id      the id of the golf course where the tournament was played
        start_date     the date of the first round of this tournament
                       NOTE: tournamentsInput.csv has this field in the format 'm-dd-yy',
                             but the database expects it in the format 'YYYY-mm-dd',
                             so it needs converted

        num_rounds     number of rounds for this tournament (2, 3, or 4)
        num_golfers    number of golfers that played in the tournament

    """

    def __init__(self, tourn_id, name, course_id, start_date,
                 num_rounds, num_golfers):
        """
        constructor of class Tournament
        """
        self.__tourn_id = tourn_id
        self.__tourn_name = name
        self.__course_id = course_id
        self.__start_date = self.to_SQL_date(start_date)
        self.__num_rounds = num_rounds
        self.__num_golfers = num_golfers

    ### Please complete the following functions
        
    def get_tourn_id(self):
        """
        return the tourn_id to the caller
        """
        return self.__tourn_id

    def get_tourn_name(self):
        """
        return the tourn_name to the caller
        """
        return self.__tourn_name

    def get_course_id(self):
        """
        return the course_id to the caller
        """
        return self.__course_id

    def get_start_date(self):
        """
        return the start_date to the caller
        """
        return self.__start_date

    def get_num_rounds(self):
        """
        return the num_rounds to the caller
        """
        return self.__num_rounds

    def get_num_golfers(self):
        """
        return the num_golfers to the caller
        """
        return self.__num_golfers

    def to_SQL_date(self, start_date):
        """
        convert csv date ('mm-dd-yy') to sql date ('YYYY-mm-dd')
        return the converted date
        """
        first_part = start_date[:5]
        if len(first_part) < 6:
            first_part = start_date[:4]
            first_part = "0" + first_part
        second_part = start_date[-2:]
        self.to_SQL_date = "20" + second_part + "-" + first_part
        #print(self.to_SQL_date)

        return self.to_SQL_date

    def  __str__(self):
        """
        return a comma-delimiter string
        of the instance variable values
        """
        csv_str = "{0},{1},{2},{3},{4},{5}".format(
            self.__tourn_id, self.__tourn_name, self.__course_id,
            self.__start_date, self.__num_rounds, self.__num_golfers)

        return csv_str
