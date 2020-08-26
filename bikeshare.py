import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = { 'january': '1',
                'february': '2',
                'march': '3',
                'april': '4',
                'may': '5',
                'june': '6',
                'all' : '7'
                }

WEEK_DATA = { 'Saturday': '0',
                'Sunday': '1',
                'Monday': '2',
                'Tuesday': '3',
                'Wednesday': '4',
                'Thursday': '5',
                'Friday': '6',
                'all' : '7'
                }

def get_city():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("please enter: \n (1) for chicago \n (2) for new york city \n (3) for washington \n").lower()

    while True:
        while True:     # for handling the unexpected input by user
            if city == '1':
                print("\nYou chose Chicago\n")
                return 'chicago'
            if city == '2':
                print("\nYou chose new york city\n")
                return 'new york city'
            elif city == '3':
                print("\nYou chose washington\n")
                return 'washington'

            else:
                print('\nPlease enter a valid number \n')
                city = input('please enter: \n (1) for chicago \n (2) for new york city \n (3) for washington \n')



    # TO DO: get user input for month (all, january, february, ... , june)
def get_month():
    month= ''
    while month not in MONTH_DATA.values():
        print("\nPlease enter the month, between Jan to jun or all for all the time span:")
        ###Here we enter the number of the month only.
        month = input('Enter a month to filter by: \n 1 for jan \n 2 for feb \n 3 for march \n 4 for april\n 5 for may\n 6 for may\n 7 for all\n')
        ###Handling the input error of the month number.
        if month not in MONTH_DATA.values():
            print("\n no valid input, try again")
    month_keys = list(MONTH_DATA.keys())
    month_values = list(WEEK_DATA.values())
    print(f"\nYou have chosen {month_keys[int(month)-1]}.")
    return month



 # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
def get_day():
    day= ''
    while day not in WEEK_DATA.values():
        print("\nPlease enter the day, between sat to fri or all for all the time span:")
         ###Here we enter the number of the day only.
        day = input('Enter a month to filter by: \n 0 for sat \n 1 for sun \n 2 for mon \n 3 for tue\n 4 for wed\n 5 for thu\n 6 for fri\n 7 for all\n')
           ###Handling the input error of the day number.
        if day not in WEEK_DATA.values():
            print("\n no valid input, try again")
    day_keys = list(WEEK_DATA.keys())
    day_values = list(WEEK_DATA.values())
    print(f"\nYou have chosen {day_keys[int(day)]}.")
    return day_keys[int(day)]


print('-'*40)


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        param1 (str): name of the city to analyze
        param2 (str): name of the month to filter by, or "all" to apply no month filter
        param3 (str): name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df: Pandas DataFrame containing city data filtered by month and day
    """
    #Load data for city
    print("\nCity Data..")
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != '7':
        months = ['1', '2', '3', '4', '5', '6']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_week'] == day.title()]
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)
    # display the most common day of week
    common_day_of_week = df['day_week'].mode()[0]
    print('Most Common Day Of Week:', common_day_of_week)
    # display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', common_start_station)
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', common_end_station)
    # display most frequent combination of start station and end station trip
    group_field = df.groupby(['Start Station','End Station'])
    common_combination_station = group_field.size().sort_values(ascending=False).head(1)
    print('Most common combination of Start Station & End Station trip:\n', common_combination_station)





def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        # Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('Most Common Year:',most_common_birth_year)
        most_recent_birth_year = df['Birth Year'].max()
        print('Most Recent Year:',most_recent_birth_year)
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest Year:',earliest_birth_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def show_raw_data(df):
    data = 0
    while True:
        ans = input("Would you like to see 5 lines of raw data? please enter yes or no \n")
        if ans.lower() == "yes":
            print(df[data :data+5])
            data +=5
        elif ans.lower() == "no":
            break
        else:
            print("\n******please enter yes or no*******\n")


def main():
    while True:
        city = get_city()
        month = get_month()
        day = get_day()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_ask  = show_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
