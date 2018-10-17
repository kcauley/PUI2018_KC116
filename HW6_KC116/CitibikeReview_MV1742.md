
# a. Verify that their Null and alternative hypotheses are formulated correctly

Here are Manrique's null and alternative hypotheses:

NULL HYPOTHESIS: Subscribers bike on weekends is the same or higher than the proportion of customers biking on weekends
_H_0: \S_weekend / S_total <= C_weekend/C_total 
_H_1:S_weekend/S_total > C_weekend/C_total

I will use a significance level $\alpha=0.05$ which means i want the probability of getting a result at least as significant as mine to be less then 5% I am starting with a single month of data: reading data from citibike csv file from June 2014

*** This appears to be correctly formulated***




# b. Verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)



# c. Chose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or here, or Statistics in a Nutshell.

*** For this hypothesis, I would chose to apply the chi-square test. The test determines whether there is a significant relationship between two categorical variables (weekday and customer type).
