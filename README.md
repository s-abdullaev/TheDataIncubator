# Student Default Rates in 2010-2012

In this project, I would like to find out less known reasons for student loan defaults (SLD) across the US. In my view, the sheer amount of failures to repay the student loans may cause another financial crisis in the US, and therefore it is important to understand how certain factors in this process affect SLD rates. I will use different data analysis techniques such as exploitative data analysis, machine learning and simulation. Below I broke down the phases of the project:

## 1. Data Collection

Although I have found multiple resources providing raw data about SLD rates in the US, there are ample of other relevant data yet to be collected. I can simply download the required data as a file, and later parse it, or use web-scraping tools such as BeautifulSoap (if static pages per given url) or Selenium (if login-required or javascript-based gui) to collect individually. Also I can directly contact people who might possess relevant information needed to this project. As a last resort, I can make certain assumptions about students or any other relevant characteristic that cannot be found, design a reasonable model and simulate it to generate some data. 

Below are links to the public data I found so far:
- [Federal Perkins Loan Program Status of Default - 2015](http://ifap.ed.gov/perkinscdrguide/1415PerkinsCDR.html)
- [Federal Perkins Loan Program Status of Default - 2012](http://www.ifap.ed.gov/perkinscdrguide/1112PerkinsCDR.html)
- [Three-year Official Cohort Default Rates for Schools](http://www2.ed.gov/offices/OSFAP/defaultmanagement/cdr.html), [Codebook](http://www2.ed.gov/offices/OSFAP/defaultmanagement/instructions.html)
- [Official 3-Year Cohort Default Rates for Guaranty Agencies and Lenders](http://www2.ed.gov/offices/OSFAP/defaultmanagement/lga3yr.html)
- [Federal Student Aid Data Center](https://studentaid.ed.gov/sa/data-center)

Relevant contacts:
- [Lenders and Guarantly Agencies](http://www2.ed.gov/offices/OSFAP/defaultmanagement/lga.html)

Additional Info:
- [Default Management Info](http://www.ifap.ed.gov/DefaultManagement/DefaultManagement.html)
- [Explanation of Default Rates](http://www.ifap.ed.gov/eannouncements/060614DefaultRatesforCohortYears20072011.html)
- [Cohort Default Rate Guide](http://ifap.ed.gov/DefaultManagement/guide/attachments/CDRMasterFile.pdf)

Along working in this project, I will need to specify and collect following data:

- Student's academic, professional and social background along with other personal details prior to entering the higher education institution, applying for the loan; 
- Conditions in student loan contracts, principal amounts, repayment periods, time and effort needed to succeed, success rates
- Universities' profiles, rankings, admissions to different programmes, acceptence rates, demographic.

## 2. Data Cleaning

All obtained data will be cleaned for inconsistencies. Missing data will be imputed using techniques such as K-nearest neighbours, or other approximating methods such as Gausian kernels. Data with small sample size will be bootstrapped. Also the relevant features will be extracted using PCA, and collated into complete datasets to facilitate the analysis. The shape of the dataset will be changed according to the features involved.

## 3. Explorative Data Analysis

In this phase, I will try to visualise various aspects of the collected and pre-processed data in interactive plots using Bokeh. This will include choropleth maps to highlight the regionality of the SLDs which could be manipulated to change certain parameters such as year, length of study, by perc/ by volume. Other charts will display correlations (var-covariance matrix), trends (linear plots, bar charts), statistical overview (boxplots, quantile-quantile plots, histograms), contributions (pie charts) etc.

## 4. Predictive Data Analysis

In this phase, I will use machine learning such as regression, classification and clusting algorithms to find previously unseen relationships in the data. I will use 80% of the initial data to train the predictive models, and 20% to test the accuracy rate. I am yet to decide which particular mechine learning algorithm I will use to mine the data, but I am sure this becomes obvious after collecting enough data and accomplishing the initial explorative analysis.

## 5. Presentation 

The results of my research will be published online and presented to panel of hiring managers. 
