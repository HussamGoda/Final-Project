# Import required dependancies
import numpy as np
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
from flask import Flask, request, render_template


# Flask Setup
app = Flask(__name__)

# import dataset to access training data, pre processing, 
easy_visa_original_data_df = pd.read_csv("easy_visa_cleaned_NoOutliers.csv")
easy_visa_df = easy_visa_original_data_df.copy()
easy_visa_df = easy_visa_df.drop(["case_id"], axis=1)
easy_visa_df = easy_visa_df.drop(["unit_of_wage"], axis=1)
columns_to_convert = ['continent', 'education_of_employee', 'has_job_experience', 'requires_job_training', 'region_of_employment', 'full_time_position', 'case_status']
easy_visa_df = pd.get_dummies(easy_visa_df, columns=columns_to_convert)
easy_visa_df = easy_visa_df.drop(columns=["case_status_Denied"])
y = easy_visa_df.case_status_Certified.values
X = easy_visa_df.drop(columns="case_status_Certified", ).values

# Defining the cross validation model, load each model and assign models and correspoding training dataset to a list 
num_of_folds = 10
kf = KFold(n_splits=num_of_folds, shuffle=True, random_state=42)

xv_models = []
datasets = []

for i, (train_index, test_index) in enumerate(kf.split(X)):
    # Split the data into training and testing sets for this fold
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    scaler = StandardScaler()
    X_scaler = scaler.fit(X_train)
    X_train_scaled = X_scaler.transform(X_train)

    model_file_path = f"ss_runs/model_number_{i+1}.pkl"
    model = pickle.load(open(model_file_path, 'rb'))

    xv_models.append(model)
    datasets.append((X_train_scaled, y_train))

# Flask Routes

@app.route("/")
def VisaStatus():
    # Connect to the HTML file placed in the folder "templates"
    return render_template('index.html')

# route to predict visa status, using the method POST and send th html
@app.route('/predict', methods=['POST'])
def predict ():
   
     # calling data from form and assign to dictionary
    data = request.form.to_dict()
    print(data)
    # Delete string variables
    del data['Selected Region']
    del data['Selected Continent']
    del data['Selected Education']
    del data['Selected Experience']
    del data['Selected Training']
    del data['Selected Position']

    # Rearrange entries in the dictionary to match the order of input features used during creating the neural network model
    final_data = {
    'Company Size': data['Company Size'], 'Year Compnay Established': data['Year Compnay Established'], 'Prevailing Wage': data['Prevailing Wage'],
    'Africa': data['Africa'], 'Asia': data['Asia'], 'Europe': data['Europe'], 'North America': data['North America'], 'Oceania': data['Oceania'], 'South America': data['South America'],
    'Bachelor': data['Bachelor'], 'Doctorate': data['Doctorate'], 'HighSchool': data['HighSchool'], 'Master': data['Master'],
    'requireexpN': data['requireexpN'], 'requireexpY': data['requireexpY'],
    'requiertrainingN': data['requiertrainingN'], 'requiertrainingY': data['requiertrainingY'],
    'region_of_employment_Island': data['region_of_employment_Island'], 'region_of_employment_Midwest': data['region_of_employment_Midwest'],
    'region_of_employment_Northeast': data['region_of_employment_Northeast'], 'region_of_employment_South': data['region_of_employment_South'],
    'region_of_employment_West': data['region_of_employment_West'], 'fulltimepositionN': data['fulltimepositionN'], 'fulltimepositionY': data['fulltimepositionY']
    }

    print(final_data)

    # Ensuring all data are of numerical type, assigning to an array, transform and predict
    input_features = [float(x) for x in final_data.values()]  
    features = [np.array(input_features)]
    
    visa_pred = []

    for model, (X_train_fold, y_train_fold) in zip(xv_models, datasets):
        input_values_scaled = X_scaler.transform(features)
        prediction = model.predict(input_values_scaled)
        visa_pred.append(prediction)
    
    visa_status = np.mean(visa_pred)
    
    if visa_status >= 0.5:
        output = "Certified (Accepted)"
    else:
        output = "Denied (Rejected)"

    # Send the output predicted (visa stusts) to the html file
    return render_template('index.html', prediction_text='Visa Status: {}'.format(output))

if __name__ == '__main__':
    app.run()
