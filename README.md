# nnUNet_v1_StatsLab  

This repository serves as a dedicated framework for dataset preparation, statistical analysis, and performance evaluation in nnU-Net v1 based biomedical image segmentation. It streamlines the process of dataset creation, preprocessing, and performance metric calculation, while also facilitating advanced statistical analysis and visualization.

## 📂 Dataset Details  

The dataset used in this repository is stored in **`.mat` format** under the **`data`** folder. It includes:  
- **Table24h**: Contains both **control** and **therapy** data, systematically organized for analysis.  

This structured dataset is essential for training GMM and can also be used further for evaluating the nnU-Net v1 segmentation pipeline.

The .mat files are used to train the GMM model, whereas NIfTI files are utilized for training nnU-Net.

## 📌 Key Features  

- **Dataset Preparation**: Generates dataset JSON files following the nnU-Net v1 data structure, ensuring seamless integration with the pipeline.  
- **Data Processing**: Performs preprocessing and organizes the dataset for training and testing using the [nnU-Net v1 framework](https://github.com/MIC-DKFZ/nnUNet) (*branch: nnunetv1*).  
- **Performance Evaluation**: Computes segmentation performance metrics such as Dice, Tversky score, and additional quantitative measures.  
- **Statistical Analysis & Visualization**: Supports further statistical insights through Joint Probability Mapping (JPM), advanced plots, and figures for research publications.  

## 🔬 Research & Citation  

This repository builds upon the [nnU-Net v1](https://github.com/MIC-DKFZ/nnUNet) framework. If you use nnU-Net in your work, please cite the following reference:  

> **Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., & Maier-Hein, K. H. (2021).**  
> *nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation.*  
> *Nature Methods, 18(2), 203-211.*  

## 🚀 Get Started  

This repository is designed to enhance the standard nnU-Net pipeline by providing additional tools for dataset preparation, statistical evaluation, and research-focused analysis. Feel free to explore, modify, and contribute!