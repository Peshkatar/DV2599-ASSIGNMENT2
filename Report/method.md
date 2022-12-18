### **A. Data Exploration**
Upon examination we find a right-skewed distribution for all but the target feature. The target column has a 60/40-procent ratio of ham and spam making it a fairly balanced data set.
Furthermore, we have 391 duplicate instances.

### **B. Data Transformation (discretization)**
Due to support vector machines being very sensitive to outliers(?) [1] we discretized our data set so that we'd get more comparable performance for the later evaluations.
Discretization was performed with the KBinsDiscretizer method from Sklearn [2] with X bins and Y binning technique.

### **C. Computing the Friedman & Nemenyi [post hoc] test**
The Friedman test is a non-parametric statistical test (does not assume data follows normal distribution) used to determine whether are significant differnces between treatments (algorithms) being compared in a study.
The friedman test is a rank-based test, meaning it ranks the treatments being compared and the computes a test statistic based on the ranks. If the test statistic
passes a certain threshold, referred to as the critical value (determined by the number of treatmets being compared and the significance level [5%]), then the null hypothesi
that there are no significant differences between the treatments is rejected.
In our study we have 3 treatment groups with the following three performance metrics: f-measure (description.), accuracy (the percentage of predictions that are true), computatioal time (time taken to train algorithm)

The nemenyi test is a post hoc statistical test that is conducted after completition of a study (post hoc) in order to compare treatments in a group. The nemenyi test allows us to
identify which treatments are significantly (observed diff due to chance is low) different from each other. With the nemenyi test we compare the rank means
of each treatment to identify which pairs of treatments that display a significant difference from each other. We conclude whether the difference
between treatments is significant or not by seeing if the difference between means is greater than the critical difference (threshold value, taking into account alpha)
The test will conclude that the treatments are significantly different if they pass this threshold.

### D. **Algorithms**
This study has choosen the following 3 classification models to compare:
Support Vector Machine: an algorithm that .. <br>
AdaBoost: ... <br>
Random Forest: ... <br>

### E. **Code and algorithm implementation**
The study was performed in a virtual environment on jupyter-lab with python 3.11. Our classifier models came from the sklearn library and the data
was processed and read via the pandas package. For more complex filtering and mathmetical operations NumPy was used.

### **F. Training and evaluation (cross validation. f-measure, accuracy, computational time)**
We used stratified k-fold cross validation as our training and testing procedure.The paradigm is as following: We split our data into k folds (10 in our case)
and use 9 of these folds to train our data and the remaining one to test. We repeat this procedure k-1 more times (9) without replacement.
To ensure we get a fair representation of our target with each sample the folds preserve the percentage of samples for each class [3].
With this technique we get a more robust measure of perfomance by allowing our model to train and test on different parts of the data set.
However this methodology is more computationally expensive [4].

We measure model performance with the following three metrics:
f-measure: ... <br>
accuracy: percentage of predictions that are true. <br>
computational time: time taken for model/algo to train.


### **References:**
1. https://arxiv.org/abs/1409.0934
2. Sklearn Discretizater
3. https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html
4. https://outerbounds.com/docs/what-is-cross-val/