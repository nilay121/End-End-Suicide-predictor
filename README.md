# Suicide_predictor 
### About
The model predicts the number of Suicide cases that might happen in different states of India due to various reasons(e.g Dowry,Blackmailing).

![Hnet-image(1)](https://user-images.githubusercontent.com/40202640/131976508-c91c1e69-e0ed-4cad-9f0e-33dc2b77ce71.gif)
 
### Dataset
The dataset for the Suicide Predictor model has been gathered from the website<b> data.gov.in </b>
<br>
The dataset has 7296 rows and 7 columns consisting of State,Year,Type,Type_code,Gender,Age group,Total(Suicides).It has 5 categorical columns, 1 date-time column and 1 numerical column.
### Data Preprocessing
The age was actually given in a range (like 20-30,30-40), so I converted it by taking three age groups T(teenager),A(Adult) and S(Senior).
 <br>
There were some null values in the dataset which I just dropped because they were very less in number in comparison to the size of dataset.
### Feature Handling and Model Creation
I did one hot encoding of the categorical features and then tried different Machine Learning models namely Random Forest Regressor, Decision Tree Regressor, Support vector Regressor, XG boost regressor of which Decision Tree regressor performed the best on the validation set. So, I hypertuned the Decision Tree using GridSearchCV and by using a 3-fold cross validation.
### Pipeline Dumping
After hypertuning the model I created a pipeline having objects of two classes One Hot encoder and the hypertuned Decision Tree Regressor model. I fitted the pipeline on the training set and then dumped the whole pipeline in a pickle file, which could be later used for the model deployment.
<br>

I created a simple API using Flask and deployed the model on Heroku.
<br>
Heroku link:- https://suicidepredictor.herokuapp.com
<br>
Youtube link :- https://www.youtube.com/watch?v=-OSjBFIxFbQ&t=1s



























