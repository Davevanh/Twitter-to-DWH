# Twitter to DWH

This is an end to end project of retrieving data from Twitter, loading it into a Postgres database (treated as a data warehouse) and scheduling the Extract and Load processes (Python), as well as the data transformation processes (DBT) using Airflow 


<b>1. Set up relational tables in Postgres</b><br>
The first step was to create the relational tables that will be populated with data from the Tweepy API. The source code for these tables is in the SQL statements folder.

<b>2. Retrieving data from Tweepy</b><br>
The Twitter_analysis.ipyng file is the notebook used to retrieve and clean data from Twitter using Tweepy. This clean data has been put in dataframes to easily load the data into Postgres tables. 

<b>3. Designing the data warehouse</b><br>
As part of the project, I wanted to design a data warehouse according to Kimball principles. The result is this star schema: 

![alt text](https://user-images.githubusercontent.com/28791247/62795595-0700cb80-bacf-11e9-9691-83cd91e7bb2e.jpeg)
