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
- Mach,ine Learning Modelling
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

Data Preparation Machine Learning Model
  
* Check for missing values
* Investigate if any unexpected data exist
* Confirm data types, change any if required
* Drop unnecessary columns
* Remove outliers
* Data Statistic (describe())
* Encode categorical features and target
* Split the dataset into training and testing sets

Pair plots to check degree of linearity/no-linearity

![image](https://github.com/HussamGoda/Final-Project/assets/135322159/97ae2386-68ac-41a5-b597-ccd4adc0a510)






Create Logistic Regression Model


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
                                                      
  Sunmary Logisctic regression
 
 Model's accuracy is approximately 70.75%, meaning it correctly predicted the class of roughly 70.75% of the total data points. The logistic regression model performs relatively well in predicting class 1 (case_status_certified) with high precision, recall, and F1-score. However, its performance in predicting class 0 (case_status_denied) is less impressive, with lower precision, recall, and F1-score. This suggests that the model is better at identifying certified cases but struggles with denied cases.
                          
                          
                         
