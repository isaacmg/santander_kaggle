import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn import cross_validation
training = pd.read_csv("train2.csv", index_col=0)
test = pd.read_csv("test2.csv", index_col=0)
#relt1 = pd.read_csv("simplexgbtest.csv", index_col=0)
#result2 =pd.read_csv("submission.csv", index_col=0)
#result2['TARGET2'] = result1.TARGET
#result1['TARGET']=result2.apply(lambda row: apply_average(row),axis=1)
#result1.to_csv("subm.csv")



print(training.shape)
print(test.shape)



def make_training():
    training = pd.read_csv("train2.csv", index_col=0)
    test = pd.read_csv("test2.csv", index_col=0)

    X_train, X_test = train_test_split(
        training, test_size=0.5, random_state=42)

    X_train.to_csv("a_train.csv")
    X_test.drop('TARGET', 1)

    X_test.to_csv("b_train.csv")




    return X_train, X_test

def test_prediction():
    result = pd.read_csv("test2.csv", index_col=0)
    scores = cross_validation.cross_val_score()

    return



make_training()
