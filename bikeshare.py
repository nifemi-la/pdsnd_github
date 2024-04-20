import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please Choose one of these Cities: (chicago, new york city or washington): ").lower()
    
    cities = ['chicago', 'new york city', 'washington']
   # Accounting for error caused by it not being one of the options
    while city not in cities:
        city = input('Sorry, that is not an option.\nPlease choose a city between chicago, new york city or washington: ')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please choose a month (all, january, february, ... , june): ').lower()
   
    # accounting for errors 
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in months:
         month = input("Sorry that's not a valid option.\n Please choose another month (all, january, february, ... , june): ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('Please choose a day (all, monday, tuesday, ... sunday): ').lower()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load file to dataframe 
    df = pd.read_csv(CITY_DATA[city])
                
    #convert the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
     
     # Extract the month and day of week from 'Start Time'
    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.weekday_name
                
    #filtering by month 
    if month != 'all':
        month_num = pd.to_datetime(month, format='%B').month
        df = df[df['Start Time'].dt.month == month_num]
                            
    #Filtering by week day 
    if day != 'all':
        df = df[df['Start Time'].dt.day_name() == day.title()]
         
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].value_counts().idxmax()
    print('The most common month is:', popular_month) 

    # TO DO: display the most common day of week
    popular_weekday = df['week_day'].value_counts().idxmax()
    print('The most common day of week is:', popular_weekday)

    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    
    # Convert to AM/PM format
    am_pm = 'AM' if popular_hour < 12 else 'PM'
    if popular_hour > 12:
        popular_hour -= 12
    print('The most common start hour is:', popular_hour, am_pm)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print("The most common start station is:", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print("The most common end station is ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + " to " + df['End Station']
    common_trip = df['Trip'].value_counts().idxmax()
    print("The most common trip from start to end:", common_trip)
                
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration_seconds = df['Trip Duration'].sum() 
    total_duration_hours = total_duration_seconds // 3600
    total_duration_minutes = (total_duration_seconds % 3600) // 60
    total_duration_seconds = total_duration_seconds % 60
    print(f"The Total Travel Time is {total_duration_hours} Hours, {total_duration_minutes} Minutes, and {total_duration_seconds} Seconds.")

    # TO DO: display mean travel time
    mean_duration_seconds = df['Trip Duration'].mean()
    mean_duration_hours = mean_duration_seconds // 3600
    mean_duration_minutes = (mean_duration_seconds % 3600) // 60
    mean_duration_seconds = mean_duration_seconds % 60
    print(f"The average travel time is {mean_duration_hours} Hours, {mean_duration_minutes} Minutes, and {mean_duration_seconds} Seconds.")
                
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of User Types are:", user_types)

    # TO DO: Display counts of gender
    try:
        user_gender = df['User Type'].value_counts()
        print("The count of User Types are:", user_gender)
    except KeyError:
        print("\nGender Types:\nNo data available for gender.")

     # TO DO: Display earliest, most recent, and most common year of birth
    
    try:  #Earliest birth year
        earliest_birth_year = df['Birth Year'].min()
        print('\nEarliest Year:', earliest_birth_year)
    except KeyError:
        print("\nEarliest Year:\nNo data available for this month.")
        
    try: #Recent birth Year
        most_recent_birth_year = df['Birth Year'].max()
        print('\nMost Recent Year:', most_recent_birth_year)
    except KeyError:
        print("\nMost Recent Year:\nNo data available for this month.")
        
    try: #Most Common Birth Year 
        most_common_birth_year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', most_common_birth_year)
    except KeyError:
        print("\nMost Common Year:\nNo data available for this month.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def individual_data(df):
    # Display individual trip data in batches of 5 rows
    start_data = 0
    end_data = 5
    df_length = len(df)
    
    while start_data < df_length:
        raw_data = input("\nWould you like to see individual trip data? Enter 'yes' or 'no'.\n")
        if raw_data.lower() == 'yes':
            print("\nDisplaying the next 5 rows of data:\n")
            print(df.iloc[start_data:end_data])
            start_data += 5
            end_data += 5
        else:
            break

            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
