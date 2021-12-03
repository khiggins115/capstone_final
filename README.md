# README


# Capstone: Self-Harm Mortality Rate and Alcohol Use Prevalence by County


### Problem Statement

Deaths from self harm (i.e. suicide and other intentional injuries that result in death) far outpace other mortality categories in the IMHE dataset. Knowing that substance/alcohol abuse is a factor in many diseases and mental/behavioral health disorders, I will create supervised and unsupervised model(s) to that explore the relationships between mortality rate by self-harm and other variables such as sex, year, state, unemployment and the different levels of alcohol use/abuse.


# Executive Summary

After a previous project utilized US county level mortality rate datasets from The Institute for Health Metrics & Evaluation, there were some mortality rates, even taken as an average of an age standardized mortality metric accounting for all 3000+ counties in the United States, that really jumped out. IMHE, global health research center headquartered at the University of Michigan, studies such mortality rates among other things, and has produced a data series of county level mortality rates for [Alcohol Use disorders and Drug Use Disorders from 1980 - 2014](http://ghdx.healthdata.org/record/ihme-data/united-states-substance-use-disorders-intentional-injuries-mortality-rates-county-1980-2014). This dataset additionally includes mortality by Self-Harm (Intentional Injury that results in death and/or Suicide) and Interpersonal Violence. 

Looking at a graph over time, the mortality rate from self harm far outpaced the other three mortality categories included in the dataset. Curious sufficiently piqued, I took to the internet to browse existing research. What I found was surprising. The mortality rate from self-harm/intentional-injury has [surpassed diabetes mortality rate](https://injuryprevention.bmj.com/content/25/4/331). In some places, (ex. Alaska) the self-harm mortality rate is comporable to the mortality rates from other diseases such as [Cancer](https://www.cdc.gov/nchs/pressroom/sosmap/cancer_mortality/cancer.htm) and [Heart Disease](https://www.cdc.gov/nchs/pressroom/sosmap/heart_disease_mortality/heart_disease.htm). This premature loss of life is not only tragic and preventable, but it costs our country money in terms of emergency room dollars & lost contributions to the national economy. In 2019 alone, the [economic cost of suicide mortality](https://www.cdc.gov/mmwr/volumes/70/wr/mm7048a1.htm?s_cid=mm7048a1_w) among 25-44 year olds was **167 Billion** while 45-74 year olds represented a **174 billion dollar economic burden**. And yet, public health dollars that go towards research aimed at preventing unnecessary deaths and lowering the self-harm mortality rate are shockingly low. [Funding for Cancer research and prevention](https://www.cancer.gov/about-nci/budget/fact-book/data/research-funding) at the NIH's National Cancer Instituteand totals in the hundreds of millions for individual types of cancers, while the NIH put [***35 million*** towards suicide prevention in 2017](https://www.reuters.com/article/us-usa-suicides/u-s-suicide-prevention-programs-say-more-funding-needed-idUSKCN1J42WF). 

While looking into funding statistics, it struck me that public health research dollars towards alcoholism totaled **500 million** in 2017 alone, and while alcoholism does result in many deaths yearly, the disparity in funding is shocking when the mortality rates from suicide and alcoholism are comparable.

This set me wondering if there is a strong enough relationship between some mortality categories to justify a potential joining of forces, so to speak. Overuse of alcohol is a factor in many diseases, and causal relationships have been established between harmful drinking and various mental/behavioral health disorders as well as incidence of infectious diseases such as TB and HIV/AIDS. The World Health Organization estimates that, globally, as many as *3 million deaths per year* can be attributed to [harmful alcohol use](https://www.who.int/news-room/fact-sheets/detail/alcohol). This is true as much in the US as it is in other nations.

This project then, aims to create models that explore the strength of relationships between alcohol use/overuse/abuse and self-harm mortality, in tandem with other variables such as year, sex (Male/Female) and state. By understanding some of these relationships, we can better target interventions and more effeciently use public health dollars. 

By combining IMHE's self-harm mortality data with IMHE's alcohol use prevalence, univariate and multivariate regression modeling was performed, as well as kmeans clustering. 


### Contents
- code_appendix
    - 00_DataCollection_Cleaning
    - 01_EDA
    - 02_UnivariateRegressionModeling
    - 03_MultivariateRegressionModeling
    - 04_kmeans_clustering
- data
    - alcohol_substance_deaths
    - alcohol_use_prev
    - cleaned
    - unemployment_csv
- deliverables
 - capstone_KH.pdf
 - capstone_KH.pptx
 - img


### Data Dictionary


#### selfharm_mortality
|Feature|Type|Description|
|---|---|---|
|location_name|object|County Name|
|FIPS|object|County FIPS Code|
|cause_name|object|Cause of Death|
|sex|object|Gender (Male, Female, Both) where 'Both' is average of male/female|
|year_id|int64|Year|
|mx|float64|mortality rate - deaths per 100K population|
|state|object|State|
|UID|object|Unique Identifier created for joining datasets by FIPS-year|
|UID_2|object|Alternate Unique Identifier for joining data by FIPS-sex-year|

#### alcohol_any
|Feature|Type|Description|
|---|---|---|
|FIPS|object|County FIPS Code|
|county_name|object|County Name|
|state|object|State|
|county_state|object|County, State Long Name|
|year_id|int64|Year|
|sex|object|Gender (Male, Female, Both) where 'Both' is average of male/female|
|year_metric_category|object|long version of year / sex|
|UID|object|Unique Identifier created for joining datasets by FIPS-year|
|UID_2|object|Alternate Unique Identifier for joining data by FIPS-sex-year|
|alcohol_any|float64|Prevalence of Any Alcohol Use|

#### alcohol_heavy, alcohol_binge
Include the same columns as above, but instead of alcohol_any, contain: 

|Feature|Type|Description|
|---|---|---|
|alcohol_heavy|float64|Prevalence of Heavy Alcohol Use|
|alcohol_prop_heavy|float64|Proportion of all Drinkers who are Heavy Drinkers|
|alcohol_binge|float64|Prevalence of Binge Alcohol Use|
|alcohol_prop_binge|float64|Proportion of all Drinkers who are Binge Drinkers|

#### unemployment
(used only in KMeans)
Joined with selfharm and alcohol use/abuse data frames, the unemployment data columns match what is in those (FIPS, State, mx, alcohol_heavy, alcohol_prop_heavy, alcohol_binge, alcohol_prop_binge, etc) but add the below variables

|Feature|Type|Description|
|---|---|---|
|labor_force|int64|Available Labor Force|
|employed|int64|Employed Population|
|unemployed|int64|Total Unemployed population|
|unemployment_rate|float64|County unemployment rate|



### Conclusion

Multivariate Regression Models drastically outperformed Univariate Regression Models, confirming that the inclusion of state and sex strengthens the relationship. RandomForest and GradientBoost Regressors performed the best, but didn't respond well to hypertuning. All had RMSE that was very low, so we can have high confidence that these variables have established relationships, though we cannot say for certain anything about causality (which was not the purpose of this exercise anyways). 

KMeans Clustering was an interesting exercise - 4 clusters yielded the highest silhouette scores, while including labor_force drove up SIL score to over 0.8. Including `unemployment_rate` but not `labor_force` did not yield similarly impressive results.

I think this exercise holds promise for identifying areas that have similarly and disproportionately burdened by alcohol abuse and mortality by self-harm. Potential applications include regionally targeted interventions that could aim to address multiple public health problems at once for certain geographies. 

### Next Steps
In future iterations on this theme, I would ideally find more recent data that is more complete across all sources. Based on trends observed in selfharm mortality and heavy/binge drinking prevalence on the choropleth maps of US counties, there seemed to it intuitively seemed that disproportionally affected areas are those that have little sunlight and/or harsh winters. Future models might explore the strength of the relationship between total yearly hours of sunlight and selfharm mortality. 

Additionally, I'd like to create an interactive application that allows users to select which variables to cluster and visualize the results. Because of the sheet size of the dataset, for this app to function at acceptable speeds some utilization of databases or AWS would be appropriate. 


### Sources

- [IMHE Mortality](http://ghdx.healthdata.org/record/ihme-data/united-states-substance-use-disorders-intentional-injuries-mortality-rates-county-1980-2014)
- [IMHE Alcohol Use](http://www.healthdata.org/us-health/data-download)
- [Unemployment]()
- https://injuryprevention.bmj.com/content/25/4/331
- https://www.cdc.gov/nchs/pressroom/sosmap/cancer_mortality/cancer.htm
- https://www.who.int/news-room/fact-sheets/detail/alcohol
