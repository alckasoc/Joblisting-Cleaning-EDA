![](https://github.com/alckasoc/Joblisting-Cleaning-EDA/blob/main/img/banner/banner.png?raw=true)

# Joblisting Cleaning & Exploratory Data Analysis (EDA)

A cleaning and Exploratory Data Analysis (EDA) data science project on the data science joblistings scraped from the Joblisting Webscraper project!

## Table of Contents

- [Motivation](https://github.com/alckasoc/Joblisting-Cleaning-EDA/blob/main/README.md#motivation)
- [Structure](https://github.com/alckasoc/Joblisting-Cleaning-EDA/blob/main/README.md#structure)
- [Dataset](https://github.com/alckasoc/Joblisting-Cleaning-EDA/blob/main/README.md#dataset)
- [Difficulties](https://github.com/alckasoc/Joblisting-Cleaning-EDA/blob/main/README.md#difficulties)
- [What I Learned](https://github.com/alckasoc/Joblisting-Cleaning-EDA/blob/main/README.md#what-i-learned)
- [References](https://github.com/alckasoc/Joblisting-Cleaning-EDA/blob/main/README.md#references)
- [Author Info](https://github.com/alckasoc/Joblisting-Cleaning-EDA/blob/main/README.md#author-info)


## Motivation

My motivation for this project was three-pronged. Firstly, I wanted to perform exploratory knowledge analysis with what I have learned. Secondly, I wanted to venture into the unknown! I wanted to dive deeper into EDA (which I have never really done before in my collection of [Learning ML Projects](https://github.com/alckasoc/LearningML-Projects)). Lastly, the EDA project can provide a comprehensive exploration in job market demographics for data scientist job offerings. :)

## Structure

![](https://github.com/alckasoc/Joblisting-Cleaning-EDA/blob/main/diagrams/pipeline_diagram.PNG?raw=true)\
Figure 1. Data science lifecycle. 
<br/><br/>

This project is part of a *larger* project! This is only 1 step in that larger project. To check out the other projects in this series:
1. [Joblisting-Webscraper](https://github.com/alckasoc/Joblisting-Webscraper)
2. [Joblisting-Cleaning-EDA](https://github.com/alckasoc/Joblisting-Cleaning-EDA)
3. More to come!

About the structure of this repo:
* `csv` stores the CSVs I generated for this project
* `diagrams` stores my diagrams
* `img` stores images from EDA, auto-EDA, and the banner for my app
* `input` stores the dataset I scraped
* `pages` stores the subpage for my app
* `sheets` stores the spreadsheet I use to organize my EDA process
* `1_📚_EDA_Report.py` is the main page of my app
* `banner.ipynb` is a short notebook with code that generated the images I used for my banner
* `cleaning.ipynb` is my cleaning notebook and pipeline
* `eda.ipynb` is my EDA notebook


## Dataset

A little about the dataset: the data was webscraped from Glassdoor.com's job listings for data science jobs. I used my own webscraper for it! That can be found here: https://github.com/alckasoc/Joblisting-Webscraper. The dataset is small and can be found in this repo under `input`. As an alternative, I've also stored this on Kaggle publicly: https://www.kaggle.com/datasets/vincenttu/glassdoor-joblisting.

## Difficulties

- I struggled with structuring this project! There were so many things to include or think about that I spent a good deal of time thinking about the infrastructure of my project. One example was figuring out how to structure the main dataframes and the edit log for convenience and readability. I finally solved this issue after a long mental discussion and came up with a design (specified in the project).
- One difficulty (as I am working on the project now) is the interpretation! I've interpreted different transformations on a df before, but, as I write these chains of complex functions, I realize that interpretation soon grows a bit more complex! I've spent countless hours interpreting and stepping through transformations.
- Another difficulty, this one I encountered in data wrangling and cleaning, was deciding on how to impute the data and how to interpret and create thresholds for keeping or deleting features and rows. Because of the many imputation methods and the context in which imputing needs to be considered in, data cleaning took a bit of time!

## What I Learned

- Imbalanced Learn
    - Imbalanced-learn is a great library for tackling over/under sampling problems playing off of scikit-learns name!
- Pandas profiling
    - pandas profiling is a comprehensive pandas tool for analyzing dataframes (summary statistics and graphs).
- EDA structure
    - As messy as EDA can be, there needs to be some imposed structure for people to follow your line of thought!
- Google Spreadsheet
- Data Science Analysis
    - Analysis can take many forms and it's often an umbrella term. Analyzing large quantities of data means effectively aggregating findings and results. This project I've split analyses into 2 categories: breadth and depth. The first paradigm of analyses seeks to get comfortable with the data and probe it. The second seeks to answer specific questions and dive *deeper* into the data.
- Asking the right questions!
    

## References

- The [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/) was extremely helpful in deciphering functions and searching for functions.
- [Ken Jee's End-to-End Data Science Project](https://www.youtube.com/watch?v=QWgg4w1SpJ8&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t&index=4&ab_channel=KenJeeKenJeeVerified) provided me an idea of how to approach the data science lifecycle and greatly inspired this series of projects!
- [Data Professor's Exploratory Data Analysis Walkthrough](https://www.youtube.com/watch?v=9m4n2xVzk9o) gave me a sense of the data visualizations and aggregations expected in an EDA project.
- Professor Meyer's [Intro to EDA](https://www.youtube.com/watch?v=zHcQPKP6NpM) equipped me with a refresh of what statistics and data visualization graphs are typically used in this workflow. 
- Pedro Marcelino's [Kaggle Kernel on EDA](https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python) was a great help in structuring my project (also introduced me to the logarithmic transformation trick).
- [Data Professor's Pandas Profiling](https://www.youtube.com/watch?v=Ef169VELt5o&ab_channel=DataProfessorDataProfessor) video helped immensely with introducing a quick and easy tool to break through to the EDA world.
- Yet again, [Data Professor's Imbalanced Learn](https://www.youtube.com/watch?v=4SivdTLIwHc) tutorial introduced me to a few sampling techniques that would help with imbalanced datasets.
- Railsware Product Academy's video on [Google Sheets](https://www.youtube.com/watch?v=FIkZ1sPmKNw&t=481s) familiarized me with simple navigation and cell editing.
- This Github issue on [typing the dollar sign in markdown](https://github.com/jupyter/notebook/issues/1080) was something new I learned.
- This [article](https://towardsdatascience.com/6-different-ways-to-compensate-for-missing-values-data-imputation-with-examples-6022d9ca0779) and this [video](https://www.youtube.com/watch?v=fYhr8eF1ubo) on different ways to impute missing data helped in finding new ways to impute the NaNs I had.
- I borrowed Aurélien Geron's save_fig() function from [this](https://github.com/ageron/handson-ml2/blob/master/04_training_linear_models.ipynb).
- [Yan Holtz's website](https://www.python-graph-gallery.com/cheat-sheets/) on different types of graphs was extremely helpful!

## Author Info

Contact me:

Gmail: tuvincent0106@gmail.com\
Linkedin: [Vincent Tu](https://www.linkedin.com/in/vincent-tu-422b18208/)
