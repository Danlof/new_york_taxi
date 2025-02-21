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