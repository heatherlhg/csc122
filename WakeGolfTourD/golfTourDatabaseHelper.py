"""
Creates the Golf Tour database - WakeGolfTour.db
Tables:
    GolfCourse
    Hole
    Golfer
    Tournament
    TournGolfer
    Round
    GolferRoundScores

The top of this module (file) has seven strings composed of 
the SQL language needed to create a table in the database.  
Each string is for one of the seven tables.
   
Please look at the code for the GolfCourse and Hole tables 
given to you.  Then following the example, code up the 
rest of them.

After the seven SQL strings, is a class definition.
You MUST not change any of the class definition code.
The class is used to create the database and the tables.

"""
import sqlite3
import csv


"""
This is the SQL string used to create the GolfCourse table: 
The fields are in the following order
and they have the following field types:

course_id        INTEGER  PRIMARY KEY
course_name      TEXT     DEFAULT 'UnKnown'
course_total_par INTEGER  DEFAULT 72

No FOREIGN Keys

"""
createGolfCourseTableSql = '''
CREATE TABLE IF NOT EXISTS GolfCourse (
course_id INTEGER  PRIMARY KEY NOT NULL,
course_name TEXT DEFAULT 'UnKnown' NOT NULL,
course_total_par INTEGER  DEFAULT 72 NOT NULL
);'''

"""
This is the SQL string used to create the Hole table: 
The fields are in the following order and 
they have the following field types:

hole_id        INTEGER  PRIMARY KEY 
hole_course_id INTEGER  DEFAULT 1
hole_number    INTEGER  DEFAULT 4
hole_par       INTEGER  DEFAULT 4

The hole_course_id is a FOREIGN Key.  
Note how we tell the database about this fact.
FOREIGN Keys are PRIMARY Keys for another table,
in this case for the GolfCourse table.

"""
createHoleTableSql = ''' 
CREATE TABLE IF NOT EXISTS Hole (
hole_id INTEGER  PRIMARY KEY NOT NULL,
hole_course_id INTEGER DEFAULT 1 NOT NULL,
hole_number INTEGER DEFAULT 4 NOT NULL,
hole_par INTEGER DEFAULT 4 NOT NULL,
FOREIGN KEY (hole_course_id) REFERENCES GolfCourse (course_id)
);'''

"""
This is the SQL string used to create the Golfer table: 
Follow the same format as with Hole:  
The fields are in the following order 
and they have the following field types:

golfer_id I      INTEGER PRIMARY KEY
golfer_name      TEXT DEFAULT 'UnKnown'
golfer_birthdate DATE DEFAULT '2016-01-01'

No FOREIGN Keys

"""
### Please provide your SQL code below
createGolferTableSql = ''' 
CREATE TABLE IF NOT EXISTS Golfer (
golfer_id INTEGER PRIMARY KEY NOT NULL,
golfer_name TEXT DEFAULT 'UnKnown',
golfer_birthdate DATE DEFAULT '2016-01-01');
'''

"""
This is the SQL string used to create the Tournament table: 
The fields are in the following order and 
they have the following field types:

tourn_id          INTEGER  PRIMARY KEY
tourn_name        TEXT     DEFAULT 'UnKnown'
tourn_course_id   INTEGER  DEFAULT 1
tourn_start_date  DATE     DEFAULT '2016-01-01'
tourn_num_rounds  INTEGER  DEFAULT 4 
tourn_num_golfers INTEGER  DEFAULT 15

The tourn_course_id is a FOREIGN Key.  
Note how we tell the database about this fact.
FOREIGN Keys are PRIMARY Keys for another table,
in this case for the GolfCourse table.

"""
### Please provide your SQL code below
createTournamentTableSql = ''' 
CREATE TABLE IF NOT EXISTS Tournament (
tourn_id INTEGER PRIMARY KEY,
tourn_name TEXT DEFAULT 'UnKnown',
tourn_course_id INTEGER DEFAULT 1,
tourn_start_date DATE DEFAULT '2016-01-01',
tourn_num_rounds INTEGER DEFAULT 4,
tourn_num_golfers INTEGER DEFAULT 15,
FOREIGN KEY (tourn_course_id) REFERENCES GolfCourse (course_id));
'''

