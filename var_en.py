from __future__ import division
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import math
matplotlib.use("Agg")

from sklearn.cross_validation import train_test_split

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
    we=var3['var15'] + var3['saldo_medio_var5_ult3']
    return var3['var38'] /we
# Categorization of variable 36 into a and b
def var_36(var3):
    if var3['var36']==99:
        return 0.0644624800426
    elif var3['var36']==0:
        return 0
    elif var3['var36']==2:
        return 0.0276884191176
    elif var3['var36']==1:
        return 0.0314375340971
    elif var3['var36'] == 3:
        return 0.0165937683185
    else:
        return 0
def num_var(var3):
    if var3['num_var4']==0:
        return 0.0889492011471
    elif var3['num_var4'] == 1:
        return 0.018140351797
    elif var3['num_var4'] == 2:
        return 0.0262369996848
    elif var3['num_var4'] == 3:
        return 0.0415809915467
    elif var3['num_var4'] == 4:
        return 0.0562560620757
    elif var3['num_var4'] == 5:
        return 0.0295566502463
    else:
        return 0

    return 0
def catty(var3):
   if var3['num_var4']==0 and var3['var36']==99 and var3['num_var5']==0:
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
def take_log(var3):
    return math.log(var3['var38'])



training = pd.read_csv("train/train2.csv", index_col=0)
test = pd.read_csv("train/test2.csv", index_col=0)
#resut1 = pd.read_csv("simplexgbtest.csv", index_col=0)
#result2 =pd.read_csv("submission.csv", index_col=0)
#result2['TARGET2'] = resut1.TARGET
#resut1['TARGET']=result2.apply(lambda row: apply_average(row),axis=1)
#resut1.to_csv("subm.csv")
#training['n2'] = training.sum(axis=1)
#test['n0'] = (test > 0).sum(axis=1)


print(training.shape)
print(test.shape)



X = training.iloc[:,:-1]
y = training.TARGET
s = training.var15
#X_train, X_test, y_train, y_test = train_test_split(
    #X, y, test_size=0.25, random_state=42)

# Add zeros per row as extra feature
#X['var9'] = X.sum(axis=1)


#X['n2'] = training.sum(axis=1)
s=s.to_frame()
X['new_var']=training.apply(lambda row: catty(row),axis=1)
X['var38']=training.apply(lambda row: take_log(row),axis=1)

X['TARGET']=y



total_counts = X['saldo_medio_var13_largo_ult1'].describe()

target_counts = X[X.TARGET==1].saldo_medio_var13_largo_ult1.describe()
print total_counts
print target_counts

#print target_counts[0]/total_counts[0]
#print target_counts[1]/total_counts[1]
#print target_counts[2]/total_counts[2]
#print target_counts[3]/total_counts[3]
#print target_counts[4]/total_counts[4]
#print target_counts[5]/total_counts[5]
#print X['var_new'].value_counts()

print total_counts

#### var36 categories


##sns.FacetGrid(X, hue="TARGET", size=6) \
   ##.map(plt.hist, "var_new") \

##plt.title('Unhappy cosutomers have less products')
##fig2 = plt.gcf()
##plt.show()
sns.FacetGrid(X, hue="TARGET", size=6) \
   .map(sns.kdeplot, "new_var") \

plt.title('new_var')

plt.draw()
plt.show()
#fig2.savefig("new_feature.png")


test['var38']=training.apply(lambda row: take_log(row),axis=1)

#X['age']=training.apply(lambda row: age(row),axis=1)
test['new_var']=test.apply(lambda row:catty(row),axis=1)
X['TARGET']=y


X.to_csv("train.csv")
test.to_csv("test.csv")










# Create age classfication



