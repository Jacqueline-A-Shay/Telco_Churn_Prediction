# Telco_Churn_Prediction

# Data acquisition & preparation

1. setup: env.py & use telco_churn dataset
2. Initial observation of data 

customer

contract_type_id	contract_type
1	                Month-to-month
2	                One year
3	                Two year

internet_service_type_id	internet_service_type
1	                        DSL
2	                        Fiber optic
3	                        None

payment_type_id	payment_type
1	              Electronic check
2	              Mailed check
3	              Bank transfer (automatic)
4	              Credit card (automatic)

# Questions to answer

- Could the sign-up month (e.g. specific promo lead to sign-up cohort) relate to customer churn? 
  Is there a cohort or cohorts who have a higher rate of churn than other cohorts? 
  (Plot the rate of churn on a line chart where x is the tenure and y is the rate of churn (customers churned/total     customers))
  
- Are there features that indicate a higher propensity to churn? e.g. internet service, type of phone service, online security and backup, senior citizens, paying more than x% of customers with the same services, etc.?

- Is there a price threshold for specific services where the likelihood of churn increases once price for those services goes past that point? If so, what is that point for what service(s)?

- If we looked at churn rate for month-to-month customers after the 12th month and that of 1-year contract customers after the 12th month, are those rates comparable?

# Model
# Presentation

