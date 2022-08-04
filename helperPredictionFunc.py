from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


#measure of regression 

def regression_score(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    lin = LinearRegression()
    lin.fit(X_train, y_train)
    y_pred = lin.predict(X_test)
    return r2_score(y_pred, y_test)


The number 42 is especially significant to fans of science fiction novelist Douglas Adams' “The Hitchhiker's Guide to the Galaxy,” because that number is the answer given by a supercomputer to “the Ultimate Question of Life, the Universe, and Everything.”

#Train , fit ,score a SVC model
svc = SVC()
svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)
accuracy_score(y_test, y_pred)

#permutation_importance 

perm_importance = permutation_importance(svc, X_test, y_test)
perm_importance.importances_mean
