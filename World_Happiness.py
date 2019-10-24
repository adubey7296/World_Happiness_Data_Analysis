#!/usr/bin/env python
# coding: utf-8

# ## The World Happiness Report Data Analysis:
# 
# ### A. Importing, cleaning and numerical summaries
# 
# * Download the data set data.csv from the Kaggle.
# * Import the data as a pandas DataFrame.
# * Check the number of observations.
# * Obtain the column headings.
# * Check the data type for each column.
# * Check if there are any missing values.
# * If necessary remove any observations to ensure that there are no missing values and the values in each column are of the same data type.
# * Obtain the mean, minimum and maximum value for each column containing numerical data.
# * List the 10 happiest countries.
# * List the 10 least happy countries.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


whr = pd.read_csv("2016.csv")


# In[3]:


whr.head(12)


# In[4]:


whr.shape


# In[5]:


print("There are {:,} rows ".format(whr.shape[0]) + "and {} columns in our data".format(whr.shape[1]))


# In[6]:


whr.set_index('Country', inplace=True)

whr.info()


# In[7]:


whr.isnull().sum()


# In[8]:


NULLS = whr[whr.isnull().any(axis=1)]


# In[9]:


whr.dropna(inplace=True)

whr.isnull().sum()


# In[10]:


whr.duplicated().sum()


# In[11]:


whr.describe()


# In[12]:


whr.sort_values(by="Happiness Rank", ascending=True).head(10)


# In[13]:


whr.sort_values(by="Happiness Rank", ascending=False).head(10)


# ### B. Indexing and grouping
# 
# * Use the column 'Region' to create a separate DataFrame containing the data points from each of the six regions: North America, Latin America, Western Europe, Eastern Europe, Asia Pacific, Africa.
# * Compute the mean happiness score for each region and rank the regions from most happy to least happy.
# * Compute the number of countries in each region that have a happiness score above 6.0.
# * Compute the difference between the maximum and minimum happiness score for each region. Which region has the largest range of happiness scores?

# In[14]:


whr_Region = whr.groupby('Region')


# In[15]:


whr_Region['Happiness Score'].describe().sort_values(by="mean",ascending=True).head(10)


# In[16]:


whr[whr["Region"]=="Western Europe"].head()


# In[17]:


whr = whr.replace('Europe', 'Eastern Europe')


# In[18]:


whr_Region['Happiness Score'].describe().sort_values(by="mean",ascending=False).head(10)


# In[19]:


whr_SSA = whr[whr['Region'] == 'Sub-Saharan Africa']
whr_WE = whr[whr['Region'] == 'Western Europe']
whr_CEE = whr[whr['Region'] == 'Central and Eastern Europe']
whr_NA = whr[whr['Region'] == 'North America']
whr_ANZ = whr[whr['Region'] == 'Australia and New Zealand']
whr_LAC = whr[whr['Region'] == 'Latin America and Caribbean']
whr_EA = whr[whr['Region'] == 'Eastern Asia']
whr_MENA = whr[whr['Region'] == 'Middle East and Northern Africa']
whr_SEA = whr[whr['Region'] == 'Southeastern Asia']
whr_SA = whr[whr['Region'] == 'Southern Asia']


# In[20]:


len(whr_SSA[whr_SSA['Happiness Score'] > 6])


# In[21]:


print("There are {} countries in Sub-Saharan Africa that have a happiness score above 6.0 ".format(len(whr_SSA[whr_SSA['Happiness Score'] > 6])))


# In[22]:


Delta_SSA = whr_SSA.max(axis=0)['Happiness Score'] - whr_SSA.min(axis=0)['Happiness Score']
print(Delta_SSA)


# In[23]:


len(whr_WE[whr_WE['Happiness Score'] > 6])


# In[24]:


print("There are {} countries in Western Europe that have a happiness score above 6.0 ".format(len(whr_WE[whr_WE['Happiness Score'] > 6])))


# In[25]:


Delta_WE = whr_WE.max(axis=0)['Happiness Score'] - whr_WE.min(axis=0)['Happiness Score']
print(Delta_WE)


# In[26]:


len(whr_CEE[whr_CEE['Happiness Score'] > 6])


# In[27]:


