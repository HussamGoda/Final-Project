# Final-Project


**US Working Visa Applications Status**
**Visualization and Prediction**
-
**Contributors:**  Hussam Goda, Kashif Bashir, Yoshie Hara

![Image](https://github.com/HussamGoda/Final-Project/blob/main/Images/Approve.png)




**Repo Files**
-
CSV files
- "EasyVisa.csv" : Original dataset
- "easy_visa_cleaned_NoOutliers.csv": final CSV file for Machine Learning
- "map.csv": final CSV file to be used in Tableau (contains approximate values for latitude and longitude for different regions in the US) 

Jupyter Notebook Files:
- "easy_visa_cleaning.ipynb": code used to investigate, clean, and analyze the dataset
- "easy_visa_cleaned_NoOutliers(export_for_map).ipynp": code used to add latitude and longitude to the data to facilitate the use of map in Tableau
- "easy_visa_logistic_regression.ipynb": code used for Machine learning (Logistic Regression)
- "withStandardScale_200epchs.ipynb": Code for Machine Learning (Neural Network)

files and folders for Deployment 
- folder "SS_runs": contains files saved (using pickle) from the cross-validation runs.  
- Folder “templates”: contains the file “index.html”
- "Visa_xv_model.py": code for defining Python flask, performing calculations, and returning output to the front end.

If you require to run any code, please maintain the files' relative locations as shown in the Repo. 





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

- Check and drop any missing values
- Investigate if any unexpected data exist, for example in the number of employees column, some values were reported as negative values. It was assumed that this happened by mistake. The values were then converted to positive values
- Confirm data types, and change any if required
- Drop unnecessary columns such as case_id column
- Remove outliers: using quantile (0.25, 0.5, 0.75), lower bond, and upper bond to remove outliers from the original data
- Data Statistic (describe())
- Encode categorical features and target (as indicated above)
- Split the dataset into training and testing sets for machine learning modeling.


It should be noted that in this study only records that show “unit of wage” as year are used in the study. Final number of records is 18430.


**Data Analysis and Visualization:**
-
As indicated earlier, the project involves performing an exploratory analysis of the dataset in order to gain a better understanding of general themes associated with US visa approvals. 
Before starting the analysis, python code was written to add approximate values of latitude and longitude for each region in the US. This would facilitate the use of the US map for some visualizations.

Tableau Link: [https://public.tableau.com/app/profile/yoshie.hara/viz/Project4/Story1]


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
  - It appears that the visa applications filed by employers within the Midwest region have the highest probability (77%) of certification.
  - The employers located in the Northeast, West, and Island regions have lower chances (61%) of visa certification.  
<img src="https://github.com/HussamGoda/Final-Project/blob/main/Images/Region.png" width="400" alt="Region">


  
  [Study of Wages]
  - The data highlights a predominant salary range of 40k to 80k among visa applicants, and it shows higher incomes don't consistently result in higher approval rates.
  - Intriguingly, the analysis demonstrates a correlation between education levels and income expectations, with more highly educated candidates often seeking higher salaries.
<img src="https://github.com/HussamGoda/Final-Project/blob/main/Images/Wage1.png" width="400" alt="Wage1">
<img src="https://github.com/HussamGoda/Final-Project/blob/main/Images/Wage2.png" width="400" alt="Wage2">

**Machine Learning Models**
-
In this part of the report, Machine Learning modeling is summarised. 

Initially, Pair Plots were created to investigate relationships between features and understand the degree of linearity/no-linearity that may exist.
The plot below shows a total of 9 sub-plots, 6 of which are scatter plots. such plots show the relationship between two numerical features for each case status (orange circles for "Certified" status and blue circles for "Denied" status). Looking at the plots, one may conclude that non-linearity dictates relationships between the input features.

The remaining plots (3 plots) show the distribution of each numerical feature for each visa status. The "prevailing wage" appears to be normally distributed (relatively speaking). The distributions of "no_of_employees" and "yr_of_estab" are skewed to the left and the right respectively.



![image](https://github.com/HussamGoda/Final-Project/assets/135322159/97ae2386-68ac-41a5-b597-ccd4adc0a510)

Machine Learning models use a total of 24 Input features (following transforming categorical features numerical features containing only 0 and 1)
- no_of_employees
- yr_of_estab
- prevailing_wage
- continent_Africa
- continent_Asia
- continent_Europe
- continent_North America
- continent_Oceania
- continent_South America
- education_of_employee_Bachelor's
- education_of_employee_Doctorate
- education_of_employee_High School
- education_of_employee_Master's
- has_job_experience_N
- has_job_experience_Y
- requires_job_training_N
- requires_job_training_Y
- region_of_employment_Island
- region_of_employment_Midwest
- region_of_employment_Northeast
- region_of_employment_South
- region_of_employment_West
- full_time_position_N
- full_time_position_Y

The original output target is case_status. Like other categorical columns, this column was split into case_status_Certified and case_status_denied. Only one column is sufficient as it presents both statuses; "Certified" and Denied".

Output target:
- case_status_Certified


****Logistic Regression Model****
-

Accuracy: 0.707

  
              precision    recall  f1-score   support

           0       0.53      0.31      0.39      1398
           1       0.75      0.88      0.81      3210
    accuracy                           0.71      4608
   macro avg       0.64      0.60      0.60      4608
weighted avg       0.68      0.71      0.68      4608


Confusion Matrix:

 [[ 435  963]
 [ 385 2825]]
                                                      
The model's accuracy is approximately 70.75%, meaning it correctly predicted the class of roughly 70.75% of the total data points. The logistic regression model performs relatively well in predicting class 1 (case_status_certified) with high precision, recall, and F1-score. However, its performance in predicting class 0 (case_status_denied) is less impressive, with lower precision, recall, and F1-score. This suggests that the model is better at identifying certified cases but struggles with denied cases.


****Neural Network - Single Model****
-

The dataset was split into two datasets, training and testing. Both datasets were standardized and transformed.
Following a number of trials the following neural network structure was used.
- An input layer (24 neurons),
- First hidden layer with 80 neurons
- Second hidden layer with 50 neurons
- Activation function set as sigmoid in each layer for all neurons.
- maximum of 200 epochs

following the training process, the network was tested using the testing dataset giving the following Classification Report

![image](https://github.com/HussamGoda/Final-Project/assets/134576485/6636aacd-8fc1-4051-8ce4-67f696d6a972)

The model seems able to predict the case status "Certified" (presented by 1) better than "Denied" (presented by 0). Precision and recall values for "Certified" are 78% and 85% respectively. The model accuracy is 0.73. The performance of the model appears to be similar to the logistic regression model shown above. Since the logistic regression model is simpler than the neural network model, it makes sense to deploy the logistic regression model. However, before approving that, the decision was made to, first, investigate whether training the neural network model using Cross Validation would improve its performance.

Before starting the Cross-validation modeling, it might be a good idea to have a quick look at the input features relative importance in the neural network model. One easy way of doing such an activity is by collecting the weight values for each input feature and summing them (weights going into the first hidden layer). Input features with higher weight may be considered more important.

![image](https://github.com/HussamGoda/Final-Project/assets/134576485/15e54271-b47c-4f67-a152-2ea11732eb0e)




****Neural Network - Cross Validation Model****
-

Kfold (from sklearn) was used to apply cross-validation. Cross-validation allows the neural network to be trained using multiple different training sets, and be tested using different testing sets. This would allow to network to see different training sets with different collections. This would allow the network to learn more about the hidden features (or hidden themes) that may exist in the training sets. Cross-validation also increases the chances of preventing over-fitting

A similar network architecture as the one explained before was used for the Cross-Validation model. Kfold was set to 10.

It appears that The accuracy has improved by about 6-7% to an average of 78%. The maximum accuracy for all 10 cases reaches a value of about 84%. Maximum precision and recall for "Certified" cases are 88% and 89% respectively. For "Denied" cases the maximum precision is 73% and the maximum recall is 72%. These values are higher than what has been obtained from the logistic regression model and single neural network model performed above. Like the other two models, The Cross-validation model is more reliable in predicting "Certified" cases than "Denied" Ones. The reason for that is, maybe, the majority of the dataset has certified cases than denied cases: 12840 for certified (about 70% of the dataset) and 5590 for denied (about 30% of the dataset).

Classification Report for the run (out of the 10 runs) with the lowest performance

![image](https://github.com/HussamGoda/Final-Project/assets/134576485/6b7140d7-335f-4a20-ad6d-3b48426cbfdd)

Classification Report for the run (out of the 10 runs) with the highest performance

![image](https://github.com/HussamGoda/Final-Project/assets/134576485/e0f4d3fb-9706-4a4c-b369-cddf07284f2d)


It was decided to deploy the neural network model trained using Cross-validation.


****Neural Network - Cross Validation Model Deployment****
-

Python Flask and JavaScript were used to deploy the neural network model to a locale server (all files are given in the repo).
Below is a screen capture of the final product.

![image](https://github.com/HussamGoda/Final-Project/assets/134576485/28c4f3ab-eedb-4f30-a931-f4245313675a)

The top 3 input boxes are reserved for the three numerical features (no_of_employees, yr_of_estab, prevailing_wage). Other categorical features are represented by dropdown lists. The user is required to input all three numerical values and select appropriate options from the dropdown list, before clicking "Predict Visa Status". Once the user selects all options from all dropdown lists, the code will perform the encoding to 0 and 1 based on the user selection.
Once the user clicks "Predict Visa Status", the code will go through all runs performed in the Cross-validation model, average them, and then present a visa status output. 



**Conclusion**
-
After comparing both models as above, the neural network emerged as the preferred base model. It significantly outperformed the logistic regression model, boasting an impressive accuracy of 73% for a single model and a remarkable 78-79% for the cross-validation model. The cross-validation model further demonstrated enhanced precision, reaching 82% for "Certified" cases and 65% for "Denied" cases, signifying a substantial overall performance improvement.

Notably, all models excelled in predicting the "Certified" status, showcasing elevated accuracy and precision. The neural network, especially the cross-validation variant, exhibited the most exceptional performance with its outstanding 78-79% accuracy and superior precision for both "Certified" and "Denied" cases.

As a result of these compelling findings, we have seamlessly integrated the cross-validated neural network model into our webpage. This integration empowers users to effortlessly predict the outcome of their visa applications with confidence.
