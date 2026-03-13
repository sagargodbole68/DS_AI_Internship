# Phase 1: Understanding the Dataset
This dataset contains customer-level information including demographic attributes and spending behavior.

Each row represents one individual customer.

# Phase 2: Data Cleaning and Preprocessing
The dataset was checked for missing values using `.isnull().sum()`.

Missing values were handled using appropriate methods. In this case, missing values were replaced with 0 for simplicity.


## Age Distribution
The majority of customers fall between 20 and 40 years old.

This suggests that the business primarily attracts young to middle-aged individuals. Marketing strategies may benefit from focusing on digitally active demographics.

## Annual Income Distribution
Most customers are concentrated in the mid-income range.

This indicates a financially stable customer base and presents opportunities for tiered pricing and premium product positioning.

## Gender Distribution
The dataset shows a relatively balanced gender distribution.

This suggests broad market appeal and enables inclusive marketing strategies rather than gender-specific targeting.

## Income vs Spending Score
There is no strong linear relationship between income and spending score.

This suggests that higher income does not necessarily result in higher spending. Behavioral factors may influence purchasing patterns, indicating the need for customer segmentation beyond demographics.

## Age vs Spending Score
Spending behavior varies across age groups, with younger customers showing higher variability.

This suggests younger customers may be more responsive to promotions and trend-driven marketing campaigns.

# Phase 4: Correlation Analysis & Strategic Insights

Executive Summary

1. The customer base is predominantly young adults.
2. Spending behavior is not strongly dependent on income.
3. Customer purchasing patterns are multi-dimensional.
4. The dataset is suitable for segmentation analysis using clustering techniques.

These findings support the potential for data-driven marketing optimization.