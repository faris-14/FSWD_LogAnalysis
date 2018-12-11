#!/usr/bin/env python3

import psycopg2
import re
import string
import os
import sys

# !-----------------


def main():

    # Connect to an existing database
    conn = psycopg2.connect("dbname=news")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Question 1
    sql_popular_articles = """
    SELECT slug as PATH, count(path) as View
    FROM log,articles
    WHERE substring (log.path,10)=articles.slug
    GROUP BY articles.slug
    ORDER BY View DESC limit 3;
    """

    print("Q1: Most Popular Articles:")
    tmp = sql_popular_articles
    cur.execute(tmp)
    for (PATH, View) in cur.fetchall():
        path = PATH.replace('-', ' ').title()
        print('" {}  --  {} views "'.format(path, View))
    print(".." * 30)
# ---------------------------------------------------------
    # Q2: What are the most popular article authors of all time ?
    sql_popular_authors = """
        SELECT authors.name AS Auther, count(path) as View
        FROM authors
        JOIN articles on authors.id = articles.author
        JOIN log on substring (log.path,10)=articles.slug
        GROUP BY authors.name
        ORDER BY View DESC LIMIT 4;
    """

    print("\nQ2: Most Popular Article Authors :")
    tmp = sql_popular_authors
    cur.execute(tmp)
    for (PATH, View) in cur.fetchall():
        path = PATH.replace('-', ' ').title()
        print('"{}  --  {} views"'.format(path, View))
        print(".." * 30)
# ---------------------------------------------------------
    # Question 3
    sql_percent_errors = """
    SELECT *
    FROM error_rate
    WHERE error_rate.percentage > 1
    ORDER BY error_rate.percentage DESC;
    """
    print("\nQ3 :which days did more than 1% of requests lead to errors?")
    tmp = sql_percent_errors
    cur.execute(tmp)
    for (date, percentage) in cur.fetchall():
        print('" {} -- {}% errors"'.format(date.strftime('%b %d , %Y'),
              round(percentage, 3)))
    print(".." * 30)
    # Close communication with the database

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
