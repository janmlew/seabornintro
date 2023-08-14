# -*- coding: utf-8 -*-
"""DC: Intro to Data Visualization with Seaborn

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12ZqbrOxFYXqAArxtInzkp2PrX58l-wiw

Imports.
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#import datetime

"""Data apprehension."""

# global variables
#PATH='/content/drive/MyDrive/Colab Notebooks/Project/datasets/' Unnecessary in PyCharm.

# Google Drive mount
# drive.mount('/content/drive', force_remount=True)

# Loads
country_data = pd.read_csv('countries-of-the-world.csv', index_col='Country') #, parse_dates=['date'], index_col='date')
mpg = pd.read_csv('mpg.csv')
student_data = pd.read_csv('student-alcohol-consumption.csv', index_col=0)
survey_data = pd.read_csv('young-people-survey-responses.csv', index_col=0)

# Data preparation:
#austin_weather = austin_weather.rename(columns={'DATE':'MONTH'})
#austin_weather = austin_weather.replace({'MONTH': {1: 'Jan', 2: 'Feb', 3: 'Apr', 4: 'Mar', 5: 'May', 6: 'June', 7: 'July', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}})
#seattle_weather = seattle_weather.rename(columns={'DATE':'MONTH'})
#seattle_weather_all = seattle_weather.replace({'MONTH': {1: 'Jan', 2: 'Feb', 3: 'Apr', 4: 'Mar', 5: 'May', 6: 'June', 7: 'July', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}})
#seattle_weather = seattle_weather_all[0:12]
#mens_rowing = summer2016[summer2016['Sport']=='Rowing']
#mens_gymnastics = summer2016[summer2016['Sport']=='Gymnastics']
# Index data type conversion from object to Datetime; unnecesary since data load update above.
# climate_change.index = pd.to_datetime(climate_change.index)

"""Exercise 1.

Making a scatter plot with lists

In this exercise, we'll use a dataset that contains information about 227 countries. This dataset has lots of interesting information on each country, such as the country's birth rates, death rates, and its gross domestic product (GDP). GDP is the value of all the goods and services produced in a year, expressed as dollars per person.

We've created three lists of data from this dataset to get you started. gdp is a list that contains the value of GDP per country, expressed as dollars per person. phones is a list of the number of mobile phones per 1,000 people in that country. Finally, percent_literate is a list that contains the percent of each country's population that can read and write.

* Import Matplotlib and Seaborn using the standard naming convention.
* Create a scatter plot of GDP (gdp) vs. number of phones per 1000 people (phones).
* Display the plot.
* Change the scatter plot so it displays the percent of the population that can read and write (percent_literate) on the y-axis.
"""

# Preparation of variables:

gdp = country_data['GDP ($ per capita)']
phones = country_data['Phones (per 1000)']
percent_literate = country_data['Literacy (%)']

# The exercise itself (excluding imports!):

sns.scatterplot(x=gdp, y=phones)
plt.show()

sns.scatterplot(x=gdp, y=percent_literate)
plt.show()

"""Exercise 2.

Making a count plot with a list

In the last exercise, we explored a dataset that contains information about 227 countries. Let's do more exploration of this data - specifically, how many countries are in each region of the world?

To do this, we'll need to use a count plot. Count plots take in a categorical list and return bars that represent the number of list entries per category. You can create one here using a list of regions for each country, which is a variable named region.

* Import Matplotlib and Seaborn using the standard naming conventions.
* Use Seaborn to create a count plot with region on the y-axis.
* Display the plot.
"""

# Preparation of variables:
region = country_data['Region']

# The exercise itself (excluding imports!):
sns.countplot(y=region)
plt.show()

"""Lecture code on "Using pandas with Seaborn:

# This is bullshit!
"""

# import pandas as pd <- repetitive

sns.countplot(x='location', data=student_data)

plt.show()

"""Exercise 3.

Making a count plot with a DataFrame

In this exercise, we'll look at the responses to a survey sent out to young people. Our primary question here is: how many young people surveyed report being scared of spiders? Survey participants were asked to agree or disagree with the statement "I am afraid of spiders". Responses vary from 1 to 5, where 1 is "Strongly disagree" and 5 is "Strongly agree".

To get you started, the filepath to the csv file with the survey data has been assigned to the variable csv_filepath.

