# Assignment 2 Review for KC 116
 ## A. Verify that their Null and alternative hypotheses are formulated correctly:
 Hypothesis evaluation:
 Having read the Idea for analysis, it is clear to me that the author wants to 
Alternative Hypothesis: During the weekends there will be more 'Customers'(non-subscribers who purchase 24hr passes) using Citibike than regular subscribers.
Null Hypothesis: Weekend activity has the same or less users described as 'customers.'
 However, it lacks certain specifications that would make the hypothesis testable, despite giving the significance level. 
 
## B. Verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)

The data for two genders and durations for a specific time period has been identified. I would suggest in addition to separate the two samples into two df objects (for male and female separately) and normalizing, since we are looking at the mean. At a first glance the distribution for both genders resembles Gaussian. 

Please note that despite the fact that all citibike data is provided, I assume we only compare two samples without population knowledge. This is assumption I decide to follow, however given we actually can calculate the population data, it could be restated accordingly.

## c. Chose an appropriate test to test H0 given the type of data, and the question asked.

Having two different categories being presented in different week days, I would choose Chi-Square test as it can focus on expressing the relationship between categorical data. In this case, the two categories are 'Subscribers' and 'Customers'. This test can possibly give potential opinions on if the ride counts pattern of subscribers and customers would demonstrate certain trends throughout weekdays and the weekends. 

 






  
