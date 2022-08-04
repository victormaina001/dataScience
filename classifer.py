from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd
#reading file a from csv and storing in a dataframe
data = pd.read_csv('files/iris.csv', index_col=0)
data.head()
data['Species'].value_counts()
#cleaning the data to create x=independent features (those predicting) to and y =classes (labels/dependent features) to
X = data.drop('Species', axis=1)
y = data['Species']
#machinelearning section 
#dividing into training and testing data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

svc = SVC()
svc.fit(X_train, y_train)
#predict with the model 
y_pred = svc.predict(X_test)
# test accuracy of the model 
accuracy_score(y_test, y_pred)