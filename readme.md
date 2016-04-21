# Welcome to the Santander Repository 
This is the code I have been working on for the past few weeks. 
1. cross_valid.py is essentially a script I'm working on to be able to predict the our models score without having to upload it to Kaggle (therefore not waste submissions) and for partitioning the training set for stacking. 
2. feature_importance.png is essentially just an image showing the relative importance of variables. 
3. pca.py is a script I pulled off the Kaggle message boards which is an ensemble of several models, unfortunately by itself it does not score well but I'm hoping to stack it with the XGB in R. 
4. var_en.py is what I've been using for my attempts at feature engineering. Basically it created several new categorical features.
5. tester.py the script that made the feature importance histogram. I used this in conjunction with var_en to measure the new features. Unfortunately none of these "new" features have increased LB score. 

If you have any other questions about anything feel free to ask. I will be cleaning the code over the next few days hopefully it will be clearer. Still trying to break the .841644 LB score...
