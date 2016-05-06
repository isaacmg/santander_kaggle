﻿# Santander Repository 
 

**Public LB .0.842838**

**Private LB 0.826414**

**Final Place 1084/5236 (team Alpha_Squad)**

The first of our two submissions was the model generated by best_overfit.R. This produced our best public LB score however failed horribly on the private. Our second submission was the make average script which produced our best private lb score. The script ran on the results of best(no-threshold).R, pca2.py, and blended.py 

1. cross_valid.py is essentially a script I'm working on to be able to predict the our models score without having to upload it to Kaggle (therefore not waste submissions) and for partitioning the training set for stacking. 
2. feature_importance.png is essentially just an image showing the relative importance of variables. 
3. pca.py is a script I pulled off the Kaggle message boards which is an ensemble of several models, unfortunately by itself it does not score well but I'm hoping to stack it with the XGB in R. 
4. var_en.py is what I've been using for my attempts at feature engineering. Basically it created several new categorical features.
5. tester.py the script that made the feature importance histogram. I used this in conjunction with var_en to measure the new features. Unfortunately none of these "new" features have increased LB score. 

 
