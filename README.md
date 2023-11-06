# Final-Project


**US Working Visa Applications Status**
**Visualization and Prediction**
-
**Contributers:**  Hussam Goda, Kashif Bashir, Yoshie Hara

![Image](https://github.com/HussamGoda/Final-Project/blob/main/Images/Approve.png)


**Agenda:** 
-
- Introduction and Overview
- Data Analysis and Visualization
  1.Tableau Visualizations
  2.General Observations
- Machine Learning Modelling
  1.Data Preparation
  2.Logistic Regression
  3.Artificial Neural Network
    a.Traditional Modelling
    b.Cross Validation Modelling
    c.Model Deployment
- Conclusions

**Introduction and Overview:**
-
- The goal of this project is to develop a machine learning model that predicts the case status of visa applications, the aims to to provide valuable insights for both applicants and immigration authorities, contributing to more efficient and informed decision-making.
- Data Sources: https://www.kaggle.com/datasets/moro23/easyvisa-dataset


**Step 1: Data Analysis and Visualization:**
-
This project also involved preforming an exploratory analysis on the dataset in order to gain a better understanding of general themes associated with US visa approvals. 
Tableau Link: https://public.tableau.com/app/profile/yoshie.hara/viz/Project4/Story1


#Observations#

  [Total Study]  
  - The total study is an overarching analysis that provides a comprehensive view of the dataset.
<img src="https://github.com/HussamGoda/Final-Project/blob/main/Images/Total.png" width="400" alt="Total Study">


  [Study of Continent of Origin]  
  - The most Application from Asia
  - Among different continents, Europe has the highest work visa certification rate (81%).
  - The lowest work visa certification rate belongs to South America (64%).  
<img src="https://github.com/HussamGoda/Final-Project/blob/main/Images/Continent.png" width="400" alt="Continent">

  [Study of Education]
  - It is clear that the higher the education level of an applicants is, the more their chances of visa certification are.  
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

                        ******DATA PREPARATION Machine Learning Model**************
    
* Data Loading: (Imported the dataset from 'easy_visa_cleaned_NoOutliers (2).csv)
* Initial Data Exploration: (Removed the "case_id" and "unit_of_wage" columns to clean the dataset.)
* Data Information: ( use the info() method to generate a summary of statistics
* Data Summary Statistics:(Utilized the describe(Include=‘all’ method to obtain summary statistics for the dataset, including count, unique values, and more.
* Categorical Data Conversion: Converted categorical data to numeric using one-hot encoding with ‘pd.get_dummies’. 
* Specified the columns to be converted: ['continent', 'education_of_employee', 'has_job_experience', 'requires_job_training', 'region_of_employment', 'full_time_position', 'case_status’].
* Column Removal: (Removed the "case_status_Denied" column from "easy_visa_df" to create a modified DataFrame)
* Data Types and Completeness Check:(used ‘info()’ to understand the structure of the DataFrame and assess data types and completeness.
* Data Visualization: (Visualized relationships and patterns in the data, specifically in the context of certified and non-certified case statuses)
* Plotted a pairplot using Seaborn to explore the relationships between 'no_of_employees,' 'yr_of_estab,' and 'prevailing_wage' with respect to 'case_status_Certified.'
* Data Splitting: (Split the preprocessed data into features (X) and the target variable (y). Split the data into training and testing datasets using ‘train_test_split
* Create a logistic regression model
* create a Support Vector Machine (SVM) classifier
* Create Artificial Neural Network Model –(Traditional Modeling)
* Create Artificail Neural Networl Model- ( cross validation Modelling)
* Artificial Neural Network (Model Deployment)
                               ** Create Logistic Regression Model**
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
 **Sunmary:**
 Model's accuracy is approximately 70.75%, meaning it correctly predicted the class of roughly 70.75% of the total data points. The logistic regression model performs relatively well in predicting class 1 (case_status_certified) with high precision, recall, and F1-score. However, its performance in predicting class 0 (case_status_denied) is less impressive, with lower precision, recall, and F1-score. This suggests that the model is better at identifying certified cases but struggles with denied cases.
                          **SVM Classifier Model******

Accuracy: 0.6966145833333334
Classification Report:
               precision    recall  f1-score   support

           0       0.50      0.01      0.02      1398
           1       0.70      1.00      0.82      3210

    accuracy                           0.70      4608
   macro avg       0.60      0.50      0.42      4608
weighted avg       0.64      0.70      0.58      4608
 
 **Sunmary:**
 SVM classifier Model appears to perform well in predicting class "1" (case_status_certified) with high precision and recall. However, its performance for class "0" (case_status_denied) is quite poor, with low precision and recall. It seems that the model struggles to correctly identify denied cases.