"""
This is the SQL string used to create the Round table: 
Please follow the same format as with Hole:  
The fields are in the following order
and they have the following field types:

round_id       INTEGER PRIMARY KEY
round_tourn_id INTEGER DEFAULT 0
round_day      TEXT    DEFAULT 'Sun' 

The round_tourn_id is a FOREIGN Key.  
FOREIGN Keys are PRIMARY Keys for another table,
in this case for the Tournament table.

"""
### Please provide your SQL code below
createRoundTableSql = ''' 
CREATE TABLE IF NOT EXISTS Round (
round_id INTEGER PRIMARY KEY,
round_tourn_id INTEGER DEFAULT 0,
round_day TEXT DEFAULT 'Sun',
FOREIGN KEY (round_tourn_id) REFERENCES Tournament (tourn_id));
'''

"""
This is the SQL string used to create the TournGolfer table: 
The fields are in the following order and 
they have the following field types:

tg_id        INTEGER PRIMARY KEY
tg_tourn_id  INTEGER DEFAULT 0
tg_golfer_id INTEGER DEFAULT 0

Here there are two FOREIGN Keys. 
Note how we tell the database about this fact.

The tg_tourn_id is a FOREIGN Key.  
FOREIGN Keys are PRIMARY Keys for another table,
in this case for the Tournament table.

The tg_golfer_id is a FOREIGN Key.  
FOREIGN Keys are PRIMARY Keys for another table,
in this case for the Golfer table.
"""
### Please provide your SQL code below
createTournGolferTableSql = ''' 
CREATE TABLE IF NOT EXISTS TournGolfer (
tg_id INTEGER PRIMARY KEY,
tg_tourn_id INTEGER DEFAULT 0,
tg_golfer_id INTEGER DEFAULT 0,
FOREIGN KEY (tg_tourn_id) REFERENCES Tournament (tourn_id),
FOREIGN KEY (tg_golfer_id) REFERENCES Golfer (golfer_id));
'''

"""
This is the SQL string used to create the GolferRoundScores table: 
The fields are in the following order and 
they have the following field types:

grs_id              INTEGER  PRIMARY KEY 
grs_tourn_golfer_id INTEGER  DEFAULT 0 
grs_round_id        INTEGER  DEFAULT 0 
grs_total_score     INTEGER  DEFAULT 0 
grs_hole1_score     INTEGER  DEFAULT 0 
grs_hole2_score     INTEGER  DEFAULT 0 
grs_hole3_score     INTEGER  DEFAULT 0 
grs_hole4_score     INTEGER  DEFAULT 0 
grs_hole5_score     INTEGER  DEFAULT 0 
grs_hole6_score     INTEGER  DEFAULT 0 
grs_hole7_score     INTEGER  DEFAULT 0 
grs_hole8_score     INTEGER  DEFAULT 0 
grs_hole9_score     INTEGER  DEFAULT 0 
grs_hole10_score    INTEGER  DEFAULT 0 
grs_hole11_score    INTEGER  DEFAULT 0 
grs_hole12_score    INTEGER  DEFAULT 0 
grs_hole13_score    INTEGER  DEFAULT 0 
grs_hole14_score    INTEGER  DEFAULT 0 
grs_hole15_score    INTEGER  DEFAULT 0 
grs_hole16_score    INTEGER  DEFAULT 0 
grs_hole17_score    INTEGER  DEFAULT 0 
grs_hole18_score    INTEGER  DEFAULT 0 

Here there are two FOREIGN Keys. 
Note how we tell the database about this fact.

The grs_tourn_golfer_id is a FOREIGN Key.  
FOREIGN Keys are PRIMARY Keys for another table,
in this case for the TournGolfer table.

The grs_round_id is a FOREIGN Key.  
FOREIGN Keys are PRIMARY Keys for another table,
in this case for the Round table.

"""
### Please provide your SQL code below
createGolferRoundScoresTableSql = '''
CREATE TABLE IF NOT EXISTS GolferRoundScores (
grs_id INTEGER PRIMARY KEY,
grs_tourn_golfer_id INTEGER DEFAULT 0,
grs_round_id INTEGER DEFAULT 0,
grs_total_score INTEGER DEFAULT 0,
grs_hole1_score INTEGER DEFAULT 0,
grs_hole2_score INTEGER DEFAULT 0,
grs_hole3_score INTEGER DEFAULT 0,
grs_hole4_score INTEGER DEFAULT 0,
grs_hole5_score INTEGER DEFAULT 0,
grs_hole6_score INTEGER DEFAULT 0,
grs_hole7_score INTEGER DEFAULT 0,
grs_hole8_score INTEGER DEFAULT 0,
grs_hole9_score INTEGER DEFAULT 0,
grs_hole10_score INTEGER DEFAULT 0,
grs_hole11_score INTEGER DEFAULT 0,
grs_hole12_score INTEGER DEFAULT 0,
grs_hole13_score INTEGER DEFAULT 0,
grs_hole14_score INTEGER DEFAULT 0,
grs_hole15_score INTEGER DEFAULT 0,
grs_hole16_score INTEGER DEFAULT 0,
grs_hole17_score INTEGER DEFAULT 0,
grs_hole18_score INTEGER DEFAULT 0,
FOREIGN KEY (grs_tourn_golfer_id) REFERENCES TournGolfer (tg_id),
FOREIGN KEY (grs_round_id) REFERENCES Round (round_id));
'''

