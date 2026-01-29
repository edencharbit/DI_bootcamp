"""
EXERCISE 3: IDENTIFYING DATA TYPES
Description: Categorization of dataset columns into Quantitative vs Qualitative.
Logic:
- Quantitative: Numerical values used for mathematical calculations.
- Qualitative: Categorical values used for grouping or identification.
"""

# ==============================================================================
# 1. DATASET: HOW MUCH SLEEP DO AMERICANS REALLY GET?
# ==============================================================================
sleep_data_types = {
    "index": "Qualitative (ID)",
    "Year": "Quantitative (Discrete)",
    "Period": "Qualitative (Nominal)",
    "Avg hrs per day sleeping": "Quantitative (Continuous)",
    "Standard Error": "Quantitative (Continuous)",
    "Type of Days": "Qualitative (Nominal)",
    "Age Group": "Qualitative (Ordinal)",
    "Activity": "Qualitative (Nominal)",
    "Sex": "Qualitative (Nominal)"
}

# Reasoning:
# 'Avg hrs' is quantitative because we can calculate the average sleep duration.
# 'Age Group' is qualitative because it groups data into pre-defined buckets.

# ==============================================================================
# 2. DATASET: GLOBAL TRENDS IN MENTAL HEALTH DISORDER
# ==============================================================================
mental_health_types = {
    "index": "Qualitative (ID)",
    "Entity": "Qualitative (Nominal)",
    "Code": "Qualitative (Nominal)",
    "Year": "Quantitative (Discrete)",
    "Pathology % columns": "Quantitative (Continuous)"
}

# Reasoning:
# 'Entity' (Country) is a label, whereas the '%' columns are measurements
# of prevalence that allow for global statistical comparisons.

# ==============================================================================
# 3. DATASET: CREDIT CARD APPROVALS (clean_dataset.csv)
# ==============================================================================
credit_card_types = {
    "Gender": "Qualitative (Binary)",
    "Age": "Quantitative (Continuous)",
    "Debt": "Quantitative (Continuous)",
    "Married": "Qualitative (Nominal/Binary)",
    "BankCustomer": "Qualitative (Binary)",
    "Industry": "Qualitative (Nominal)",
    "Ethnicity": "Qualitative (Nominal)",
    "YearsEmployed": "Quantitative (Continuous)",
    "PriorDefault": "Qualitative (Binary)",
    "Employed": "Qualitative (Binary)",
    "CreditScore": "Quantitative (Discrete)",
    "DriversLicense": "Qualitative (Binary)",
    "Citizen": "Qualitative (Nominal)",
    "ZipCode": "Qualitative (Geographic label)",
    "Income": "Quantitative (Continuous)",
    "Approved": "Qualitative (Target Category)"
}

# Reasoning:
# Even though 'Gender' or 'Approved' are 0 or 1, they represent categories.
# 'ZipCode' is numeric but adding two zip codes together is meaningless,
# making it Qualitative. 'Income' and 'Age' are true mathematical quantities.
