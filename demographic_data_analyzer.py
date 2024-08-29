import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # Question 1
    race_count = df['race'].value_counts()

    # Question 2
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # Question 3
    percentage_bachelors = (df['education'].value_counts(normalize=True)['Bachelors'] * 100)

    # Question 4
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # Advanced education making >50K
    higher_education_rich = (df[higher_education & (df['salary'] == '>50K')].shape[0] / df[higher_education].shape[0]) * 100

    # Non-advanced education making >50K
    lower_education_rich = (df[lower_education & (df['salary'] == '>50K')].shape[0] / df[lower_education].shape[0]) * 100

    # Question 6
    min_work_hours = df['hours-per-week'].min()

    # Question 7
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]
    rich_percentage = (df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0] / num_min_workers) * 100

    # Question 8
    country_salary_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_counts = df['native-country'].value_counts()
    highest_earning_country = (country_salary_counts / country_counts * 100).idxmax()
    highest_earning_country_percentage = (country_salary_counts / country_counts * 100).max()

    # Question 9
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
