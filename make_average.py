import pandas as pd
def apply_average(y):
   avg = y['TARGET']*.85 + y['TARGET2']*.1+y['TARGET3']*.05
   print y['TARGET4']
   if y['TARGET4']==0:
       return 0
   return avg
def sub(y):
    return
resut1 = pd.read_csv("rank_average/simplexgbtest.csv", index_col=0)
result2 =pd.read_csv("rank_average/submission.csv", index_col=0)
result3 = pd.read_csv("rank_average/sub1.csv",index_col=0)
result4 = pd.read_csv("rank_average/submission2.csv",index_col=0)
result2['TARGET3']= result3.TARGET
result2['TARGET2'] = resut1.TARGET
result2['TARGET4']= result4.TARGET
resut1['TARGET']=result2.apply(lambda row: apply_average(row),axis=1)


resut1.to_csv("subm.csv")


