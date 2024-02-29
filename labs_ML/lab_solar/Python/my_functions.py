import pandas as pd

def filter_number(df):
    numeric_columns = input_df.select_dtypes(include=['int', 'float'])
    
    numeric_df = input_df[numeric_columns.columns]
    
    return numeric_df


def format_dates(df):
    df['Data'] = pd.to_datetime(df['Data'], format='%m/%d/%Y %I:%M:%S %p')
    df['TimeSunRise'] = pd.to_datetime(df['TimeSunRise'], format='%H:%M:%S')
    df['TimeSunSet'] = pd.to_datetime(df['TimeSunSet'], format='%H:%M:%S')
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')
    return df


def format_dates_2(df):
    df['Date'] = pd.to_datetime(df['Date'])  
    df['Time'] = pd.to_datetime(df['Time']).dt.time 
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['Hour'] = df['Time'].apply(lambda x: x.hour)
    df['Minute'] = df['Time'].apply(lambda x: x.minute)

    return df

import pandas as pd

def format_dates_3(df):
    datetime_columns = ['Data', 'TimeSunRise', 'TimeSunSet', 'Time']

    for column in datetime_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(df[column])

    if 'Data' in datetime_columns:
        df['Year'] = df['Data'].dt.year
        df['Month'] = df['Data'].dt.month
        df['Day'] = df['Data'].dt.day
    if 'TimeSunRise' in datetime_columns:
        df['Sunrise_Hour'] = df['TimeSunRise'].dt.hour
        df['Sunrise_Minute'] = df['TimeSunRise'].dt.minute
    if 'TimeSunSet' in datetime_columns:
        df['Sunset_Hour'] = df['TimeSunSet'].dt.hour
        df['Sunset_Minute'] = df['TimeSunSet'].dt.minute
    if 'Time' in datetime_columns:
        df['Hour'] = df['Time'].dt.hour
        df['Minute'] = df['Time'].dt.minute

    return df




def process_date(df):
    df['Data'] = pd.to_datetime(df['Data'])
    df['day'] = df['Data'].dt.day.astype(int)  
    df['month'] = df['Data'].dt.month.map({1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'})
    df = df.drop(columns=['Data'])  
    return df

import pandas as pd

def process_time_columns(df):
    # Process TimeSunRise
    df['TimeSunRise'] = pd.to_timedelta(df['TimeSunRise'])
    df['TotalSecondsSunRise'] = df['TimeSunRise'].dt.total_seconds()
    df = df.drop(columns=['TimeSunRise'])  # Remove the original 'TimeSunRise' column
    
    # Process TimeSunSet
    df['TimeSunSet'] = pd.to_timedelta(df['TimeSunSet'])
    df['TotalSecondsSunSet'] = df['TimeSunSet'].dt.total_seconds()
    df = df.drop(columns=['TimeSunSet'])  # Remove the original 'TimeSunSet' column
    
    # Process time
    df['Time'] = pd.to_timedelta(df['Time'])
    df['TotalSecondsTime'] = df['Time'].dt.total_seconds()
    df = df.drop(columns=['Time'])  # Remove the original 'time' column
    
    return df