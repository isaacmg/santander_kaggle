import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
# The categorical enconding of age. This feature did not work out very well...
def age(age):
    if age['var15']<30:
        return "young"
    if age['var15']<40:
        return "middle"
    if age['var15'] < 50:
        return "upmiddle"
    else:
        return "old"
# Categorize var_38
def var_38(var3, i):
    if str(var3['var38']) == '117310.979016':
        return "avg"
    else:
        return "navg"
# A combo feature of vars 36 and var15
def var_new(var3):
    return var3['var36'] / var3['var15']
# Categorization of variable 36 into a and b
def var_36(var3):
    if var3['var36']==99:
        return "cat1"
    elif var3['var36']==0:
        return "cat2"
    elif var3['var36']==2:
        return "cat3"
    elif var3['var36']==1:
        return "cat4"
    elif var3['var36'] == 3:
        return "cat5"
    else:
        return "cat6"

#
def var_5(var3):
    if var3['saldo_medio_var5_ult3']<0:
        return "pos"
    else:
        return "neg"


def apply_average(y):
   avg = y['TARGET'] + y['TARGET2']
   aveg = avg/2
   return aveg


training = pd.read_csv("train2.csv", index_col=0)
test = pd.read_csv("test2.csv", index_col=0)
#relt1 = pd.read_csv("simplexgbtest.csv", index_col=0)
#result2 =pd.read_csv("submission.csv", index_col=0)
#result2['TARGET2'] = result1.TARGET
#result1['TARGET']=result2.apply(lambda row: apply_average(row),axis=1)
#result1.to_csv("subm.csv")



print(training.shape)
print(test.shape)



X = training.iloc[:,:-1]
y = training.TARGET
s = training.var15
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)

# Add zeros per row as extra feature
#X['var9'] = X.sum(axis=1)



s=s.to_frame()

print training.saldo_medio_var5_ult3.describe()
print training.loc[training['TARGET']==1, 'saldo_medio_var5_ult3'].describe()

X['var36']=training.apply(lambda row: var_36(row),axis=1)

#X['age']=training.apply(lambda row: age(row),axis=1)
X['TARGET']=y

test['var36']=test.apply(lambda row:var_36(row),axis=1)








X.to_csv("train.csv")
test.to_csv("test.csv")


# Create age classfication



