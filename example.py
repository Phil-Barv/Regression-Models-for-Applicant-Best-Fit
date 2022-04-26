import scipy.stats as sts

from fit import fitting

#set difficulty of questions
difficulty = [1,2,3,4,5,6,7,8,9,10]

#generate applicants
#applicant that performed uniformly
applicantUniform = sts.uniform(0,10).pdf(difficulty)
applicantUniformPerformance = fitting(difficulty, applicantUniform, 'Stacie', scale=50)

#applicant that performed exponentially
applicantExpon = sts.geom.pmf(difficulty,p=0.5)
applicantExponPerformance = fitting(difficulty, applicantExpon,'Susie', scale=20)

#applicant that performed with log distribution
applicantLog = sts.logistic.cdf(difficulty)*10
applicantLogPerformance = fitting(difficulty, applicantLog, 'Missy', scale=10)