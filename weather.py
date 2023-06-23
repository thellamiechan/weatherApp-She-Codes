import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    date_object = datetime.fromisoformat(iso_string)
    human_readable_date = date_object.strftime("%A %d %B %Y")
    return human_readable_date



    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """


def convert_f_to_c(temp_in_farenheit):
    celc = (float(temp_in_farenheit)-32.0)
    celc = celc * (5/9)
    celcius = round(celc, 1)
    return float(celcius)
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """


def calculate_mean(weather_data):
    total = 0
    for i in weather_data:
        total = total + float(i)
    return float(total)/len(weather_data)

    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """


def load_data_from_csv(csv_file):
    new_list = []
    with open(csv_file) as csv_data:
        next(csv_data)
        reader = csv.reader(csv_data)
        for line in reader:
            if line != []:
                integers = [int(value) if len(value) < 4 else value for value in line]
                new_list.append(integers)
    return new_list
   

    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass


def find_min(weather_data):
    if len(weather_data) != 0:
        min_val = weather_data[0]
        min_ind = 0
        for index, temp in enumerate(weather_data):
            if float(temp) <= float(min_val): 
                min_val = float(temp) 
                min_ind = index
        return float(min_val), min_ind
    return ()
    
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
     


def find_max(weather_data):
    if weather_data:
        max_val = weather_data[0]
        max_ind = 0
        for index, temp in enumerate(weather_data):
            if float(temp) >= float(max_val):
                max_val = float(temp)
                max_ind = index
        return float(max_val), max_ind
    return ()
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):
    dates = []
    min_vals = []
    max_vals = []
    for line in weather_data:
        dates.append(line[0]) 
        min_vals.append(line[1])
        max_vals.append(line[2])
    day = len(dates)
    min_val, min_ind = find_min(min_vals)
    # print(min_vals)
    min_date = dates[min_ind]
     
    max_val, max_ind = find_max(max_vals)
    max_date = dates[max_ind]
    
    mean_low = calculate_mean(min_vals)

    mean_high = calculate_mean(max_vals)
    
    summary = f"{day} Day Overview\n  The lowest temperature will be {format_temperature(convert_f_to_c(min_val))}, and will occur on {convert_date(min_date)}.\n  The highest temperature will be {format_temperature(convert_f_to_c(max_val))}, and will occur on {convert_date(max_date)}.\n  The average low this week is {format_temperature(convert_f_to_c(mean_low))}.\n  The average high this week is {format_temperature(convert_f_to_c(mean_high))}.\n"

    return summary
    
    


    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    


def generate_daily_summary(weather_data):
    output = ""
    for line in weather_data:
        date = convert_date(line[0])
        temp = format_temperature(convert_f_to_c(line[1]))
        temp1 = format_temperature(convert_f_to_c(line[2]))
        output += f'---- {date} ----\n  Minimum Temperature: {temp}\n  Maximum Temperature: {temp1}\n\n'
    return output
        
    

    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
