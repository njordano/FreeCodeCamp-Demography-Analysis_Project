import pandas as pd

def demography_analyzer(print_data=True):

    # Make the csv into a pandas DF:
    df = pd.read_csv('adult.data.csv')
    
    # How many of each race are represented in this dataset?
    race = df['race'].value_counts()
    
    # What is the average age of men?
    male_mean_age = df.loc[df['sex']=='Male', 'age'.mean()
    
    # people with higher education
    bchlr_prcntg = "{:.3%}".format((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]))
    
    # What is the percentage of people who have a Bachelor's degree?
    skilled_hgh_paid = "{:.3%}".format(
            df[
                (df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & 
                (df['salary'] == '>50K')
            ].shape[0] /
            df[
                df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
            ].shape[0]
    )
    
    # What percentage of people without advanced education make more than 50K?
    unskilled_hgh_paid = "{:.3%}".format(
            df[
                ~(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & 
                (df['salary'] == '>50K')
            ].shape[0] /
            df[
                ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
            ].shape[0]
    )
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_hrs_per_wk = df['hours-per-week'].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hrs_ovr_50k = "{:.3%}".format(
        df[
            (
                df['hours-per-week'] == min_hrs_per_wk) & 
            (df['salary'] == '>50K')
        ].shape[0] /
        df[
            df['hours-per-week'] == min_hrs_per_wk
        ].shape[0]
    )
    
    # What country has the highest percentage of people that earn >50K?
    total_per_country = df['native-country'].value_counts() 
    country_ovr_50K_prctg = (df[
        df['salary'] == '>50K']
        ['native-country'].value_counts().reindex(index=total_per_country.index, fill_value=0) / 
        total_per_country)
    country_hghst_ovr_50K_prctg = f"{country_ovr_50K_prctg.idxmax()} with {country_ovr_50K_prctg.max():.3%}"

     # Identify the most popular occupation for those who earn >50K in India.
    job_high_income_indian = (df[
        (df['native-country']=='India') &
        (df['salary']=='>50K')
        ]['occupation']
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Number of each race:\n", race) 
        print("Average age of men:", male_mean_age)
        print(f"Percentage with Bachelors degrees: {bchlr_prcntg}")
        print(f"Percentage with higher education that earn >50K: {skilled_hgh_paid}")
        print(f"Percentage without higher education that earn >50K: {unskilled_hgh_paid}")
        print(f"Min work time: {min_hrs_per_wk} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {min_hrs_ovr_50k}")
        print("Country with highest percentage of rich:", country_hghst_ovr_50K_prctg)
        print("Top occupations in India:", job_high_income_indian)

    return {
        'race_count': race,
        'average_age_men': male_mean_age,
        'percentage_bachelors': bchlr_prcntg,
        'higher_education_rich': skilled_hgh_paid,
        'lower_education_rich': unskilled_hgh_paid,
        'min_work_hours': min_hrs_per_wk,
        'min_rich_work_hours': min_hrs_ovr_50k,
        'highest_earning_country': country_hghst_ovr_50K_prctg,
        'top_IN_occupation': job_high_income_indian
    }

# test it:
demography_analyzer()