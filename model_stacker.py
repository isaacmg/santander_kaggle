import pandas as pd
def stacker_up():
    trained_a = pd.read_csv("train/a_train.csv", index_col=0)
    test = pd.read_csv("train/test2.csv", index_col=0)
    test_xit = pd.read_csv("submission_RF_GBT_ABC_XGB.csv", index_col=0)
    trained_b = pd.read_csv("train/b_train.csv", index_col=0)
    ya = trained_a['TARGET']
    yc = trained_b['TARGET']
    trained_a=trained_a.drop(['TARGET'],axis=1)
    trained_b = trained_b.drop(['TARGET'],axis=1)
    b_res = pd.read_csv("train/b_test.csv",index_col=0)
    a_res = pd.read_csv("train/a_test.csv",index_col=0)
    #
    b_res['bit']=b_res['TARGET']
    a_res['bit']=a_res['TARGET']
    #
    trained_b['bit'] = b_res['TARGET']
    trained_a['bit'] = a_res['TARGET']
    trained_a['bit'] = a_res['TARGET']
    trained_b['bit'] = b_res['TARGET']
    trained_a['TARGET'] = ya
    trained_b['TARGET'] = yc
    test['bit'] = test_xit['TARGET']
    final = trained_a.append(trained_b)
    test.to_csv("test.csv")
    final.to_csv("train.csv")
stacker_up()