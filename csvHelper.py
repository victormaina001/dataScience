from sklearn.feature_selection import VarianceThreshold
import pandas as pd 
data = pd.read_excel('path')
data.head()
sel = VarianceThreshold()
sel.fit_transform(data)
print(sel.get_feature_names_out())
sel = VarianceThreshold(threshold=0.01)
sel.fit(data)
print(len(sel.get_feature_names_out()))
quasi_constant = [col for col in data.columns if col not in sel.get_feature_names_out()]
len(quasi_constant)
train = data[sel.get_feature_names_out()]
print(train.shape)
 # find correlated features 
corr_matrix = train.corr()
feature = 'imp_op_var39_comer_ult3'
(corr_matrix[feature].iloc[:corr_matrix.columns.get_loc(feature)] > 0.8).any()
corr_features = [feature for feature in corr_matrix.columns if (corr_matrix[feature].iloc[:corr_matrix.columns.get_loc(feature)] > 0.8).any()]
print(len(corr_features), len(quasi_constant))

#Wrapper Methods
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
X = data.drop(['TARGET'] + quasi_constant + corr_features, axis=1)
y = data['TARGET']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.9, random_state=42)
sfs = SFS(SVC(), k_features=2, verbose=2, cv=2, n_jobs=8)
sfs.fit(X_train, y_train)
#shows the trainScore
print(y_train.value_counts()/len(y_train))
