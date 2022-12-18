## Assignment 2
The aim of Assignment 2 is to experimentally compare the computational and predictive performance of three learning algorithms on a spam detection task.

**Group assignment:** Max 2 students

**Prerequisite reading:** sections 12.1 - 12.3 in the main literature

**Language:** Python (Already implemented supervised learning algorithms and standard libraries can be used. However, It is NOT permitted to use any library or API that directly computes the Friedman and Nemeyi tests.)

**Data:** Spambase Dataset, https://archive.ics.uci.edu/ml/datasets/SpambaseLinks to an external site.

**Algorithms**
three supervised classification learning algorithms of your choice.

**Evaluation measures:** perform a comparison between the selected algorithms based on:
1) computational performance in terms of training time,
2) predictive performance based on accuracy.
3) predictive performance based on F-measure.

**Procedure**
(repeat steps 2, 3, and 4 for each evaluation measure above)

1. Run stratified ten-fold cross-validation tests.
2. Present the results exactly as in the table in example 12.4 of the main literature.
3. Conduct the ***Friedman test*** and report the results exactly as in the table in example 12.8 of the main literature.
4. Determine whether the average ranks as a whole display significant differences on the **0.05** $\alpha$-level and, if so, use the Nemeyi test to calculate the critical difference in order to determine which algorithms perform significantly different from each other.

**Compute**
the size of possible instances
the size of hypothesis space (the number of possible extensions)
the number of possible conjunctive concepts according to the descriptions in Section 4.1 of the main literature
Implement the algorithm and verify that it works as expected.
Compute the accuracy of the model and report the generated model, i.e., the conjunctive rule.

**Written report**
Template: The IEEE conference template and citation style should be followed (templatesLinks to an external site. in MS word and LaTeX).
Language: English without spelling mistakes.
Style: Clear.
Content: The report should give an overview of the conducted experiments and the obtained results. It should contain (but not be limited to) information about the used classifiers, a brief description of the Friedman and Nemeyi tests along with the formulas, results of the experiment as stated above, results of the comparison stating whether the algorithms perform significantly different or not from each other for each performance measure.
Format: PDF.
Page limit: 2 pages excluding references (no abstract should be included)

**Code**
Provide meaningful comments for different blocks of the code.
A README.TXT file must clearly state exactly how to execute the code and any necessary setups.

**Submission**
Make sure to include your names in the report and the code.
The report must be submitted as a PDF separately (not to be included in the ZIP file).
Code and additional files related to implementation must be archived using ZIP.