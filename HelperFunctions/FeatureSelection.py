
import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
data = pd.read_parquet('files/house_sales.parquet')
data.head()
data['SalePrice'].value_counts()/len(data)
data.shape
data.info()
data = data.drop('PoolQC', axis=1)
data = data.fillna(-1)
sel = VarianceThreshold(threshold=0.01)
sel.fit(data)
len(sel.get_feature_names_out())
quasi_features = [col for col in data.columns if col not in sel.get_feature_names_out()]
quasi_features
corr_matrix = data.corr()
corr_features = [feature for feature in corr_matrix.columns if (corr_matrix[feature].iloc[:corr_matrix.columns.get_loc(feature)] > 0.8).any()]
corr_features
X = data.drop(['SalePrice'] + quasi_features + corr_features, axis=1)
y = data['SalePrice']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
sfs = SFS(LinearRegression(), k_features=10, verbose=2)
sfs.fit(X_train, y_train)
sfs.k_feature_idx_
lin = LinearRegression()
lin.fit(X_train, y_train)
y_pred = lin.predict(X_test)
r2_score(y_test, y_pred)
columns = X_train.columns[list(sfs.k_feature_idx_)]
lin.fit(X_train[columns], y_train)
y_pred = lin.predict(X_test[columns])
r2_score(y_test, y_pred)
columns = corr_matrix['SalePrice'].sort_values(ascending=False)[1:11].index
X_train, X_test, y_train, y_test = train_test_split(data.drop('SalePrice', axis=1), y, random_state=0)

lin = LinearRegression()
lin.fit(X_train[columns], y_train)
y_pred = lin.predict(X_test[columns])
r2_score(y_test, y_pred)
X_train.columns[list(sfs.k_feature_idx_)]
print(corr_features)


