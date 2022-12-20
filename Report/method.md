### **A. Data Exploration**
Upon examination we find a right-skewed distribution for all but the target feature. The target column has a 60/40-procent ratio of ham and spam making it a fairly balanced data set.
Furthermore, we have 391 duplicate instances.

### **B. Data Transformation (discretization)**
Due to support vector machines being very sensitive to outliers(?) [1] we discretized our data set so that we'd get more comparable performance results between the algorithms. Discretization was performed with the KBinsDiscretizer method from Sklearn [2] with 7 bins and kmeans binning technique.

### **C. Computing the Friedman & Nemenyi test**
The Friedman test is a non-parametric statistical test (does not assume data follows normal distribution) used to determine whether are significant differnces between treatments (algorithms) being compared in a study.
The friedman test is a rank-based test, meaning it ranks the treatments being compared and the computes a test statistic based on the ranks. If the test statistic
passes a certain threshold, referred to as the critical value (determined by the number of treatmets being compared and the significance level [5%]), then the null hypothesis that there are no significant differences between the treatments is rejected.
<br>

- **Friedman test** [6] <br>
k = number of treatments (algorithms) <br>
n = number of samples (blocks)

    **(1.1)** Mean rank: $\bar{R} = \frac{1}{nk}R_{ij} = \frac{k + 1}{2};$ <br>
    **(1.2)** Sum of squared differences: $n \sum_j (R_j - \bar{R})^2;$ <br>
    **(1.3)** Sum of squared differences: $\frac{i}{n(k - 1)} \sum_{ij} (R_{ij} - \bar{R})^2;$ <br>
    **(1.4)** Friedman score - ratio between 1.2 & 1.3: $\frac{n \sum_j (R_j - \bar{R})^2}{\frac{i}{n(k - 1)} \sum_{ij} (R_{ij} - \bar{R})^2}.$ <br>

The nemenyi test is a post hoc statistical test that is conducted after completition of a study (post hoc) in order to compare treatments in a group. The nemenyi test allows us to
identify which treatments are significantly (observed diff due to chance is low) different from each other. With the nemenyi test we compare the rank means
of each treatment to identify which pairs of treatments that display a significant difference from each other. We conclude whether the difference between treatments is significant or not by seeing if the difference between means is greater than the critical difference (threshold value, taking into account alpha). The test will conclude that the treatments are significantly different if they pass this threshold.

- **Nemenyi test** <br>
**(2.1)** Critical difference: $CD = q_\alpha \sqrt{\frac{k(k+1)}{6n}}$ [6] <br>
**(2.2)** $\sum_{ij} | \bar{R_i} - \bar{R_j} | > CD$. [5]

### **D. Algorithms**
This study has choosen the following 3 classification models to compare: <br>
Support Vector Machine: an algorithm that **...** <br>
AdaBoost: **...** <br>
Random Forest: **...** <br>
These algorithms show great performance, are very popular [10] and don't require much-to-any hyper parameter tuning. These reasons were the motivation behind our decision.

### **E. Code and algorithm implementation**
The study was performed in a virtual environment on jupyter-lab with python 3.11. Our classifier models and performance measures came from the sklearn library and the data was processed and read via the pandas package. For more complex filtering and mathmetical operations NumPy and itertools was used and lastly for measuring the training time we borrowed the time method from the standard library time.

### **F. Training and evaluation (cross validation. f-measure, accuracy, computational time)**
We used stratified k-fold cross validation as our training and testing procedure.The paradigm is as following: We split our data into k folds (10 in our case)
and use 9 of these folds to train our data and the remaining one to test. We repeat this procedure k-1 more times (9) without replacement.
To ensure we get a fair representation of our target with each sample the folds preserve the percentage of samples for each class [3].
With this technique we get a more robust measure of perfomance by allowing our model to train and test on different parts of the data set.
However this methodology is more computationally expensive [4].

We measure model performance with the following three metrics: <br>
- **F-measure**: also known as F1 score, is a performance metric used to evaluate a classification model. It is computed as the harmonic mean between precision and recall. F-measure ranges between 0 to 1, with higher values meaning better performance. It is a balanced metric that considers both precision and recall of the model.<br>
$F1 = 2 * \frac{precision * recall}{precision + recall}, F1 \in [0, 1]$ <br>
- **Precision**: is the fraction of true positive (TP) predictions made by the model among all positive predictions. <br>
$precision = \frac{TP}{TP+FP}, precision \in [0, 1]$ <br>
- **Recall**: is the fraction of true positive predictions made by the classifier among all actual positive predictions. <br>
$recall = \frac{TP}{TP+FN}, recall \in [0, 1]$ <br>
- **Accuracy**: the percentage of predictions that are correct. <br>
$accuracy = \frac{TP + TN}{TP + FP + TN + FN}, accuracy \in [0, 1]$ <br>
- **Computational time**: time taken to train algorithm.

### **References:**
1. https://arxiv.org/abs/1409.0934
2. Sklearn Discretizater
3. https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html
4. https://outerbounds.com/docs/what-is-cross-val/
5. https://www.real-statistics.com/one-way-analysis-of-variance-anova/kruskal-wallis-test/nemenyi-test-after-kw/
6. boken
10. https://www.simplilearn.com/10-algorithms-machine-learning-engineers-need-to-know-article