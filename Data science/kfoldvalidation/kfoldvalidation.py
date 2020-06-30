from sklearn.linear_model import LogisticRegression 
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np 
from sklearn.datasets import load_digits 
digits=load_digits()
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(digits.data,digits.target,test_size=0.3)

# LogisticRegression Model
# lr=LogisticRegression()
# lr.fit(x_train,y_train)
# print(lr.score(x_test,y_test))

# Support vector Machine
# svm=SVC()
# svm.fit(x_train,y_train)
# print(svm.score(x_test,y_test))

# Random forest
# rf=RandomForestClassifier(n_estimators=40)
# rf.fit(x_train,y_train)
# print(rf.score(x_test,y_test))

# K fold example

from sklearn.model_selection import KFold
kf=KFold(n_splits=3)
for train_index,test_index in kf.split([1,2,3,4,5,6,7,8,9]):
    print(train_index,test_index)

# For uniform kfold and best accuracy use Straticfiedkfold
from sklearn.model_selection import StratifiedKFold
foldss=StratifiedKFold(n_splits=2)
from sklearn.model_selection import cross_val_score
print(cross_val_score(LogisticRegression(),digits.data,digits.target))
print(cross_val_score(SVC(),digits.data,digits.target))
print(cross_val_score(RandomForestClassifier(n_estimators=40),digits.data,digits.target))