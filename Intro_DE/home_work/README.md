### Home 
download data to a specific folder and download incase of network interruption:
```
wget -c https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2019-10.parquet -P data
```

- Putting it into postgress
### Question 3 answers:

- 1 mile excluisive and 3 inclusive 
```
SELECT COUNT(*) FROM green_taxi
WHERE lpep_dropoff_datetime >='2019-10-1' AND lpep_dropoff_datetime < '2019-11-1' 
AND trip_distance > '1' AND trip_distance <='3'
AND trip_distance IS NOT NULL
```

- 3 miles exclusive and 7 miles inclusive 
```
SELECT COUNT(*) FROM green_taxi
WHERE lpep_dropoff_datetime >='2019-10-1' AND lpep_dropoff_datetime < '2019-11-1' 
AND trip_distance > '3' AND trip_distance <='7' 
AND trip_distance IS NOT NULL
```

- 7 miles exlusive and 10 miles inclusive 

```
SELECT COUNT(*) FROM green_taxi
WHERE lpep_dropoff_datetime >='2019-10-1' AND lpep_dropoff_datetime < '2019-11-1' 
AND trip_distance > '7' AND trip_distance <='10' 
AND trip_distance IS NOT NULL
```

-over 10 miles 
```
SELECT COUNT(*) FROM green_taxi
WHERE lpep_dropoff_datetime >='2019-10-1' AND lpep_dropoff_datetime < '2019-11-1' 
AND trip_distance > '10'
AND trip_distance IS NOT NULL
```

here is the answer : `104,802; 198,924; 109,603; 27,678; 35,189`

### Question 4. Longest trip for each day

Which was the pick up day with the longest trip distance? Use the pick up time for your calculations.

Tip: For every day, we only care about one single trip with the longest distance.

```
WITH DailyMax AS(
SELECT DATE(lpep_pickup_datetime) AS pickup_day,
MAX(trip_distance) AS max_distance_per_day
FROM green_taxi
GROUP BY DATE(lpep_pickup_datetime)
)
SELECT pickup_day,max_distance_per_day AS longest_trip_distance FROM DailyMax
WHERE max_distance_per_day = (SELECT MAX(max_distance_per_day) FROM DailyMax);
```

answer: `2019-10-31`

### Question 5. Three biggest pickup zones

Which were the top pickup locations with over 13,000 in total_amount (across all trips) for 2019-10-18?

Consider only lpep_pickup_datetime when filtering by date.

```
SELECT 
    DATE(t.lpep_pickup_datetime) AS pickup_day,
    CONCAT(zpu."Borough", ' / ', zpu."Zone") AS pickup_loc,
    SUM(t.total_amount) AS total_amount_sum
FROM green_taxi t
JOIN zones zpu 
  ON t."PULocationID" = zpu."LocationID"
WHERE DATE(t.lpep_pickup_datetime) = '2019-10-18'
GROUP BY pickup_day, pickup_loc
HAVING SUM(t.total_amount) > 13000
ORDER BY total_amount_sum DESC;


```

answer : `East Harlem North, East Harlem South, Morningside Heights`