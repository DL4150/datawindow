from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = """
Simplify data tasks in Python with interactive interface for effortless data interaction. Empower your data journey today.
"""
LONG_DESCRIPTION = """
Introducing datawindow: Simplifying Data Processing and Analysis in Python

datawindow is a comprehensive Python library designed to streamline and simplify the entire data manipulation and analysis workflow. With its intuitive classes and interactive interface, datawindow empowers users to effortlessly handle various data-related tasks, making data preparation, exploration, visualization, and machine learning model creation more accessible than ever before.


** NOTE: datawindow works on locally run set ups like python on your desktop, jupyter on your desktop, etc.** 

** Jupyter notebook on local device is best**


Key Features:

1. dfclean: Tackle Data Cleaning with Ease
   The dfclean class offers a powerful solution for managing missing data, handling outliers, scaling features, and categorizing data. Effortlessly preprocess your datasets to ensure they are primed for analysis.

2. dfsum: Gain Deeper Insights with Data Summarization
   Uncover the essence of your data using the dfsum class. This functionality allows you to quickly grasp the essential statistics and characteristics of your datasets, facilitating better decision-making.

3. dfviz: Visualize Data for Enhanced Understanding
   The dfviz class empowers you to visualize each column in your dataset through a variety of charts, enabling you to grasp patterns, trends, and correlations with ease. Transform raw data into meaningful insights.

4. dfload: Simplified Loading of Large Datasets
   With the dfload class, effortlessly load and convert a multitude of files into dataframes. Save time and resources while working with extensive datasets, making the data loading process seamless.

5. ml_model: Effortless Machine Learning Model Creation
   Create and assess machine learning models effortlessly using the ml_model class. Gauge the performance of your models with various algorithms, facilitating informed decision-making in your data-driven projects.

6. dl_model: Effortless Basic Deep Learning Model Creation
   Create and assess Deep learning models effortlessly using the dl_model class. Gauge the performance of your models with various structures, facilitating informed decision-making in your data-driven projects.

7. clust_model: Effortless Basic Deep Learning Model Creation
   By utilizing this technique, the function offers valuable insights into determining the ideal number of clusters, their arrangement within a dataset and creating a clustering model.

8. model_check: Comprehensive Model Performance Evaluation
   serves as a versatile tool for evaluating and comparing the performance of a predefined list of models on a specific dataset. It facilitates a systematic assessment of each model's efficacy, enabling data practitioners to make informed choices about model selection and deployment strategies. By quantitatively measuring how well different models fit the data, the function aids in optimizing decision-making processes related to model implementation.

Interactive Interface for Enhanced User Experience:

datawindow introduces an interactive interface that leverages windows to provide users with a more engaging and user-friendly environment. This interface streamlines your workflow, allowing you to seamlessly interact with your data, perform tasks, and analyze results in a dynamic and intuitive manner.

Whether you're a data scientist, analyst, or enthusiast, datawindow is your trusted companion for simplifying the complex world of data manipulation and analysis. Say goodbye to tedious processes and hello to efficiency and insight with datawindow.

Discover the future of data processing and analysis – get started with datawindow today and experience the difference firsthand.
For a better understanding of the library, visit the datawindow repository https://github.com/DL4150/datawindow
"""



setup(
    name="datawindow",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Daniel Lawrence",
    author_email="daniellawrence4150@gmail.com",
    url='https://github.com/DL4150/datawindow',
    license='MIT',
    packages=find_packages(),
    install_requires=['pandas','sklearn','scipy','matplotlib','seaborn','numpy'],
    keywords=['python','data science','data analytics','machine learning','data','analysis'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
