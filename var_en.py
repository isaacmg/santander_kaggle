import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
from sklearn.cross_validation import train_test_split
# The categorical enconding of age. This feature did not work out very well...
def stacker_up():
    trained_a = pd.read_csv("train/a_train.csv", index_col=0)
    test = pd.read_csv("train/test2.csv", index_col=0)
    test_xit = pd.read_csv("simplexgbtest.csv", index_col=0)
    trained_b = pd.read_csv("train/b_train.csv", index_col=0)
    b_res = pd.read_csv("submission_b.csv",index_col=0)
    a_res = pd.read_csv("submission_a.csv",index_col=0)
    b_res['xit']=b_res['TARGET']
    a_res['xit']=a_res['TARGET']
    b_res['TARGET']=trained_b['TARGET']
    a_res['TARGET']=trained_a['TARGET']
    trained_a['xit'] = a_res['TARGET']
    trained_b['xit'] = b_res['TARGET']

    test['xit']=test_xit['TARGET']
    final=a_res.append(b_res)
    test_xit.to_csv("test.csv")
    final.to_csv("train.csv")




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
    we=var3['var15'] + var3['saldo_medio_var5_ult3']
    return var3['var38'] /we
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
def catty(var3):
    if var3['var36'] == 99 and var3['num_var4']== 0 and var3['num_var5'] ==0 :
        return 1
    return 0

#
def var_5(var3):
    if var3['saldo_medio_var5_ult3']<0:
        return "pos"
    else:
        return "neg"


def apply_average(y):
   avg = y['TARGET']*.79 + y['TARGET2']*.21
   data_dict={}
  
   aveg = avg/3
   return avg



training = pd.read_csv("train/train2.csv", index_col=0)
test = pd.read_csv("train/test2.csv", index_col=0)
resut1 = pd.read_csv("simplexgbtest.csv", index_col=0)
result2 =pd.read_csv("submission.csv", index_col=0)
result2['TARGET2'] = resut1.TARGET
resut1['TARGET']=result2.apply(lambda row: apply_average(row),axis=1)
resut1.to_csv("subm.csv")
training['n0'] = (training > 0).sum(axis=1)
test['n0'] = (test > 0).sum(axis=1)


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


X['var_new']=training.apply(lambda row: catty(row),axis=1)

print X.var36.describe()
print X.loc[X['TARGET']==1, 'var36'].describe()
print X['var36'].value_counts()
print X[X.TARGET==1].var36.value_counts()

sns.FacetGrid(X, hue="TARGET", size=6) \
   .map(plt.hist, "var_new") \

plt.title('Unhappy cosutomers have less products')
fig2 = plt.gcf()
plt.show()

plt.draw()
fig2.savefig("new_feature.png")



#X['age']=training.apply(lambda row: age(row),axis=1)
X['TARGET']=y

test['var_new']=test.apply(lambda row:catty(row),axis=1)

X.to_csv("train.csv")
test.to_csv("test.csv")









# Create age classfication



