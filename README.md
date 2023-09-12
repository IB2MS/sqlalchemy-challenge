# sqlalchemy-challenge

# sqlalchemy-challenge

![fig1.png](Images/fig1.jng)

I've decided to treat myself to a long holiday vacation in Honolulu, Hawaii. To help with my trip planning, i decided to do a climate analysis about the area. 
The steps that I took to accomplish this task:

## Part 1: Analyze and Explore the Climate Data

I  used Python and SQLAlchemy to do a basic climate analysis and data exploration of climate database. Specifically, I  used  SQLAlchemy ORM queries, Pandas, and Matplotlib with the provided files (climate_starter.ipynb and hawaii.sqlite).

* Used the SQLAlchemy `create_engine` function to connect to your SQLite database.
* Used the SQLAlchemy `automap_base()` function to reflect your tables into classes, and then save references to the classes named `Station` and `Measurement`.
* Linked Python to the database by creating a SQLAlchemy session.
* Performed a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

1. Found the most recent date in the dataset.
2. Using that date, got the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Select only the `date` and `prcp` values.
4. Load the query results into a Pandas DataFrame. Explicitly set the column names.
5. Sort the DataFrame values by "date".
6. Plot the results by using the DataFrame plot method, as the following image shows:
    ![fig2](Images/fig2.png)

7. Use Pandas to print the summary statistics for the precipitation data.  

### Station Analysis

   *  Designed a query to get the previous 12 months of temperature observation (TOBS) data.
   *  Designed a query to calculate the total number of stations.
   *  Plot the results as a histogram with `bins=12`, as the following image shows: 

![fig3](Images/fig3.png)

## Part 2: Design Your Climate App

I’ve completed initial analysis, I design a Flask API based on the queries that O just developed. To do so, used Flask to create your routes as follows:

### Routes

* `/`

* `/api/v1.0/precipitation`

* `/api/v1.0/stations`

* `/api/v1.0/tobs`

* `/api/v1.0/<start>` 

* `/api/v1.0/<start>/<end>`

### Temperature Analysis

* Hawaii is place to enjoy mild weather all year.  The reason for this is the average_temp = 71,66 , max_temp = 85.0, min_temp = 54.0
* One of the impotant factors when we traveling , of course , precipition: most pprecipition: in August , january, AApril and july. 


   