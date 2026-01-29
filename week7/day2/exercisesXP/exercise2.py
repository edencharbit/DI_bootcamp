import pandas as pd

# ==============================================================================
# 1. DATASET: HOW MUCH SLEEP DO AMERICANS REALLY GET?
# Path: 'Time Americans Spend Sleeping.csv'
# ------------------------------------------------------------------------------
# Description:
# Surveys the sleeping habits of Americans from 2003 to 2017.
#
# Key Columns:
# - Year: Survey year (2003-2017)
# - Avg hrs per day sleeping: Target numerical value
# - Type of Days: All days, Weekdays, or Weekends/Holidays
# - Age Group: Demographic segments (e.g., '15 years and over')
# ==============================================================================
sleep_df = pd.read_csv('Time Americans Spend Sleeping.csv')
print("--- Sleep Data Sample ---")
print(sleep_df.head(), "\n")


# ==============================================================================
# 2. DATASET: GLOBAL TRENDS IN MENTAL HEALTH DISORDER
# Path: 'Mental health Depression disorder Data.csv'
# ------------------------------------------------------------------------------
# Description:
# Global prevalence rates of various mental health conditions by country and year.
#
# Key Columns:
# - Entity: Country or Region name
# - Code: ISO Country Code
# - Schizophrenia to Alcohol use disorders (%): Prevalence rates
# ==============================================================================
mental_health_df = pd.read_csv('Mental health Depression disorder Data.csv')
print("--- Mental Health Data Sample ---")
print(mental_health_df.head(), "\n")


# ==============================================================================
# 3. DATASET: CREDIT CARD APPROVALS
# Path: 'clean_dataset.csv' (Pre-processed version of crx.csv)
# ------------------------------------------------------------------------------
# Description:
# A cleaned dataset used for binary classification. Predicts whether a credit
# card application will be approved based on applicant's financial profile.
#
# Key Columns:
# - Debt / Income: Numerical financial indicators
# - PriorDefault: Categorical (1 if the user had a default before)
# - Approved: TARGET (1 = Yes, 0 = No)
# ==============================================================================
credit_card_df = pd.read_csv('clean_dataset.csv')
print("--- Credit Card Data Sample ---")
print(credit_card_df.head())