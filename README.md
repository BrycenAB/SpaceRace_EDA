# Exploritory Data Analysis of all rocket launches up to the year 2020.
---
# Overview

## About the data
* The data is from __[Kaggle/agirlcoding](https://www.kaggle.com/agirlcoding/all-space-missions-from-1957)__
* The data contains information about all space missions from 1957 to 2020
* Columns:
    * Company Name - Name of the company
    * Location - Location of the launch
    * Datum - Date and time of the launch
    * Detail - Rocket name
    * Satus Rocket - Status of the rocket
    * Launch Cost  - Cost of the rocket (original column name is "Rocket")
    * Status Mission - Status of the mission
* Missing values in the data:
    * Company Name - 0
    * Location - 0
    * Datum - 0
    * Detail - 0
    * Satus Rocket - 0
    * Launch Cost  - 3360
    * Status Mission - 0
* Data types:
    * Company Name - String
    * Location - String
    * Datum - String
    * Detail - String
    * Satus Rocket - String
    * Launch Cost  - Float
    * Status Mission - String
 ---
 # Questions/Conclusion

The data was very clean and simple to work with, the only data cleaning necessary was converting the date to datetime format and graph specific alterations.

## How did the rate of launches change over the years?
* When looking at the data there are two peak times of space exploration the first starting in the 60's and dying down a bit in the late 70's.
The second starting in 2016 where launches where doubled that of previous years, this peak  slowed down in 2020 most likely due to the pandemic.

## How many launches per location ?
* The country with the most Launches is Russia with 1395 launches.
* The country with the second most Launches is the USA with 1344 launches.
* The country with the third most Launches is Kazakhstan with 701 launches.
* France, China and Japan are the only other countries with more than 100 launches.

## How many launches per company ?
* The company with the most launches is RVSN USSR with 1777 launches.
* All other companies have less than 300 Launches with Arianespace being the second most with 279 launches.
* Nasa sits in fifth place with 203 launches sitting just behind General Dynamics and CASC.

## What is the success rate of all launches ?
* The success rate of all launches is 89.7%.
* The failure rate of all launches is 7.84%.
* The partial failure rate of all launches is 2.36%.
* The preliminary failure rate of all launches is 0.0925%.

## What is the success rate of all launches per year?
* in the early days of space exploration, the success was significantly lower than it is now and yet it was still bellow 10% of all launches, but as technology improved, the success rate also increased.

## How has the cost of the launches changed over time ?
* The average cost of launches has slowly risen over the years but at a rather slow rate and this is primarily due to some outliers in the data where the cost of the launch is far greater than the average.

## How has the cost of launches changed over time per company ?
* While the average cost of launches has increased slightly over the years, some companies have managed to have a downward trend in cost , this is most likely due to increase in technology and the ability to reuse rockets or pieces of rockets.

