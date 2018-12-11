Project (1): Log Analysis


#Start with Software Installation:

a. Vagrant: https://www.vagrantup.com/downloads.html
b. Virtual Machine: https://www.virtualbox.org/wiki/Downloads
c. Download a FSND virtual machine: https://github.com/udacity/fullstack-nanodegree-vm
and probably you will find the file in your “Download” folder.
- You will also need a Unix-style terminal program. On Mac or Linux systems, you can use the
built-in Terminal. On Windows, we recommend Git Bash, which is installed with the Git version control software.

--------------------------------------

#Once you get the above software installed, follow the following instructions:
cd vagrant
vagrant up
vagrant ssh
cd /vagrant
mkdir log-analysis-project cd log-analysis-project

--------------------------------------
#Download and Load the Data
a. For this project, you need to download “newsdata.sql” from the project page or by clicking
on the following link:
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdat
a.zip

#Load the data from the “newsdata.sql”
psql -d news -f newsdata.sql
--------------------------------------
#connect to your database using:
psql -d news
--------------------------------------


## requirments :
- psycopg2
- pycodestyle



## Questions
1. What are the most popular three articles of all time?

    ```
      SELECT slug as PATH, count(path) as View 
      FROM log,articles 
      WHERE substring (log.path,10)=articles.slug 
      GROUP BY articles.slug  
      ORDER BY View DESC limit 3;"

    ```

2. Who are the most popular article authors of all time?
       ```
       SELECT authors.name AS Auther, count(path) as View
        FROM authors
        JOIN articles on authors.id = articles.author
        JOIN log on substring (log.path,10)=articles.slug
        GROUP BY authors.name  ORDER BY View DESC LIMIT 4;
       
       ```


3. On which days did more than 1% of requests lead to errors?
		 ```
		CREATE VIEW total_view AS
		SELECT date(time), COUNT(*) AS views
		FROM log 
		GROUP BY date(time)
		ORDER BY date(time);
		```

		```sql
		CREATE VIEW error_view AS
		SELECT date(time), COUNT(*) AS errors
		FROM log WHERE status = '404 NOT FOUND' 
		GROUP BY date(time) 
		ORDER BY date(time);
		```

		```sql
		CREATE VIEW error_rate AS
		SELECT total_view.date, (100.0*error_view.errors/total_view.views) AS percentage
		FROM total_view, error_view
		WHERE total_view.date = error_view.date
		ORDER BY total_view.date;