"""
This class is given to you.  
You do not have to change a thing.
PLEASE do not change this class.

This class is for creation of the WakeGolfTour database.
It has the following methods:

1. __init__ (self, database_name):
   Class constructor that receives the database name 
   as a parameter to get that private instance variable.
   
2. def get_database_name (self):
   Returns the database name  
   
3. def create_database (self):
   Creates and connects to the database.using Python DB-API
   Creates each of the nine database tables by calling the
     createTable method, which is passed the connection object
     and the corresponding SQL string created above for the 
     table creation.
     
4. def get_connection (self, db):
   Creates a database connection to the SQLite database
  
5. def create_table (self, conn, sql):
   Creates a database connection to the SQLite database
  
6. def save_to_database (self, tablename, csvdata):
   Saves the passed in CSV file data (csvdata) to the passed in 
      database table (tablename) and commits the changes
  
7. def close_connection(self):
   Closes the connection to the database
  
"""


class GolfTourDatabaseHelper:
    def __init__(self, database_name):
        """
        constructor of class GolfTourDatabaseHelper
        """

        self.__database_name = database_name
        self.__connection = None

    def get_database_name(self):
        """
        return the database name to the caller
        """

        return self.__database_name

    def create_database(self):
        """
        Create and/or connect to the database
        """

        conn = self.get_connection(self.__database_name)

        if conn is not None:

            print("Database created and opened successfully")

            # Create Wake Golf Tour Tables

            self.create_table(conn, createGolfCourseTableSql)
            print("GolfCourse Table created ")

            self.create_table(conn, createHoleTableSql)
            print("Golf Hole Table created ")

            self.create_table(conn, createGolferTableSql)
            print("Golfer Table created ")

            self.create_table(conn, createTournamentTableSql)
            print("Tournament Table created ")

            self.create_table(conn, createRoundTableSql)
            print("Tournament Round Table created ")

            self.create_table(conn, createTournGolferTableSql)
            print("Tournament Golfer Table created ")

            self.create_table(conn, createGolferRoundScoresTableSql)
            print("Golfer Round Scores Table created ")

        else:
            print("Error! cannot create or connect to the database.")

    def get_connection(self, db):
        """ 
        Create a database connection to the SQLite database 
        """

        if self.__connection is not None:
            return self.__connection

        try:
            self.__connection = sqlite3.connect(db)
            return self.__connection

        except ValueError as e:
            print(e)

        return None

    @staticmethod
    def create_table(conn, sql):
        """ 
        create a table  
        """

        try:
            c = conn.cursor()
            c.execute(sql)
            c.close()
            conn.commit()
        except ValueError as e:
            print("Error creating one of the tables. {}".format(e))

    def save_to_database(self, tablename, csvdata):
        """
        Save the data passed in (csvdata) to the 
             database table, tablename 
        """

        # Get connection, if not one already

        conn = self.__connection
        if conn is None:
            conn = self.get_connection(self.__database_name)

        # Get a cursor for the connection

        curs = conn.cursor()

        # Get the number of columns in the table

        columns_query = "PRAGMA table_info({})".format(tablename)
        curs.execute(columns_query)
        number_of_columns = len(curs.fetchall())

        # Generate the value placeholder string

        vals = "(" + ("?," * (number_of_columns - 1)) + "?)"

        # Read the data from the csv file and insert 
        #      the data from each record into table row

        records = csv.reader(open(csvdata, 'r'))

        for row in records:
            if len(row) == number_of_columns:
                curs.execute("INSERT OR REPLACE INTO {} VALUES {};".format(tablename, vals), row)
            else:
                print("ERROR: Table '{}' has {} columns".format(tablename, number_of_columns))
                print("       Data record has {} fields".format(len(row)))

        curs.close()

        # Commit the changes

        conn.commit()

    def close_connection(self):
        """
        Close the connection to the database 
        """

        if self.__connection is not None:
            self.__connection.close()
