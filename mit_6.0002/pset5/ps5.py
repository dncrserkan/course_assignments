# -*- coding: utf-8 -*-
# Problem Set 5: Experimental Analysis

import pylab
import re

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

TRAINING_INTERVAL = range(1961, 2010)
TESTING_INTERVAL = range(2010, 2016)

"""
Begin helper code
"""
class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a 1-d pylab array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return pylab.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]

def se_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.
    
    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by a linear
            regression model
        model: a pylab array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y)**2).sum()
    var_x = ((x - x.mean())**2).sum()
    SE = pylab.sqrt(EE/(len(x)-2)/var_x)
    return SE/model[0]

"""
End helper code
"""

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        degs: a list of degrees of the fitting polynomial

    Returns:
        a list of pylab arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    arrays = []
    for deg in degs:
        arrays.append(pylab.polyfit(x, y, deg))
    return arrays

def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    
    Args:
        y: 1-d pylab array with length N, representing the y-coordinates of the
            N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the R-squared error term
    """
    nom = sum((y - estimated) ** 2)
    mean = y.mean()
    denom = sum((y - mean) ** 2)
    return 1 - (nom / denom)

def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-squared value for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points,
        and SE/slope (if degree of this model is 1 -- see se_over_slope). 


    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    for model in models:
        est = pylab.poly1d(model)
        r2 = r_squared(y, est(x))
        
        pylab.figure(figsize=(8,8))
        pylab.plot(x, y, 'bo', label="Data")
        pylab.plot(x, est(x), 'r', label='Model')
        pylab.legend(loc='best')

        #first degree model "ax + b"
        if len(model) == 2:
            pylab.title(f'Degree of fit: {len(model) - 1}' + f'\nR2 = {r2:.6f}' +
                        f'\nRatio of SE = {se_over_slope(x, y, est(x), model):.6f}')
        else:
            pylab.title(f'Degree of fit: {len(model) - 1}\nR2 = {r2:.6f}')
        
        pylab.xlabel('Years')
        pylab.ylabel('Temperature [°C]')
        # pylab.ylabel('Temperature Deviations [°C]') # for section E
        pylab.show()
        # pylab.savefig(f'{models.index(model):0>3}.png')

def gen_cities_avg(climate, multi_cities, years):
    """
    Compute the average annual temperature over multiple cities.

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to average over (list of str)
        years: the range of years of the yearly averaged temperature (list of
            int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the average annual temperature over the given
        cities for a given year.
    """
    sample_temperatures = []
    for year in years:
        inyear_avg_temps = []
        for city in multi_cities:
            # take average temperature for each city for that year
            inyear_avg_temps.append(climate.get_yearly_temp(city, year).mean())
        # take average temperature for each year
        inyear_avg_temps = pylab.array(inyear_avg_temps)
        sample_temperatures.append(inyear_avg_temps.mean())
    return pylab.array(sample_temperatures)


def moving_average(y, window_length):
    """
    Compute the moving average of y with specified window length.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        window_length: an integer indicating the window length for computing
            moving average

    Returns:
        an 1-d pylab array with the same length as y storing moving average of
        y-coordinates of the N sample points
    """
    averages = []
    for i in range(len(y)):
        fi = max(i - window_length + 1, 0)  # first slice index
        si = i + 1                          # second slice index
        temp = y[fi:si]
        averages.append(sum(temp) / len(temp))
    return pylab.array(averages)

def rmse(y, estimated):
    """
    Calculate the root mean square error term.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the root mean square error term
    """
    nom = sum((y - estimated) ** 2)
    denom = len(y)
    return (nom / denom) ** 0.5
 
def gen_std_devs(climate, multi_cities, years):
    """
    For each year in years, compute the standard deviation over the averaged yearly
    temperatures for each city in multi_cities. 

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to use in our std dev calculation (list of str)
        years: the range of years to calculate standard deviation for (list of int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the standard deviation of the average annual 
        city temperatures for the given cities in a given year.
    """
    std_devs = []
    for year in years:
        year_temperatures = []
        for city in multi_cities:
            year_temperatures.append(climate.get_yearly_temp(city, year))
        year_temperatures = pylab.array(year_temperatures)
        year_temperatures_mean = year_temperatures.mean(axis=0)
        std_devs.append(pylab.std(year_temperatures_mean))
    return pylab.array(std_devs)

def evaluate_models_on_testing(x, y, models):
    """
    For each regression model, compute the RMSE for this model and plot the
    test data along with the model’s estimation.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        RMSE of your model evaluated on the given data points. 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    for model in models:
        est = pylab.poly1d(model)
        RMSE = rmse(y, est(x))
        
        pylab.figure(figsize=(8,8))
        pylab.plot(x, y, 'bo', label='Data')
        pylab.plot(x, est(x), 'r', label='Model')
        pylab.legend(loc='best')
        pylab.title(f'Degree of fit: {len(model) - 1}\nRMSE = {RMSE:.6f}')
        pylab.xlabel('Years')
        pylab.ylabel('Tepmerature [°C]')
        pylab.show()

if __name__ == '__main__':

    climate = Climate("data.csv")
    cities = CITIES
    training_years = pylab.array(TRAINING_INTERVAL)
    testing_years = pylab.array(TESTING_INTERVAL)


    # # Part A.4
    # # A.4 | Section I
    # city, month, day = "NEW YORK", 1, 10
    # degrees = [1]

    # temperatures = []
    # for year in training_years:
    #     temperatures.append(climate.get_daily_temp(city, month, day, year))
    # temperatures = pylab.array(temperatures)

    # models = generate_models(training_years, temperatures, degrees)
    # evaluate_models_on_training(training_years, temperatures, models)
    

    # # A.4 | Section II
    # city = "NEW YORK"
    # degrees = [1]

    # temperatures = []
    # for year in training_years:
    #     temperatures.append(climate.get_yearly_temp(city, year).mean())
    # temperatures = pylab.array(temperatures)

    # models = generate_models(training_years, temperatures, degrees)
    # evaluate_models_on_training(training_years, temperatures, models)
    

    # Part B
    # degrees = [1]

    # temperatures = gen_cities_avg(climate, cities, training_years)
    # models = generate_models(training_years, temperatures, degrees)
    # evaluate_models_on_training(training_years, temperatures, models)


    # Part C
    # degrees = [1]
    # window_length = 5

    # temperatures = gen_cities_avg(climate, cities, training_years)
    # mov_averages = moving_average(temperatures, window_length)
    # models = generate_models(training_years, mov_averages, degrees)
    # evaluate_models_on_training(training_years, mov_averages, models)


    # Part D.2
    # # D.2 | Problem 2
    # degrees = [1]

    # training_temperatures = gen_cities_avg(climate, cities, training_years)
    # training_models = generate_models(training_years, training_temperatures, degrees)
    # testing_temperatures = gen_cities_avg(climate, cities,testing_years)
    # evaluate_models_on_testing(testing_years, testing_temperatures, training_models)


    # # D.2 | Problem 2 - I
    # degrees = [1, 2, 20]
    # window_length = 5

    # training_temperatures = gen_cities_avg(climate, cities, training_years)
    # move_averages = moving_average(training_temperatures, window_length)
    # training_models = generate_models(training_years, move_averages, degrees)
    # evaluate_models_on_training(training_years, move_averages, training_models)
    

    # # D.2 | Problem 2 - II
    # degrees = [1, 2, 20]
    # window_length = 5

    # training_temperatures = gen_cities_avg(climate, cities, training_years)
    # move_averages = moving_average(training_temperatures, window_length)
    # training_models = generate_models(training_years, move_averages, degrees)
    # testing_temperatures = gen_cities_avg(climate, cities, testing_years)
    # testing_move_averages = moving_average(testing_temperatures, window_length)
    # evaluate_models_on_testing(testing_years, testing_move_averages, training_models)


    # Part E
    # window_length = 5
    # degrees = [1]

    # deviations = gen_std_devs(climate, cities, training_years)
    # move_deviations = moving_average(deviations, window_length)
    # deviation_models = generate_models(training_years, move_deviations, degrees)
    # evaluate_models_on_training(training_years, move_deviations, deviation_models)

