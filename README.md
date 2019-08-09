# Twitter to Postgres data warehouse 

This is an end to end project of extracting data from Twitter, loading it into a Postgres database (treated as a data warehouse), and scheduling the ELT (python + DBT, see the Twitter-DBT repository) using Airflow.


<b>1. Set up relational tables in Postgres</b><br>
First, the relational tables that will be populated with data from the Tweepy API have been created. The queries for this are stored in the SQL statements folder.

<b>2. Retrieving data from Tweepy</b><br>
The Twitter_analysis.ipyng file is the notebook used to retrieve and clean data from Twitter using Tweepy. The cleaned data has been put in data frames to easily load into the Postgres tables. 

<b>3. Designing the data warehouse</b><br>
As part of the project, I wanted to design a data warehouse according to Kimball principles. The result is this star schema: 

![alt text](https://user-images.githubusercontent.com/28791247/62795595-0700cb80-bacf-11e9-9691-83cd91e7bb2e.jpeg)

<b>4. Scheduling the ELT jobs</b><br>
The project is spread across two repositories: Twitter-DBT and this one, Twitter-to-DWH. The Twitter-DBT is the repository containing all code that runs the data transformations within the Postgres data warehouse using DBT. Both the python code (Twitter_analysis.ipyng) as well as the DBT code are being scheduled in order to fully automate this project. The automation is done using Airflow, which creates a DAG of tasks that need to be run in a set order. For this project, the steps are: 
1. Run the python script to Extract data from Twitter and Load it into Postgres
2. Run the dbt run command to finalize the data transformations within the Postgres data warehouse
3. Send an email in case any of the above tasks fail 
