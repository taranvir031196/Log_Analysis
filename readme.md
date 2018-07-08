# log_analysis_project_Udacity

## PROJECT OVERVIEW-:

This is a udacity's full Stack Nanodegree project.In this project you will work with the data that have come from he real-world web application, with field representing 
information that a web server would record, such as HTTP status codes and url paths.The main aim of this project is to build an internal reporting tool for a newspaper 
site to draw conclusions on what Kind of articles the site's reader like.The database contains newspaper articles, as well as the web server log for the site.in order
to complete this project we need a CLI interface on which we will display our output.

## To START/RUN-:

We will need:

1. Python3
2. Vagrant
3. VirtualBox

## Setup-:
1. Install Vagrant and Virtual Box.
2. Clone this Repository.

## In order to Run-:

1. Launch the Vagrant VM by running command 'vagrant up' in the git bash terminal and then when the virtual machine is booted up in order log into the VM run command 'vagrant ssh'.

2. To load this data,use the command 'psql -d news -f newsdata.sql to connect to the database and run the necessary SQL.

The database includes three tables named-:

1. Articles Table.
2. Authors Table.
3. Log Table.

In order to retrieve the required results first we need to create three different views named-:

1. pop_articles-:
	"create view pop_articles as\
        select title,count(title) as views from articles,log\
        where log.path = concat('/article/',articles.slug)\
        group by title order by views DESC" 

2. pop_authors-:
	"create view pop_authors as select authors.name,\
        count(articles.author) as views from articles, log, authors where\
        log.path = concat('/article/',articles.slug) and\
        articles.author = authors.id group by authors.name order by views DESC"

3. log_status-:
	"create view log_status as select Date,Total,Error,\
        (Error::float*100)/Total::float as Percent from\
        (select time::timestamp::date as Date, count(status) as Total,\
        sum(case when status = '404 NOT FOUND' then 1 else 0 end) as Error\
        from log group by time::timestamp::date) as result\
        where (Error::float*100)/Total::float > 1.0 order by Percent DESC;"


## TO RUN THE CODE TO RETRIEVE QUERY RESULTS-:

In order to execute the program, run 'python newsdata.py' from the location where the project is being located from the command line and hence 
RETRIEVE THE OUTPUT.

					  "It was fun creating this Log Reporting Tool" 

  


 
