# Geotab Intersection Congestion Prediction

![Intersection_intro](https://github.com/gayuc07/Cloud_Computing/blob/master/Images/intersec.JPG)

Intersection Congestion provides information gathered from commercial vehicle telematics devices.It includes aggregate stopped vehicle information and intersection wait times. 
Possible use cases include(Geotab website): 
A city can use the data to analyze congestion and light timing issues at scale across the region, and evaluate for impact or potential impact of infrastructure changes. 
NGOs can use the data as part of research into emissions and pollution. 
Fleet managers can use the information on traffic congestion at intersections as a factor to support optimal routing decisions.

In this project, we use intersection details of Philadelphia city. Aim of this project is to make use of the amazon sagemaker service to predict congesion by aggregate measure of stopping distance and waiting times. 

Dataset: https://www.kaggle.com/c/bigquery-geotab-intersection-congestion/data

## Data Preprocessing
From Dataset, Features are mostly categorical values and they are nominal data. Inorder reduce the dimensionality of final dataset and preserve information present in each feature, we are clustering regions and forming new feature.

### Cluster Details
![Clusters](https://github.com/gayuc07/Cloud_Computing/blob/master/Images/Clusters.JPG)


## Exploratory Data Analysis

The cluster 3 & 4 had high congestion compared to the other cluster spot. The total time stopped at clusters 3 & 4 are on average 
![EDA](https://github.com/gayuc07/Cloud_Computing/blob/master/Images/EDA-Clusters_direction.JPG)
![EDA](https://github.com/gayuc07/Cloud_Computing/blob/master/Images/EDA-total_time_stopped.JPG)


## AWS Pipeline - Project Architecture & Data Flow

![Data Flow](https://github.com/gayuc07/Cloud_Computing/blob/master/Images/AWS_pipeline.JPG)
