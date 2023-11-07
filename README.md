# Final-Project


**US Working Visa Applications Status**
**Visualization and Prediction**
-
**Contributors:**  Hussam Goda, Kashif Bashir, Yoshie Hara

![Image](https://github.com/HussamGoda/Final-Project/blob/main/Images/Approve.png)


**Introduction and Overview:**
-
In this project, a dataset of US working visa status is considered. The dataset contains 25480 records and a total of 12 columns, summarized as follows.
- Case id: unique ID for each application,
- Continent: Applicant location (categorical feature),
- Education of Employee: applicant level of education (categorical feature),
- Job Experience: whether the job requires prior experience (categorical feature),
- Job Training: whether the job involves initial training (categorical feature),
- Number of Employees: company size (numerical feature)
- Year of Establishment: the year the company was established (numerical feature)
- Region of Employment: US region where the company is located (categorical feature),
- Prevailing Wage: salary on offer (numerical feature)
- Unit of wage: yearly, weekly, monthly (categorical feature)
- Full-Time Position: whether the position is full-time or not (categorical feature)
- Case status: whether the case is certified or denied (categorical target)


The goal of this project is two-fold.
- Understand the visa award program and factors that may influence the final decision, using data analysis and visualizations in Tableau.
- Develop machine learning models that predict the status of visa application results, with the aim to provide valuable insights for both applicants and immigration authorities, contributing to more efficient and informed decision-making


Data Source: https://www.kaggle.com/datasets/moro23/easyvisa-dataset


**Data Preparation**
-
Before starting the analysis, Several steps were taken to ensure the data was cleaned and processed.
•	Check and drop any missing values
•	Investigate if any unexpected data exist, for example in the number of employees column, some values were reported as negative values. It was assumed that this happened by mistake. The values were then converted to positive values
•	Confirm data types, and change any if required
•	Drop unnecessary columns such as case_id column
•	Remove outliers: using quantile (0.25, 0.5, 0.75), lower bond, and upper bond to remove outliers from the original data
•	Data Statistic (describe())
•	Encode categorical features and target (as indicated above)
•	Split the dataset into training and testing sets for machine learning modeling.


It should be noted that in this study only records that show “unit of wage” as year are used in the study. Final number of records is 18430.


**Step 1: Data Analysis and Visualization:**
-
This project also involved preforming an exploratory analysis on the dataset in order to gain a better understanding of general themes associated with US visa approvals. 
Tableau Link: https://public.tableau.com/app/profile/yoshie.hara/viz/Project4/Story1


#Observations#

  [Total Study]  
  - The total study is an overarching analysis that provides a comprehensive view of the dataset.
<img src="https://github.com/HussamGoda/Final-Project/blob/main/Images/Total.png" width="400" alt="Total Study">


  [Study of Continent of Origin]  
  - The most Applications from Asia
  - Among different continents, Europe has the highest work visa certification rate (81%).
  - The lowest work visa certification rate belongs to South America (64%).  
<img src="https://github.com/HussamGoda/Final-Project/blob/main/Images/Continent.png" width="400" alt="Continent">

  [Study of Education]
  - It is clear that the higher the education level of applicants is, the more their chances of visa certification are.  
<img src="https://github.com/HussamGoda/Final-Project/blob/main/Images/Education.png" width="400" alt="Education">  


  [Study of Region of Employer]
  - It appears that the visa applications filed by the employers within the Midwest region have the highest probability (77%) of certification.
  - The employers located in the Northeast, West, and Island regions have lower chances (61%) of visa certification.  
<img src="https://github.com/HussamGoda/Final-Project/blob/main/Images/Region.png" width="400" alt="Region">


  
  [Study of Wages]
  - The data highlights a predominant salary range of 40k to 80k among visa applicants, and it shows higher incomes don't consistently result in higher approval rates.
  - Intriguingly, the analysis demonstrates a correlation between education levels and income expectations, with more highly educated candidates often seeking higher salaries.
<img src="https://github.com/HussamGoda/Final-Project/blob/main/Images/Wage1.png" width="400" alt="Wage1">
<img src="https://github.com/HussamGoda/Final-Project/blob/main/Images/Wage2.png" width="400" alt="Wage2">

Data Preparation Machine Learning Model:
  
* Check for missing values
* Investigate if any unexpected data exist
* Confirm data types, change any if required
* Drop unnecessary columns
* Remove outliers
* Data Statistic (describe())
* Encode categorical features and target
* Split the dataset into training and testing sets

Pair plots to check the degree of linearity/no-linearity

![image](https://github.com/HussamGoda/Final-Project/assets/135322159/97ae2386-68ac-41a5-b597-ccd4adc0a510)






Create Logistic Regression Model:


  Accuracy: 0.7074652777777778

  
              precision    recall  f1-score   support

           0       0.53      0.31      0.39      1398
           1       0.75      0.88      0.81      3210
    accuracy                           0.71      4608
   macro avg       0.64      0.60      0.60      4608
weighted avg       0.68      0.71      0.68      4608


Confusion Matrix:

 [[ 435  963]
 [ 385 2825]]
                                                      
  Summary Logistic Regression:
 
 The model's accuracy is approximately 70.75%, meaning it correctly predicted the class of roughly 70.75% of the total data points. The logistic regression model performs relatively well in predicting class 1 (case_status_certified) with high precision, recall, and F1-score. However, its performance in predicting class 0 (case_status_denied) is less impressive, with lower precision, recall, and F1-score. This suggests that the model is better at identifying certified cases but struggles with denied cases.
                          
                          
                         
