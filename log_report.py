#! /usr/bin/env python
# Project-:Log Analysis-Udacity

import psycopg2


def connect(database_name="news"):
    """Connect to the PostgreSQL database and try to retrieve the database"""
    try:
        DB = psycopg2.connect("dbname={}".format(database_name))
        cursor = DB.cursor()
        return DB, cursor
    except:
        print("Error in connecting the database")

""" Uncomment defined functions in order to create the view."""

"""
def get_popular_articles():
    try:
        DB, cursor = connect()
        query = "create or replace view pop_articles as\
        select title,count(title) as views from articles,log\
        where log.path = concat('/article/',articles.slug)\
        group by title order by views DESC"
        cursor.execute(query)
        DB.commit()
        DB.close()
    except:
        print("Error in viewing popular articles")


def get_popular_authors():
    try:
        DB, cursor = connect()
        query = "create or replace view pop_authors as select authors.name,\
        count(articles.author) as views from articles, log, authors where\
        log.path = concat('/article/',articles.slug) and\
        articles.author = authors.id group by authors.name order by views DESC"
        cursor.execute(query)
        DB.commit()
        DB.close()
    except:
        print("Error in viewing popular authors")


def get_log_report():
    try:
        DB, cursor = connect()
        query = "create or replace view log_status as select Date,Total,Error,\
        (Error::float*100)/Total::float as Percent from\
        (select time::timestamp::date as Date, count(status) as Total,\
        sum(case when status = '404 NOT FOUND' then 1 else 0 end) as Error\
        from log group by time::timestamp::date) as result\
        where (Error::float*100)/Total::float > 1.0 order by Percent DESC;"
        cursor.execute(query)
        DB.commit()
        DB.close()
    except:
        print("Error in creating log report")
"""


def find_popular_articles():
    """This function prints the three most popular articles of all time"""
    DB, cursor = connect()
    query = "select * from pop_articles LIMIT 3"
    cursor.execute(query)
    result = cursor.fetchall()
    DB.close()
    print("\n Top three Popular Articles:\n")
    for x in range(0, len(result), 1):
        print '\t' + str(result[x][0]) + '--->' + str(result[x][1]) + "views"


def find_popular_authors():
    """This function prints most popular authors of all time"""
    DB, cursor = connect()
    query = "select * from pop_authors"
    cursor.execute(query)
    result = cursor.fetchall()
    DB.close()
    print("\n The Popular Authors:\n")
    for x in range(0, len(result), 1):
        print "\t" + result[x][0] + "--->" + str(result[x][1]) + "views"


def find_log_report():
    """function prints on which day more than 1% requests turned into error"""
    DB, cursor = connect()
    query = "select * from log_status"
    cursor.execute(query)
    result = cursor.fetchall()
    DB.close()
    print("\n The Log Report:\n")
    for x in range(0, len(result), 1):
        print str(result[x][0]) + "-" + str(round(result[x][3], 2)) + "%err"

    # calling all the functions defined above functions

if __name__ == '__main__':
    # Uncomment these in order to call the function.
    """
    get_popular_articles()
    get_popular_authors()
    get_log_report()
    """
    find_popular_articles()
    find_popular_authors()
    find_log_report()

    print"\n SUCCESSFUL ANALYSIS PERFORMED!!! \n"
