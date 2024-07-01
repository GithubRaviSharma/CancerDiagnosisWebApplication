import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

st.set_page_config(
    page_title="Medicos",
    page_icon=":hospital:",
    layout="centered",
    initial_sidebar_state="expanded"
)
        
# Title and Description
st.write("""
# Medicos: Breast Cancer Diagnosis 
Medicos is a medical web application which does Breast Cancer Diagnosis by classifying the cells into **Benign & Malignant** based on the Input Parameters!
""")
st.image('./Images/Banner.jpg', use_column_width=True)
st.write('---')

st.write("""
## What are Benign and Malignant cells?
""")
st.write('---')

st.write("""
## Benign
"Benign" tumors or conditions are non-cancerous and do not invade nearby tissues or spread to other parts of the body. They typically grow slowly and are usually considered less harmful than malignant tumors. In the context of breast cancer, benign tumors are not cancerous and do not pose the health risks.
""")
st.write('---')


st.write("""
## Malignant
"Malignant" refers to a medical term used to describe cells or tumors that are cancerous. In the context of breast cancer or any other type of cancer, malignant cells are abnormal cells that have the potential to invade nearby tissues and spread to other parts of the body. A malignancy can be aggressive and requires medical intervention such as surgery, chemotherapy, radiation, or targeted therapy to manage and treat.""")
st.write('---')

# Display image
st.image('./Images/Benign&Malignant.png', use_column_width=True)
st.write('---')

# Load breast cancer dataset
breast_cancer = load_breast_cancer()
X = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
Y = pd.Series(breast_cancer.target, name='diagnosis')

# Sidebar for user input parameters
st.sidebar.header('Specify Input Parameters')

def user_input_features():
    data = {}
    for feature in X.columns:
        data[feature] = st.sidebar.slider(f'{feature}', float(X[feature].min()), float(X[feature].max()), float(X[feature].mean()))
    return pd.DataFrame(data, index=[0])

df = user_input_features()

# Display specified input parameters
st.header('Specified Input Parameters')
st.write(df)

# Build and train the model
model = RandomForestClassifier()
model.fit(X, Y)

# Make prediction
prediction = model.predict(df)


# Display prediction
st.header('Prediction of Diagnosis')
diagnosis_mapping = {0: 'Benign', 1: 'Malignant'}
predicted_diagnosis = diagnosis_mapping[prediction[0]]
st.write(f"###### Predicted Diagnosis: There are signs of the presence of {predicted_diagnosis} cells.")
st.write('---')


if predicted_diagnosis == 'Malignant':
    st.warning('There are symptoms of cancerous cells. If you also feel the following symptoms then seek immediate medical help!')
    st.write("""
1. Fatigue.
2. Shortness of breath.
3. Anemia.
4. Diarrhea.
5. Weight loss.
6. Drenching night sweats.
7. Abnormal lumps or bumps.
             """)
    st.markdown("[Learn more about Malignant cells](https://www.ncbi.nlm.nih.gov/books/NBK9553/)")

else:
    st.warning('There are no symptoms of cancerous cells  in the patient!')
    st.markdown("[Learn more about Benign Cells](https://www.healthline.com/health/benign)")


# Feature Importance based on RandomForestClassifier
feature_importances = model.feature_importances_
sorted_idx = feature_importances.argsort()

# Plotting feature importance
st.header('Feature Importance')
plt.figure(figsize=(10, 8))
plt.barh(X.columns[sorted_idx], feature_importances[sorted_idx], color='skyblue')
plt.xlabel('Feature Importance')
plt.title('Feature Importance based on RandomForestClassifier')
st.pyplot(plt)
st.write('---')

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Assuming you have a test set X_test and corresponding true labels Y_test
Y_pred = model.predict(X)  # Use the model to predict on the entire dataset for demonstration

# Histogram of selected feature distributions
st.header('Histograms of Selected Features')
selected_feature = st.selectbox('Select feature for histogram', options=X.columns)

plt.figure(figsize=(8, 6))
plt.hist(X[selected_feature], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel(selected_feature)
plt.ylabel('Frequency')
plt.title(f'Histogram of {selected_feature}')
st.pyplot(plt)
st.write('---')

# Scatter plot based on user-selected features
st.header('Scatter Plot')
x_feature = st.selectbox('Select X-axis feature', options=X.columns)
y_feature = st.selectbox('Select Y-axis feature', options=X.columns)

plt.figure(figsize=(10, 8))
plt.scatter(X[x_feature], X[y_feature], c=Y, cmap='coolwarm', alpha=0.7)
plt.colorbar(label='Diagnosis', ticks=[0, 1])
plt.xlabel(x_feature)
plt.ylabel(y_feature)
plt.title(f'Scatter Plot: {x_feature} vs {y_feature}')
st.pyplot(plt)
st.write('---')

st.header('Confusion Matrix')
cm = confusion_matrix(Y, Y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot(cmap='Blues', ax=plt.gca())
plt.title('Confusion Matrix')
plt.grid(False)
st.pyplot(plt)
st.write('---')

footer = """
<style>
footer {
    visibility: hidden;
}
.main-footer {
    font-size: 12px;
    color: gray;
    text-align: center; 
    bottom: 0;
    width: 100%;
}
</style>
<div class="main-footer">
    <p><a href="https://www.linkedin.com/in/ravi-sharma-586838287/" target="_blank">Medicos</a> &copy; 2024. All rights reserved.</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)