from my_trace import trace_class_method

class GolfCourse:
    """
    GolfCourse object derived from data in the golfCoursesInput.csv

    Attributes:
        course_id      a unique id for this golf course (to be used as a primary key when stored in the database)
        course_name    the name for the golf course
        total_par      the total par for this course
    """
    @trace_class_method(printArgs=True)
    def __init__(self, course_id, name, tot_par):
        """
        constructor of class GolfCourse
        """
        self.__course_id = course_id
        self.__course_name = name
        self.__total_par = tot_par

    @trace_class_method(printRes=True)
    def get_course_id(self):  # course_id
        """
        return the course_id to the caller
        """
        return self.__course_id

    @trace_class_method(printRes=True)
    def get_course_name(self):  # course_name
        """
        return the course_name to the caller
        """
        return self.__course_name

    @trace_class_method(printRes=True)
    def get_total_par(self):  # total_par
        """
        return the total_par to the caller
        """
        return self.__total_par

    @trace_class_method(printRes=True)
    def __str__(self):
        """
        create a comma-delimiter string
        of the instance variable values
        """
        csv_str = str(self.__course_id) + ',' + self.__course_name + \
                 ',' + str(self.__total_par)

        return csv_str