Note that because csv_filepath is a Python variable, you will not need to put quotation marks around it when you read the csv.

* Import Matplotlib, pandas, and Seaborn using the standard names.
* Create a DataFrame named df from the csv file located at csv_filepath.
* Use the countplot() function with the x= and data= arguments to create a count plot with the "Spiders" column values on the x-axis.
* Display the plot.

# Adding fucking plt.show() as a separate task EVERY FUCKING TIME. In reality, one exercise has only one or two (at most) meaningful tasks.
"""

# Import Matplotlib, pandas, and Seaborn
#import matplotlib.pyplot as plt
#import pandas as pd
#import seaborn as sns

# Create a DataFrame from csv file
#df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x='Spiders', data=survey_data)

# Display the plot
plt.show()

"""Hue and scatter plots

In the prior video, we learned how hue allows us to easily make subgroups within Seaborn plots. Let's try it out by exploring data from students in secondary school. We have a lot of information about each student like their age, where they live, their study habits and their extracurricular activities.

For now, we'll look at the relationship between the number of absences they have in school and their final grade in the course, segmented by where the student lives (rural vs. urban area).

* Create a scatter plot with "absences" on the x-axis and final grade ("G3") on the y-axis using the DataFrame student_data. Color the plot points based on "location" (urban vs. rural).
* Make "Rural" appear before "Urban" in the plot legend.
"""

# Import Matplotlib and Seaborn
#import matplotlib.pyplot as plt
#import seaborn as sns

# Create a scatter plot of absences vs. final grade
sns.scatterplot(x='absences', y='G3', data=student_data, hue='location', hue_order=['Rural', 'Urban'])
plt.show()

"""Hue and count plots

Let's continue exploring our dataset from students in secondary school by looking at a new variable. The "school" column indicates the initials of which school the student attended - either "GP" or "MS".

In the last exercise, we created a scatter plot where the plot points were colored based on whether the student lived in an urban or rural area. How many students live in urban vs. rural areas, and does this vary based on what school the student attends? Let's make a count plot with subgroups to find out.

* Fill in the palette_colors dictionary to map the "Rural" location value to the color "green" and the "Urban" location value to the color "blue".
* Create a count plot with "school" on the x-axis using the student_data DataFrame.
 * Add subgroups to the plot using "location" variable and use the palette_colors dictionary to make the location subgroups green and blue.
"""

# Create a dictionary mapping subgroup values to colors
palette_colors = {'Rural': "green", 'Urban': "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x='school', data=student_data, hue='location', palette=palette_colors)
plt.show()

"""Creating subplots with col and row

We've seen in prior exercises that students with more absences ("absences") tend to have lower final grades ("G3"). Does this relationship hold regardless of how much time students study each week?

To answer this, we'll look at the relationship between the number of absences that a student has in school and their final grade in the course, creating separate subplots based on each student's weekly study time ("study_time").

Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt.

* Modify the code to use relplot() instead of scatterplot().
* Modify the code to create one scatter plot for each level of the variable "study_time", arranged in columns.
* Adapt your code to create one scatter plot for each level of a student's weekly study time, this time arranged in rows.
"""

# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3",
            data=student_data,
            kind="scatter",
            col="study_time")
plt.show()

sns.relplot(x="absences", y="G3",
            data=student_data,
            kind="scatter",
            row="study_time")
plt.show()

"""Creating two-factor subplots

Let's continue looking at the student_data dataset of students in secondary school. Here, we want to answer the following question: does a student's first semester grade ("G1") tend to correlate with their final grade ("G3")?

There are many aspects of a student's life that could result in a higher or lower final grade in the class. For example, some students receive extra educational support from their school ("schoolsup") or from their family ("famsup"), which could result in higher grades. Let's try to control for these two factors by creating subplots based on whether the student received extra educational support from their school or family.

Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt.

* Use relplot() to create a scatter plot with "G1" on the x-axis and "G3" on the y-axis, using the student_data DataFrame.
* Create column subplots based on whether the student received support from the school ("schoolsup"), ordered so that "yes" comes before "no".
* Add row subplots based on whether the student received support from the family ("famsup"), ordered so that "yes" comes before "no". This will result in subplots based on two factors.
"""

sns.relplot(x="G1", y="G3",
            data=student_data,
            kind="scatter",
            col="schoolsup",
            row='famsup',
            col_order=["yes", "no"],
            row_order=["yes", "no"])
plt.show()

"""Changing the size of scatter plot points

