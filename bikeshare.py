# US Bikeshare Data Analysis

import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input("Enter the city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        print("Invalid input. Please choose from chicago, new york city, or washington.")

    while True:
        month = input("Enter the month (all, january, february, ..., june): ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        print("Invalid input. Please choose a valid month or 'all'.")

    while True:
        day = input("Enter the day of the week (all, monday, tuesday, ..., sunday): ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        print("Invalid input. Please choose a valid day or 'all'.")

    print('-' * 40)
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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]

    return df

def display_raw_data(df):
    """
    Displays raw data upon user request, 5 lines at a time.
    """
    row_index = 0
    while True:
        raw_data = input("Would you like to see 5 lines of raw data? Enter yes or no: ").lower()
        if raw_data not in ['yes', 'y']:
            break
        print(df.iloc[row_index:row_index + 5])
        row_index += 5
        if row_index >= len(df):
            print("No more data to display.")
            break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print(f"Most common month: {df['month'].mode()[0]}")
    print(f"Most common day of week: {df['day_of_week'].mode()[0]}")
    print(f"Most common start hour: {df['Start Time'].dt.hour.mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print(f"Most commonly used start station: {df['Start Station'].mode()[0]}")
    print(f"Most commonly used end station: {df['End Station'].mode()[0]}")
    df['trip'] = df['Start Station'] + " to " + df['End Station']
    print(f"Most frequent trip: {df['trip'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print(f"Total travel time: {df['Trip Duration'].sum()} seconds")
    print(f"Mean travel time: {df['Trip Duration'].mean()} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print(f"Counts of user types:\n{df['User Type'].value_counts()}")

    if 'Gender' in df:
        print(f"\nCounts of gender:\n{df['Gender'].value_counts()}")
    else:
        print("\nGender data not available.")

    if 'Birth Year' in df:
        print(f"\nEarliest birth year: {int(df['Birth Year'].min())}")
        print(f"Most recent birth year: {int(df['Birth Year'].max())}")
        print(f"Most common birth year: {int(df['Birth Year'].mode()[0])}")
    else:
        print("\nBirth year data not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def main():
    print("Welcome to the US Bikeshare Data Analysis Tool!")

    while True:
        try:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            display_raw_data(df)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

            restart = input('\nWould you like to restart? Enter yes or no (or type "exit" to quit):\n').lower()
            if restart not in ['yes', 'y']:
                print("Thank you for using the US Bikeshare Data Analysis Tool. Goodbye!")
                break
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()
