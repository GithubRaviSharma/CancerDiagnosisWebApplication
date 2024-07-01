# Medicos: Breast Cancer Diagnosis Web Application

## Overview

Medicos is a web application designed to assist in the diagnosis of breast cancer by allowing users to input 30 parameters of breast cancer data using interactive sliders. Based on the input parameters, the application predicts whether the breast cell is benign or malignant. Additionally, the application provides visualizations such as histograms, scatter plots, and a confusion matrix to help users better understand the data and the model's performance.

## Features

- **Interactive Sliders**: Users can input all 30 parameters of the breast cancer dataset using intuitive sliders.
- **Prediction**: The application predicts whether the cell is benign or malignant based on the input parameters.
- **Visualizations**: Includes histograms, scatter plots, and a confusion matrix to visualize data and model performance.
- **User-Friendly Interface**: Built with Streamlit for a clean, responsive, and easy-to-use interface.

## Usage

1. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

2. **Open the application in your web browser**:
   The application will run locally, typically accessible at `http://localhost:8501`.

## Dataset

The application uses the Breast Cancer Wisconsin dataset, which is publicly available from the UCI Machine Learning Repository. The dataset consists of 30 numeric features computed from a digitized image of a fine needle aspirate (FNA) of a breast mass, describing characteristics of the cell nuclei present in the image.

## Visualizations

- **Histogram**: Displays the distribution of each feature.
- **Scatter Plot**: Shows the relationship between any two selected features.
- **Confusion Matrix**: Evaluates the performance of the classification model.

## Model

The model used for prediction is based on the Random Forest Classifier from the `scikit-learn` library, which has been trained on the Breast Cancer Wisconsin dataset.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## Acknowledgements

- Dr. William H. Wolberg, University of Wisconsin Hospitals, Madison
- UCI Machine Learning Repository for providing the dataset
