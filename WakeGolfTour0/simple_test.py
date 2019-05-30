import pdb

def to_SQL_date(bday):
    """
    convert ('mm-dd-yy') to sql date ('YYYY-mm-dd')
    """
    pdb.set_trace()
    first_part = bday[5:]
    second_part = bday[:-2]
    bday_sql = "19" + second_part + "-" + first_part
    return bday_sql

def main():
    bday = '09-11-80'
    sql_bday = to_SQL_date(bday)
    print(sql_bday)

main()

