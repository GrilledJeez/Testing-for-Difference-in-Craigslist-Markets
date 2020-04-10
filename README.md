# Testing for Difference in Craigslist Markets
<br><br>
I am investigating the difference in craigslist markets seeking to prove that there is a significant difference between one cities market for a category from others. 

__Abstract:__
I am conducting a Welch T-Test for one city against nine other cities using a Bonferroni correction. The sample data I am testing with has been collected from Craigslist's motorcycles category with a webscraper.

𝐻0 = There is no significant difference in the mean value of motorcycles in the craigslist marketplace between Austin and other cities.

𝐻𝑎 = There is a significant difference in the mean value of motorcycles in the craigslist marketplace between Austin and other cities.

__Results:__
There is a significant difference in the mean value of motorcycles in the craigslist marketplace between one city (Austin) and nine other cities.

See this work as a presentation in [Google Slides](https://docs.google.com/presentation/d/1USBbeBNS2mk7EQKyIUaCc81KVKVgFBys-fNmp1cbIHY/edit?usp=sharing).

# Background and Motivation

For everyone that has used Craigslist, they are faced with a dillemma regarding whether they are getting a fair deal or not. However, almost every item is incredibly unique on Craigslist because they are used, and their is limited market data on the used product since they have been replaced with newer products or discontinued.

I want to resolve this by building a "Kelly Bluebook" for Craigslist where you type in a description for what you are trying to buy or sell, and the system recommending a price within a range. This system would regularly collect information from Craigslist, and use ML and NLP systems to infer a recommended price. It does not have to be correct. It only has to be more correct than any given alternative.

## The First Problem

However, before I embark on building this I have to determine if cities are a variable. I believe they are because every city should have a different market with its own supplies and demands.

## The Solution

I am taking one market that has less product variability from other markets on Craigslist and testing if it's mean price is different from other cities. If it is than I will know that although some cities have similar markets, each city will need to have a tailored recommendation regarding prices if a price recommender is built.

# Hypotheses

𝐻0 = There is no significant difference in the mean value of motorcycles in the craigslist marketplace between Austin and other cities.

𝐻𝑎 = There is a significant difference in the mean value of motorcycles in the craigslist marketplace between Austin and other cities.

# Analysis methods

The tech stack consists of Python 3, Numpy, Pandas, Beautiful Soup, Scipy, Matplotlib, and HTML

Four ```csv``` files, the results of the webscraping, are stored in the ```data``` directory.

```craigslist_motorcycles_8APR2020.csv``` has the cleaned data for ten cities with 964 listings.

To prepare the dataset for analyses:

`import pandas as pd

moto = pd.read_csv('data/craigslist_motorcycles_8APR2020.csv')`

Seperate dataframe by city and store as new variables:

atx_m = moto[moto['city'] == 'Austin']

la_m = moto[moto['city'] == 'Los Angeles']

sf_m = moto[moto['city'] == 'San Francisco']

stl_m = moto[moto['city'] == 'Seattle']

chi_m = moto[moto['city'] == 'Chicago']

den_m = moto[moto['city'] == 'Denver']

pit_m = moto[moto['city'] == 'Pittsburgh']

atl_m = moto[moto['city'] == 'Atlanta']

nyc_m = moto[moto['city'] == 'New York City']

knx_m = moto[moto['city'] == 'Knoxville']

Then store these new variables into a list:

`city_codes = [atx_m, la_m, sf_m, stl_m, chi_m, den_m, pit_m, atl_m, nyc_m, knx_m]`

Now import the following imports and input the function below:

import scipy.stats as stats\
import scipy as sp\
import numpy as np\
import pandas as pd\
import math\
import matplotlib.pyplot as plt\
import matplotlib.pylab as pylab\
%matplotlib inline\
plt.style.use('ggplot')\

def welch_test_and_plot(test_city, city_list):
    for city in city_list:
        print("{} vs {}".format(test_city.iloc[0,5], city.iloc[0,5]))
        test_statistic, p_value = np.round(stats.ttest_ind(test_city['price'], city['price']), 4)
        ss1 = len(test_city['price'])
        ss2 = len(city['price'])
        deg_f = math.floor(
            ((np.var(test_city['price'])/ss1 + np.var(city['price'])/ss2)**(2.00)) / 
            ((np.var(test_city['price'])/ss1)**(2)/(ss1 - 1) + (np.var(city['price'])/ss2)**(2)/(ss2 - 1)))
        x = np.linspace(-5, 5, num=400)
        fig, ax = plt.subplots(1, figsize=(12, 4))
        students = stats.t(deg_f)
        ax.plot(x, students.pdf(x), linewidth=2, label="Degree of Freedom: {:2.0f}"
                .format(deg_f))
        _ = ax.fill_between(x, students.pdf(x), where=(x >= abs(test_statistic)), color="red",
                alpha=0.25, label = "P Value:\
                    {:2.4f}".format(p_value))
        _ = ax.fill_between(x, students.pdf(x), where=(x <= -(abs(test_statistic))), color="red", 
                alpha=0.25)
        ax.axvline(x=test_statistic, linewidth=4, color='r', label = "Test Stat:\
                 {:2.4f}".format(test_statistic), linestyle = '--')
        ax.legend(bbox_to_anchor=(1,1), loc = 'upper left')
        plt.xlabel('x', fontsize = 14, color = 'black')
        plt.ylabel('Probability Density', fontsize = 14, color = 'black')
        ax.set_title("{}-{} Welch Test Results".format(test_city.iloc[1,5], city.iloc[1,5]), fontsize = 20, color = 'black')
        plt.tight_layout()
        plt.show()
        
        
Save your test cities into a new list to call to compare against.

`test_cities = [la_m, sf_m, stl_m, chi_m, den_m, pit_m, atl_m, nyc_m, knx_m]`

Since we will be testing Austin as the main city, you will use atx_m as your 'test_city'.
Run the following and observe your results.

`welch_test_and_plot(atx_m, test_cities)`

Now we must test against each of these with our Bonferroni correction. Input the following function which has the Bonferroni correction formul programmed into it.

`def bonferroni_test(city_1, test_city_list):
    bonferroni = round(.05/len(test_city_list), 4)
    reject_cities = []
    for city in test_city_list:
        test_statistic, p_value = np.round(stats.ttest_ind(city_1['price'], city['price']),4)
        if p_value <= bonferroni:
            reject_cities.append(city.iloc[0,5])
        else:
            continue          
    if len(reject_cities) > 0:
        print("We REJECT the null hypothesis.")
        print("")
        print("There is a significant difference in the mean value of motorcycles")
        print("in the craigslist marketplace between {} and other cities.".format(city_1.iloc[0,5]))
        print("")
        print("{} of our {} p values fell outside our Bonferroni correction.".
              format(len(reject_cities), len(test_city_list)))
        print("")
        print("These cities are significantly different from {}:".format(city_1.iloc[0,5]))
        for _ in reject_cities:
            print(_)
    else:
        print("")
        print("We FAIL TO REJECT the null hypothesis.")
        print("")
        print("There is no significant difference in the mean value of motorcycles")
        print("in the craigslist marketplace between Austin and other cities.")`

Now you are ready to test Austin against your test cities. Run the following code:

`bonferroni_test(atx_m, test_cities)`

# Results

We REJECT the null hypothesis.

There is a significant difference in the mean value of motorcycles
in the craigslist marketplace between Austin and other cities.

4 of our 9 p values fell outside our Bonferroni correction.

These cities are significantly different from Austin:
San Francisco
Chicago
Pittsburgh
New York City


# Future improvements
- Implement a mongo instance with docker where the data will dump once scraped.  
- Clean code with comprehension and consolidating different scripts into functions.
- Expand analyses to collect and test more cities and categories. 


# Acknowledgements

Thanks to Dan Rupp, Peter Galea, Austin Penner, and Juliana Duncan for critical feedback and guidance during the development of this project.