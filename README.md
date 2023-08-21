# datawindow
# Simplifying Data Processing and Analysis in Python
![image](https://github.com/DL4150/datawindow/assets/92887753/61ff77c2-f93b-40c6-bee1-131d578807c1)


**datawindow** is a comprehensive Python library designed to streamline and simplify the entire data manipulation and analysis workflow. With its intuitive classes and interactive interface, dsmate empowers users to effortlessly handle various data-related tasks, making data preparation, exploration, visualization, and machine learning model creation more accessible than ever before.

## Features:

1. **dfclean: Tackle Data Cleaning with Ease**

   The `dfclean` class offers a powerful solution for managing missing data, handling outliers, scaling features, and categorizing data. Effortlessly preprocess your datasets to ensure they are primed for analysis.

   Syntax Example:
   ```python
   from datawindow import dfclean
   window=dfclean(dataframe)
   clean_df=window.clean()

2. **dfsum: Gain Deeper Insights with Data Summarization**

   Uncover the essence of your data using the `dfsum` class. This functionality allows you to quickly grasp the essential statistics and characteristics of your datasets, facilitating better decision-making.

   **Syntax Example:**

   ```python
   from datawindow import dfsum
   window=dfsum(dataframe) # summarize the dataframe and understand more about it


3. **dfviz: Visualize Data for Enhanced Understanding**
   
   The `dfviz` class empowers you to visualize each column in your dataset through a variety of charts, enabling you to grasp patterns, trends, and correlations with ease. Transform raw data into meaningful insights..

   **Syntax Example:**

   ```python
   from datawindow import dfviz
   window=dfviz(dataframe) # plot the columns of the dataframe 

4. **dfload: Simplified Loading of Large Datasets**
   
   With the `dfload` class, effortlessly load and convert a multitude of files into dataframes. Save time and resources while working with extensive datasets, making the data loading process seamless..

   **Syntax Example:**

   ```python
   from datawindow import dfload
   window=dfload() #only accepts csv and excel files
   dataframes=window.dataframes # get back a list of dataframes selected

5. **ml_model: Effortless Machine Learning Model Creation**
   
   Create and assess machine learning models effortlessly using the `ml_model` class. Gauge the performance of your models with various algorithms, facilitating informed decision-making in your data-driven projects..

   **Syntax Example:**

   ```python
   from datawindow import ml_model
   window=ml_model(X,y,split=0.25,randomness=0,type=0)
   # X- the independent features as dataframe
   # y- dependent or target feature as dataframe
   # split- percentage of how the dataset is split in training and test set; default value is 0.25
   # randomness- how the rows are divided in the dataset, default is 0
   # type- 0 for classification; default value
   #     - 1 for regression
   model=window.model # returns the trained model
   

## Interactive Interface for Enhanced User Experience:

dsmate introduces an interactive interface that leverages windows to provide users with a more engaging and user-friendly environment. This interface streamlines your workflow, allowing you to seamlessly interact with your data, perform tasks, and analyze results in a dynamic and intuitive manner.

Whether you're a data scientist, analyst, or enthusiast, dsmate is your trusted companion for simplifying the complex world of data manipulation and analysis. Say goodbye to tedious processes and hello to efficiency and insight with dsmate.

Discover the future of data processing and analysis – get started with dsmate today and experience the difference firsthand.
Feel free to use this Markdown-formatted text for your needs!
 # Template for building a model with ease
 ```python
from datawindow import dfclean,dfsum,dfviz,ml_model,dfload
window=dfload()
dataframe=window.dataframes[0]
window=dfsum(dataframe)
window=dfviz(dataframe)
window=dfclean(dataframe)
clean_df=window.clean()
window=ml_model(X,y,split=0.25,randomness=0,type=0)
model=window.model
