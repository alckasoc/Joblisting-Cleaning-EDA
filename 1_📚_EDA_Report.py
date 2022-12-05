# Imports.
import streamlit as st
import numpy as np
import pandas as pd
import cv2
 
# Page config.
st.set_page_config(
    page_title="Diving into Data Science Jobs",
    page_icon=":books:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# This is a header. This is an *extremely* cool app!",
    }
)

# Banner.
image = cv2.cvtColor(cv2.imread("./img/banner/banner_cropped.png"), cv2.COLOR_BGR2RGB)
st.image(image)

# Title.
st.title("Diving into Data Science Jobs")

# Table of contents.
st.markdown("\
**Table of Contents**: <br>\
\
<ul>\
    <li>1. <a href=\"#1-introduction\">Introduction</a></li>\
    <li>2. <a href=\"#2-cleaning\">Cleaning</a></li>\
    <li>3. <a href=\"#3-eda\">Exploratory Data Analysis (EDA)</a>\
        <ul>\
            <li>3.1. <a href=\"#3-1-a-univariate-look\">A Univariate Look</a></li>\
            <li>3.2. <a href=\"#3-2-a-multivariate-dive\">A Multivariate Dive</a></li>\
            <li>3.3. <a href=\"#3-3-a-free-form-exploration\">A Free-form Exploration</a></li>\
        </ul>\
    </li>\
    <li>4. <a href=\"#4-conclusion\">Conclusion</a></li>\
</ul>\
", unsafe_allow_html=True)

# 1. Introduction.
st.markdown("## 1. Introduction")

st.write("\
    This project tackled 2 tasks within the data science lifecycle: cleaning & exploring data.\
    A table of contents is provided to direct you. I've organized the sections in this EDA\
    report the same way I organized my project process. After this introduction,\
    I cover my cleaning process and the reasoning behind my process. Then, I cover the\
    the EDA which is broken down into 3 sections: univariate, multivariate, free-form.\
    Finally, I wrap up this report with a conclusion. I'm really happy with how this\
    project turned out. I hope you enjoy it!\
    \
")

st.write("\
    PS: As a small note, (columns ≡ features ≡ variables) and (rows ≡ instances ≡ joblistings).\
")

# 2. Cleaning.
st.markdown("## 2. Cleaning")

image = cv2.cvtColor(cv2.imread("./diagrams/joblisting_EDA_cleaning_pipeline.png"), cv2.COLOR_BGR2RGB)
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
st.image(image)
st.caption("Figure 1. Cleaning Pipeline.")

st.markdown("\
    Data was webscraped from my [Joblisting Webscraper](https://github.com/alckasoc/Joblisting-Webscraper) project.\
    I scraped data on 3 separate occasions (these were all scraped in close time proximity to one another in roughly\
    March of 2021 when I began this project). I accumulated a little over two thousand instances.\
    Being real-world data, this dataset was extremely unclean! Some features were lumped together (company and rating).\
    There were lots of NaNs. Joblistings on Glassdoor have multiple optional input fields and\
    scraping those often yielded a good amount of NaNs. Some string features were representing\
    numerical values (like revenue and salary estimate). Different columns also had different ways\
    of representing a NaN. Some represented as \"-1\" and some as \"unknown\".\
")

st.markdown("\
    From the figure, I divided my cleaning pipeline into multiple modularized components (all of which\
    can be easily expanded upon) to handle each feature.\
    In addition to what's already evident from the figure, I decided to remove rows with five\
    or more NaNs because these joblistings were unsalvageable!\
    I also realized that the \"headquarters\" column had a mix up with the job title and the\
    \"company\" column had a few non-company name strings.\
    The \"revenue\" column had a huge amount of unknowns (NaNs) (~25\% of the data), but I decided to keep the column because non-reporting may be interesting to look into.\
    Finally, I noticed quite a few joblistings were from the same company but with a different\
    spelling for the company name. I included a grouper function to fix this.\
")

# 3. EDA
st.markdown("## 3. EDA")

st.write("The following sections concern exploratory data analysis! Both univariate and\
    multivariate sections are divided into non-graphical and graphical.\
")

# 3.1. A Univariate Look.
st.markdown("### 3.1. A Univariate Look")

df = pd.read_csv("./csv/describe.csv")
st.dataframe(df)
st.caption("Figure 2. Descriptive statistics about rating and salary estimate.")

st.write("\
    Average rating is 4.1 with a minimum at 2.1 and a maximum of 5.0. Average salary\
    estimate is around \$133k to \$135k\ with the minimum at \$24.5k and the maximum at \$209k.\
    \
    \
    \
    \
    \
    \
")

image = cv2.cvtColor(cv2.imread("./img/prop.png"), cv2.COLOR_BGR2RGB)
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
st.image(image)
st.caption("Figure 3. Proportions of unique companies w.r.t joblistings.")

# 3.2. A Multivariate Dive.
st.markdown("### 3.2. A Multivariate Dive")

# 3.3. A Free-form Exploration.
st.markdown("### 3.3. A Free-form Exploration")

# 4. Conclusion.
st.markdown("## 4. Conclusion")
