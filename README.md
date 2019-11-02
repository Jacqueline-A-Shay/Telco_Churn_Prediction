# Telco_Churn_Prediction

# Data acquisition & preparation

1. setup: env.py & use Codeup telco_churn dataset
2. Initial observation of data 

# Important finding:
1. Logistic regression algorithm provided a more balanced accuracy and recall rate (rather than false predict churn than not catching)

2. Within the highest churning customer population - month to month (no contract), identified a correlation between longer average tenure and customers with:
> paperless-billing (avg of 5 months longer tenure)
>
> auto payment (credit card or bank transfer) (avg of 11 months longer tenure)

**May want to promote these two features more to non-contract customers due to the observed longer tenure, at NO COST for our company.**



# Questions to answer

- Could the sign-up month (e.g. specific promo lead to sign-up cohort) relate to customer churn? 
  Is there a cohort or cohorts who have a higher rate of churn than other cohorts? 
  (Plot the rate of churn on a line chart where x is the tenure and y is the rate of churn (customers churned/total     customers))
  
- Are there features that indicate a higher propensity to churn? e.g. internet service, type of phone service, online security and backup, senior citizens, paying more than x% of customers with the same services, etc.?

- Is there a price threshold for specific services where the likelihood of churn increases once price for those services goes past that point? If so, what is that point for what service(s)?

- If we looked at churn rate for month-to-month customers after the 12th month and that of 1-year contract customers after the 12th month, are those rates comparable?

# Model
Logistic regression algorithm 
Features selected using chi-square test, t-test and/ or correlation.

# Presentation
https://docs.google.com/presentation/d/1H5qk9D169Xa-h6PV36BCKWZC3C6Cgfi3a8V4QAKwGRU/edit#slide=id.gc6f9e470d_0_0

