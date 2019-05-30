class Golfer:
    """Golfer object derived from data in the golfersInput.csv

    Attributes:
        golfer_id          a unique id for this golfer (to be used as a primary key when stored in the database)
        golfer_name        the name for the golfer
        golfer_birthdate   the golfers birthdate
                           NOTE: golfersInput.csv has this field in the format 'mm-dd-yy',
                                 but the database expects it in the format 'YYYY-mm-dd', so it needs converted

    """

    def __init__(self, golfer_id, name, bday):
        """
        constructor of class Hole
        """
        self.__golfer_id = golfer_id
        self.__golfer_name = name
        self.__golfer_birthdate = self.to_SQL_date(bday)
    
    ### Please complete the following functions
    
    def get_golfer_id(self):
        """
        return the golfer_id to the caller
        """
        return self.__golfer_id

    def get_golfer_name(self):
        """
        return the golfer_name to the caller
        """
        return self.__golfer_name
    
    def get_golfer_birthdate(self):
        """
        return the golfer_birthdate to the caller
        """
        return self.__golfer_birthdate

    def to_SQL_date(self, bday):
        """
        convert csv date ('mm-dd-yy') to sql date ('YYYY-mm-dd')
        """
        first_part = bday[:5]
        second_part = bday[-2:]
        self.to_SQL_date = "19" + second_part + "-" + first_part
        #print(self.to_SQL_date)

        return self.to_SQL_date


    def __str__(self):
        """
        return a comma-delimiter string
        of the instance variable values
        """
        csv_str = "{0},{1},{2}".format(
            self.__golfer_id,  self.__golfer_name, self.__golfer_birthdate)

        return csv_str