print("There is {} country in Central and Eastern Europe that has a happiness score above 6.0 ".format(len(whr_CEE[whr_CEE['Happiness Score'] > 6])))


# In[28]:


Delta_CEE = whr_CEE.max(axis=0)['Happiness Score'] - whr_CEE.min(axis=0)['Happiness Score']
print(Delta_CEE)


# In[29]:


len(whr_NA[whr_NA['Happiness Score'] > 6])


# In[30]:


print("There are {} countries in the North America that have a happiness score above 6.0 ".format(len(whr_NA[whr_NA['Happiness Score'] > 6])))


# In[31]:


Delta_NA = whr_NA.max(axis=0)['Happiness Score'] - whr_NA.min(axis=0)['Happiness Score']
print(Delta_NA)


# In[32]:


len(whr_ANZ[whr_ANZ['Happiness Score'] > 6])


# In[33]:


print("There are {} countries in the Australia and New Zealand that have a happiness score above 6.0 ".format(len(whr_ANZ[whr_ANZ['Happiness Score'] > 6])))


# In[34]:


Delta_ANZ = whr_ANZ.max(axis=0)['Happiness Score'] - whr_ANZ.min(axis=0)['Happiness Score']
print(Delta_ANZ)


# In[35]:


len(whr_LAC[whr_LAC['Happiness Score'] > 6])


# In[36]:


print("There are {} countries in the Latin America and Caribbean that have a happiness score above 6.0 ".format(len(whr_LAC[whr_LAC['Happiness Score'] > 6])))


# In[37]:


Delta_LAC = whr_LAC.max(axis=0)['Happiness Score'] - whr_LAC.min(axis=0)['Happiness Score']
print(Delta_LAC)


# In[38]:


len(whr_EA[whr_EA['Happiness Score'] > 6])


# In[39]:


print("There are {} countries in the Eastern Asia that have a happiness score above 6.0 ".format(len(whr_EA[whr_EA['Happiness Score'] > 6])))


# In[40]:


Delta_EA = whr_EA.max(axis=0)['Happiness Score'] - whr_EA.min(axis=0)['Happiness Score']
print(Delta_EA)


# In[41]:


len(whr_MENA[whr_MENA['Happiness Score'] > 6])


# In[42]:


print("There are {} countries in the Middle East and Northern Africa that have a happiness score above 6.0 ".format(len(whr_MENA[whr_MENA['Happiness Score'] > 6])))


# In[43]:


Delta_MENA = whr_MENA.max(axis=0)['Happiness Score'] - whr_MENA.min(axis=0)['Happiness Score']
print(Delta_MENA)


# In[44]:


len(whr_SEA[whr_SEA['Happiness Score'] > 6])


# In[45]:


print("There are {} countries in the Southeastern Asia that have a happiness score above 6.0 ".format(len(whr_SEA[whr_SEA['Happiness Score'] > 6])))


# In[46]:


Delta_SEA = whr_SEA.max(axis=0)['Happiness Score'] - whr_SEA.min(axis=0)['Happiness Score']
print(Delta_SEA)


# In[47]:


len(whr_SA[whr_SA['Happiness Score'] > 6])


# In[48]:


print("There are {} countries in the Southern Asia that have a happiness score above 6.0 ".format(len(whr_SA[whr_SA['Happiness Score'] > 6])))


# In[49]:


Delta_SA = whr_SA.max(axis=0)['Happiness Score'] - whr_SA.min(axis=0)['Happiness Score']
print(Delta_SA)


# In[50]:


Deltas = {}


# In[51]:


Deltas["Sub-Saharan Africa"] = Delta_SSA
Deltas["Southern Asia"] = Delta_SA
Deltas["Western Europe"] = Delta_WE
Deltas["Middle East and Northern Africa"] = Delta_MENA
Deltas["North America"] = Delta_NA
Deltas["Central and Eastern Europe"] = Delta_CEE
Deltas["Australia and New Zealand"] = Delta_ANZ
Deltas["Latin America and Caribbean"] = Delta_LAC
Deltas["Eastern Asia"] = Delta_EA
Deltas["Southeastern Asia"] = Delta_SEA


# In[52]:


print("The {} region seems to have the largest range of happiness scores".format(max(Deltas, key=Deltas.get)))