In this exercise, we'll explore Seaborn's mpg dataset, which contains one row per car model and includes information such as the year the car was made, the number of miles per gallon ("M.P.G.") it achieves, the power of its engine (measured in "horsepower"), and its country of origin.

What is the relationship between the power of a car's engine ("horsepower") and its fuel efficiency ("mpg")? And how does this relationship vary by the number of cylinders ("cylinders") the car has? Let's find out.

Let's continue to use relplot() instead of scatterplot() since it offers more flexibility.

* Use relplot() and the mpg DataFrame to create a scatter plot with "horsepower" on the x-axis and "mpg" on the y-axis. Vary the size of the points by the number of cylinders in the car ("cylinders").
* To make this plot easier to read, use hue to vary the color of the points by the number of cylinders in the car ("cylinders").
"""

sns.relplot(x='horsepower', y='mpg', data=mpg, size='cylinders', kind='scatter', hue='cylinders')
plt.show()
sns.relplot(x='acceleration', y='mpg', data=mpg, style='origin', kind='scatter', hue='origin')
plt.show()

sns.relplot(x='model_year', y='mpg', data=mpg, kind='line') #mean with confidence interval
plt.show()
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line", ci='sd') #mean with standard deviation
plt.show()
sns.relplot(x='model_year', y='horsepower', data=mpg, kind='line', ci=None)
plt.show()
sns.relplot(x="model_year", y="horsepower",
            data=mpg, kind="line",
            ci=None, style='origin',
            hue='origin')
plt.show()
sns.relplot(x="model_year", y="horsepower",
            data=mpg, kind="line",
            ci=None, style="origin",
            hue="origin", markers=True,
            dashes=False)
plt.show()

"""Categorical plots :)"""

sns.catplot(x="Internet usage", data=survey_data,
            kind="count")
plt.show()

#Data preparation:
age_cat = []
for i in survey_data['Age']:
  if i >= 21:
    age_cat.append(str('21+'))
  elif i < 21:
    age_cat.append('Less than 21')
  else:
    age_cat.append(None)
survey_data['Age Category']=age_cat
#Code:
sns.catplot(y="Internet usage", data=survey_data, kind="count", col='Age Category')
plt.show()

#sns.catplot(y="Interested in Math", x="Gender", data=survey_data, kind='bar')
#plt.show()

category_order = ["<2 hours",
                  "2 to 5 hours",
                  "5 to 10 hours",
                  ">10 hours"]
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=category_order,
            ci=None)
plt.show()

study_time_order = ["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"]
sns.catplot(x='study_time', y='G3', data=student_data, kind='box', order=study_time_order)
plt.show()

sns.catplot(x='internet', y='G3', data=student_data, kind='box', hue='location', sym='')
plt.show()

sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box", whis=0.5)
plt.show()

sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box", whis=[5, 95])
plt.show()

sns.catplot(x='famrel', y='absences', data=student_data, kind='point')
plt.show()
sns.catplot(x='famrel', y='absences', data=student_data, kind='point', capsize=0.2, join=False)
plt.show()

sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None, estimator=np.median)
plt.show()

"""Styles."""

#sns.set_style("whitegrid")
#sns.set_palette("RdBu")
#sns.set_palette("#39A7D0", "#36ADA4")
#sns.set_context("paper")
#sns.set_context("notebook")
#category_order = ["Never", "Rarely", "Sometimes",
#                  "Often", "Always"]
#sns.catplot(x="Parents Advice",
#            data=survey_data,
#            kind="count",
#            order=category_order)
#plt.show()

g = sns.relplot(x="weight",
                y="horsepower",
                data=mpg,
                kind="scatter")
g.fig.suptitle('Car Weight vs. Horsepower')
plt.show()

type_of_g = type(g)
print(type_of_g)

#g = sns.lineplot(x="model_year", y="mpg_mean", data=mpg_mean, hue="origin")
#g.set_title("Average MPG Over Time")
#g.set(xlabel='Car Model Year', ylabel='Average MPG')
#plt.show()