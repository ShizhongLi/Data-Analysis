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
    while True:
        city = input("Please input the name of the city(chicago, new york city, washington) you want to analyze:")
        if city.lower() in CITY_DATA.keys():
            city = city.lower()
            break
        else:
            print("Your input is invalid, please input one of 'chicago','new york city','washington'.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please input which month(all, january, february, ... , june) you want to analyze:")
        if month.lower() in ['january', 'february', 'march', 'april', 'may', 'june','all']:
            month = month.lower()
            break
        else:
            print("Your input is invalid, please input one of 'all, january, february, ... , june'.\n")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please input which day of week(all, monday, tuesday, ... sunday) you want to analyze:")
        if day.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']:
            day = day.lower()
            break
        else:
            print("Your input is invalid, please input one of 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all'.\n")

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    # print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month_index = df.groupby('month').size().idxmax() - 1
    travel_times_of_most_common_month = df.groupby('month').size().max()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = months[most_common_month_index]
    print("the most common month is {}, with {} times of travel ".format(most_common_month, travel_times_of_most_common_month))

    # TO DO: display the most common day of week
    most_common_week = df.groupby('day_of_week').size().idxmax()
    travel_times_of_most_common_day_of_week = df.groupby('day_of_week').size().max()
    print("the most common day of week is {}, with {} times of travel ".format(most_common_week, travel_times_of_most_common_day_of_week))

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df.groupby('start_hour').size().idxmax()
    travel_times_of_most_common_start_hour = df.groupby('start_hour').size().max()
    print("the most common start hour is {} oclock, with {} times of travel ".format(most_common_start_hour, travel_times_of_most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_used_start_station = df.groupby('Start Station').size().idxmax()
    travel_times_of_most_common_used_start_station = df.groupby('Start Station').size().max()
    print("the most commonly used start station is {}, with {} times of travel ".format(most_common_used_start_station, travel_times_of_most_common_used_start_station))

    # TO DO: display most commonly used end station
    most_common_used_end_station = df.groupby('End Station').size().idxmax()
    travel_times_of_most_common_used_end_station = df.groupby('End Station').size().max()
    print("the most commonly used end station is {}, with {} times of travel ".format(most_common_used_end_station, travel_times_of_most_common_used_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination_of_start_station_and_end_station = df.groupby(['Start Station','End Station']).size().idxmax()
    travel_times_of_most_frequent_combination_of_start_station_and_end_station = df.groupby(['Start Station','End Station']).size().max()
    print("the most frequent combination of start station and end station trip is from {} to {}, with {} times of travel ".format(most_frequent_combination_of_start_station_and_end_station[0], most_frequent_combination_of_start_station_and_end_station[1], travel_times_of_most_frequent_combination_of_start_station_and_end_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('total travel time is {} seconds'.format(total_trip_duration))

    # TO DO: display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()
    print('mean travel time is {} seconds'.format(mean_trip_duration))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usertype_size_df = df.groupby('User Type').size()
    print(usertype_size_df)
    print()
    if usertype_size_df.size == 2:
        print("there are {} {} users and {} {} users.".format(usertype_size_df.values[0], usertype_size_df.index[0], usertype_size_df.values[1], usertype_size_df.index[1]))
    elif usertype_size_df.size == 3:
        print("there are {} {} users, {} {} users and {} {} users.".format(usertype_size_df.values[0], usertype_size_df.index[0], usertype_size_df.values[1], usertype_size_df.index[1], usertype_size_df.values[2], usertype_size_df.index[2]))
    print('\n')
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns.values.tolist():
        gender_size_df = df.groupby('Gender').size()
        print(gender_size_df)
        print()
        print("there are {} {} users and {} {} users.".format(gender_size_df.values[0], gender_size_df.index[0], gender_size_df.values[1], gender_size_df.index[1]))
        print('\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns.values.tolist():
        birth_size_df = df.groupby('Birth Year').size()
        print("earliest year of birth is {}, most recent year of birth is {}, and most common year of birth is {} with {} users born in that year.".format(int(df['Birth Year'].min()), int(df['Birth Year'].max()), int(birth_size_df.idxmax()), birth_size_df.max()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