# ### C. Bar plot of the Happiness Score
# 
# * Obtain a horizontal bar plot of the Happiness Score of the top 10 countries. Your bar chart should have the names of the countries are listed vertically along the y-axis and the x-axis should have labels for each number from 0 to 8. Ensure that the chart has an appropriate title and labels.
# * You will now modify the bar chart you obtained in step 1 to turn into a stacked bar chart where the overall happiness score is divided into the seven parts corresponding to the columns:
# * Economy
# * Family
# * Health
# * Freedom
# * Generosity
# * Corruption
# * Dystopia
# * Choose a distinct color for each category and include an appropriate legend with your chart.
# * Obtain the same stacked horizontal bar chart as in step 2 but this time instead of the top 10 countries consider all countries from the region Africa.

# In[53]:


whr['Happiness Score'].head(10).plot(xticks=np.arange(9), kind='barh', figsize= (10, 10))
plt.xlabel("Happiness Score")
plt.title('Happiness Score of the top 10 Countries')


# In[54]:


whr[['Economy (GDP per Capita)','Family','Health (Life Expectancy)','Freedom','Trust (Government Corruption)','Generosity','Dystopia Residual']].head(10).plot(kind='barh',
                                                                xticks=np.arange(9), stacked=True, figsize= (10, 10))

plt.xlabel("Happiness Score")
plt.title('Happiness Score of the top 10 Countries')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[55]:


whr_SSA[['Economy (GDP per Capita)','Family','Health (Life Expectancy)','Freedom','Trust (Government Corruption)','Generosity','Dystopia Residual']].head(10).plot(kind='barh',
                                                                xticks=np.arange(9), stacked=True, figsize= (10, 10))

plt.xlabel("Happiness Score")
plt.title('Happiness Score of the top 10 Countries')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# ### D. Pairwise Scatter plots
# 
# * Obtain scatter plots of the Happiness Score versus each of the other variables. Your plots should be displayed as multiple plots table and obtained with one command as supposed to separate commands for each plot.

# In[56]:


sns.pairplot(data=whr, kind='reg', size = 5,
                  x_vars=['Happiness Score'],
                  y_vars=['Economy (GDP per Capita)','Family','Health (Life Expectancy)','Freedom','Trust (Government Corruption)','Generosity','Dystopia Residual'])


# In[57]:


sns.pairplot(data = whr, height = 5, hue = 'Region',
                  x_vars=['Happiness Score'],
                  y_vars=['Economy (GDP per Capita)','Family','Health (Life Expectancy)','Freedom','Trust (Government Corruption)','Generosity','Dystopia Residual'])


# ### E. Correlation
# 
# * Obtain the correlation between the Happiness Score and each of the other variables. Which variable has the highest correlation with the Happiness Score?

# In[58]:


whr.corr(method="pearson", min_periods=20)["Happiness Score"].sort_values(ascending=False)


# In[59]:


whr.corr(method="pearson", min_periods=20)["Happiness Score"].abs().sort_values(ascending=False)


# In[60]:


whr.corr(method="pearson", min_periods=20)


# In[61]:


corr = whr.corr(method = "pearson")

f, ax = plt.subplots(figsize=(10, 10))

sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), 
            cmap=sns.diverging_palette(220, 10, as_cmap=True), square=True, ax=ax)


# ### F. Probabilities
# 
# * Compute the probability that randomly selected country with Happiness score over 6.0 is from Western Europe. You will have to use pandas to count the appropriate quantities.

# In[62]:


whr[whr['Happiness Score'] > 6].shape[0]


# In[63]:


whr[(whr['Happiness Score'] > 6) & (whr['Region'] == 'Western Europe')].shape[0]


# In[64]:


float(len(whr[(whr['Happiness Score'] > 6) & (whr['Region'] == 'Western Europe')]))/float(len(whr[whr['Happiness Score'] > 6]))


# In[65]:


print("The probability that a randomly selected country with happiness score over 6.0 is form Western Europe is {0:.0%}".format(float(whr[(whr['Happiness Score'] > 6) & (whr['Region'] == 'Western Europe')].shape[0]

)/float(whr[whr['Happiness Score'] > 6].shape[0])))

