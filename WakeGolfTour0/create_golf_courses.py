import csv
from my_trace import trace_function
from golfCourse import GolfCourse


@trace_function()
def main():
    """
    Algorithm:
    1.  Initialize the input and output file names
    2.  Initialize the database and table names for output
    3.  Call create_golf_courses function, passing in the the input
        file name, and retrieving the returned golf_course_list,
        a list of GolfCourse objects containing information for 5 
        golf courses and the returned golf_course_holes_dict which 
        has the golf_course_id as the key, and the value is a list 
        of 18 tuples containing (hole_num, par_value).
    4.  Write out the class objects to files from:
        create_golf_courses
     """
    print("Wake Golf Tour Project 1")

    # 1. Initialize the input and output file names
    #input
    golf_courses_infile = "golfCoursesInput.csv"

    # output    
    golf_courses_file = "golfCourses.csv"

    # 2. Call create_golf_courses function, passing in the input
    #    file name, and retrieving the returned golf_courses_list,
    #    a list of 5 golf course objects and the golf_course_holes_dict,
    #    containing information about the holes for each of the golf courses
    
    golf_course_list, golf_course_holes_dict = create_golf_courses(golf_courses_infile)

    # 3. Write out the list returned from the create function:

    write_objs_to_file(golf_courses_file, golf_course_list)


@trace_function(printArgs=True, printRes=True)
def create_golf_courses(filename):
    """
    Each line of input contains:
    golf_course_name, par_h1, par_h2, ..., par_h18

    where golf_course_name is the name of the golf course and each
          par_h# is a par value for the hole #.
    
    Note: string input needs to be stripped of any whitespace
          integer strings need to be changed to ints 

    Algorithm:
    1. Create an empty list called golf_course_list that will contain
       GolfCourse objects whose data comes from the input file
    2. Create a dictionary, golf_course_holes_dict, having the golf_course_id as the key,
       and a list of 18 tuples containing (hole_num, par_value) as the value
       Each entry will have:
         golf_course_id: [(hole_num, par_value), 
                          (hole_num, par_value), ..., 
                          (hole_num, par_value)]
    3. Initialize the golf_course_id to 1
    4. Use a try/except block to capture a File Not Found Error
        a. Open the input file object for reading the input file
        b. Call the csv.reader function, passing in the input file
           and capturing the CSV file contents.
        c. Create a list from the file contents: courses_list
        d. Create an outer loop to read each golf course in courses_list
           Outer Loop
            1. Get the golf course name from the first element stripped of whitespace.
            2. Create an empty list, hole_info,  to hold the hole information
            3. Create an inner loop to traverse the 18 hole
               par values using the range function
               Inner Loop
                 a. Convert the string hole par values to ints
                 b. Add par value to total par
                 c. Append hole_num and par value to the hole_info list

            3. Add entry for this golf course's hole_info to the golf_course_holes_dict
            4. Create a new GolfCourse object, call it golf_course,
               passing in golf_course_id, golf_course_name, and total_par
            5. Append the golf_course object to the golf_course_list
            6. Increment the golf_course_id

        e. Close input_file object
    3. Print each golf_course object in the golf_course_list to the console
    4. Return the golf_course_list
    """

    print("\nGolf Course List: golf_course_list\n")
    print("function name: " + create_golf_courses.__name__)

    # Algorithm:
    # 1. Create an empty list called golf_course_list that will contain
    #    GolfCourse objects whose data comes from the input file

    golf_course_list = []

    # 2. Create an empty dictionary called golf_course_holes_dict
    #    whose key is the golf_course_id and the value is a tuple
    #    containing hole_number and par_value
    
    golf_course_holes_dict = dict()

    # 3. Initialize the golf_course_id to 1

    golf_course_id = 1

    # 4. Use a try/except block to capture a File Not Found Error

    try:
        # a. Open the input_file object for reading the input file

        input_file = open(filename, 'r')

        # b. Call the csv.reader function, passing in the input file
        #    and capturing the CSV file contents.

        file_lines = csv.reader(input_file)

        # c. Create a list from the file contents: courses_list

        courses_list = list(file_lines)

        # d. Create an outer loop to read each golf course in
        #    courses_list

        for golf_course in courses_list:

            # Outer Loop
            # 1. The first element (golf course name) is stripped
            #    of whitespace.

            golf_course_name = golf_course[0].strip()

            # 2. Create an inner loop to traverse the 18 hole
            #    par values using the range function

            total_par = 0
            holes = []
            for i in range(1,19):
                # Inner Loop
               
                # a. Get hole par value
                par = int(golf_course[i])

                # b. Add value to total par
                total_par = total_par + par

                # c. Append hole_num and par to list for dictionary
                holes.append((i, par))

            # 2. Add entry for this golf course's holes to the golf_course_holes_dict
            golf_course_holes_dict[golf_course_id] = holes

            # 4. Create a new GolfCourse object, call it golf_course,
            #    passing in golf_course_id, golf_course_name, and total_par

            golf_course = GolfCourse(golf_course_id, golf_course_name, total_par)

            # 5. Append the golf_course object to the golf_course_list

            golf_course_list.append(golf_course)

            # 6. Increment the golf_course_id

            golf_course_id = golf_course_id + 1

        # e. Close input_file object

        input_file.close()

    except IOError:
        print("File Not Found Error.")

    # 4. Print the golf_course_list objects to the console

    for gc in golf_course_list:
        print(gc)

    # 5. Return the golf_course_list and holes dictionary

    return golf_course_list, golf_course_holes_dict


@trace_function(printArgs=True, printRes=True)
def write_objs_to_file(filename, object_list):
    """
    This function takes a nested_list as input and writes it
    out to a csv file, where each line is a inner list

    Algorithm:
    1. Open the output file object for writing
    2. Create a loop to traverse the object_list parameter,
       where the loop variable is each object in the list:
       Loop:
       a. Set a str_obj string variable to the result of
          converting 'object' to a string using the __str__ 
          method of the class..  This can be accomplished 
          by passing the object into the str() function.
       b. Add a new line character to the end of the
          str_obj string
       c. Use the write method of the output file object to
          write the str_obj string to the output file,
    3. Close the output file
    """
    # 1. Open the output file object for writing

    output_file = open(filename, 'w')

    # 2. Create a loop to traverse the object_list parameter,
    #    where the loop variable is each object in the list:

    for obj in object_list:
        # Loop:
        # a. Set a str_obj string variable to the result of
        #    converting 'object' to a string using the
        #    __str__ method of the class.  This can be
        #    accomplished by passing the object into the
        #    str() function.

        str_obj = str(obj)

        # b. Add a new line character to the end of the
        #    str_obj string

        str_obj += '\n'

        # c. Use the write method of the output file object
        #    to write the str_obj string to the output file,

        output_file.write(str_obj)

    # 3. Close the output file

    output_file.close()

main()

