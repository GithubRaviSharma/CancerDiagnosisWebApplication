import streamlit as st

st.set_page_config(
    page_title="Parameters",
    page_icon=":hospital:",
    layout="centered",
)

st.write("""
# Parameters: Breast Cancer Diagnosis 
Medicos uses over thirty **Parameters** to provide accurate results, The model is train and tested for **Maximum** Accuracy and **Minimum** Errors.
""")
st.write('---')

st.write("""
    ## Input Parameters of Breast Cancer Dataset

    1. **mean radius**: Mean of distances from center to points on the perimeter.
    2. **mean texture**: Standard deviation of gray-scale values.
    3. **mean perimeter**: Perimeter of the tumor.
    4. **mean area**: Area of the tumor.
    5. **mean smoothness**: Local variation in radius lengths.
    6. **mean compactness**: Measure of shape compactness.
    7. **mean concavity**: Severity of concave portions of the contour.
    8. **mean concave points**: Number of concave portions of the contour.
    9. **mean symmetry**: Symmetry of tumor.
    10. **mean fractal dimension**: Coastline approximation - 1.
    11. **radius error**: Standard error of the mean of distances from center to points on the perimeter.
    12. **texture error**: Standard error of gray-scale values.
    13. **perimeter error**: Error of the tumor's perimeter.
    14. **area error**: Error of the tumor's area.
    15. **smoothness error**: Local variation in radius lengths.
    16. **compactness error**: Measure of shape compactness.
    17. **concavity error**: Severity of concave portions of the contour.
    18. **concave points error**: Number of concave portions of the contour.
    19. **symmetry error**: Symmetry of tumor.
    20. **fractal dimension error**: Coastline approximation - 1.
    21. **worst radius**: "Worst" or largest mean value for radius.
    22. **worst texture**: "Worst" or largest mean value for texture.
    23. **worst perimeter**: "Worst" or largest mean value for perimeter.
    24. **worst area**: "Worst" or largest mean value for area.
    25. **worst smoothness**: "Worst" or largest mean value for smoothness.
    26. **worst compactness**: "Worst" or largest mean value for compactness.
    27. **worst concavity**: "Worst" or largest mean value for concavity.
    28. **worst concave points**: "Worst" or largest mean value for concave points.
    29. **worst symmetry**: "Worst" or largest mean value for symmetry.
    30. **worst fractal dimension**: "Worst" or largest mean value for fractal dimension.
    """)
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
    
    