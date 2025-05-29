# ===============================================================
# ULTRAMARATHON DATA CLEANING PROJECT
# Dataset: Two Centuries of Ultramarathon Races (7M+ records)
# Goal: Clean and filter the dataset for USA 50km/50mi races in 2020
# Tools: Python, pandas
# ===============================================================

import pandas as pd
import seaborn as sns

# ---------------------------------------------------------------
# STEP 1: Load dataset and configure display settings
# ---------------------------------------------------------------
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)        # Don't wrap lines

df = pd.read_csv(r"D:\School\Power Bi Dashboards\TWO_CENTURIES_OF_UM_RACES.csv")

# Optional: Preview basic info
# print(df.head(10))
# print(df.shape)
# print(df.dtypes)

# ---------------------------------------------------------------
# STEP 2: Filter dataset for 50km or 50mi races in the USA (2020)
# ---------------------------------------------------------------
# Note: Country info is embedded in 'Event name' in the format: "Race Name (Country)"

# Create filtered DataFrame
USAdf = df[
    df['Event distance/length'].isin(['50mi', '50km']) &
    (df['Year of event'] == 2020) &
    (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')
].copy()  # .copy() to avoid SettingWithCopyWarning

# ---------------------------------------------------------------
# STEP 3: Clean and transform data fields
# ---------------------------------------------------------------

# ➤ Clean race name by removing country label (e.g., "(USA)")
USAdf['Event name'] = USAdf['Event name'].str.split('(').str.get(0).str.strip()

# ➤ Engineer athlete age from birth year
USAdf['Athlete_Age'] = 2020 - USAdf['Athlete year of birth']

# ➤ Remove the 'h' from athlete performance time (e.g., "9:15:00 h" → "9:15:00")
USAdf['Athlete performance'] = USAdf['Athlete performance'].str.split(' ').str.get(0)

# ---------------------------------------------------------------
# STEP 4: Drop irrelevant or redundant columns
# ---------------------------------------------------------------
USAdf = USAdf.drop([
    'Athlete club',
    'Athlete country',
    'Athlete age category',
    'Athlete year of birth'
], axis=1)

# ---------------------------------------------------------------
# STEP 5: Handle missing data and duplicates
# ---------------------------------------------------------------

# ➤ Check for missing values in athlete age
# print(USAdf['Athlete_Age'].isna().sum())

# ➤ Drop rows with any missing values
USAdf = USAdf.dropna()

# ➤ Check for and display duplicate rows
# print(USAdf[USAdf.duplicated()])

# ---------------------------------------------------------------
# STEP 6: Reset index and convert data types
# ---------------------------------------------------------------
USAdf.reset_index(drop=True, inplace=True)

# ➤ Convert athlete age to integer, average speed to float
USAdf['Athlete_Age'] = USAdf['Athlete_Age'].astype(int)
USAdf['Athlete average speed'] = USAdf['Athlete average speed'].astype(float)

# ---------------------------------------------------------------
# STEP 7: Rename columns for readability and consistency
# ---------------------------------------------------------------
USAdf = USAdf.rename(columns={
    'Year of event': 'year',
    'Event dates': 'race date',
    'Event name': 'race name',
    'Event distance/length': 'race length',
    'Event number of finishers': 'total finishers',
    'Athlete performance': 'athlete performance',
    'Athlete gender': 'athlete gender',
    'Athlete average speed': 'athlete average speed',
    'Athlete ID': 'athlete ID',
    'Athlete_Age': 'athlete age'
})

# ---------------------------------------------------------------
# STEP 8: Preview cleaned dataset
# ---------------------------------------------------------------
print(USAdf.head(10))

# ---------------------------------------------------------------
# STEP 9: Save cleaned dataset to CSV
# ---------------------------------------------------------------
USAdf.to_csv("cleaned_ultra_races_USA_2020.csv", index=False)
