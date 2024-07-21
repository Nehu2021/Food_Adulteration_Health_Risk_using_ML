import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load the saved model
model_path = 'C:\\Users\\USER\\Desktop\\Food_Adulteration\\ML_Model\\gradient_boosting_model.pkl'
model = joblib.load(model_path)

# Extract feature names from the model if they are available
try:
    expected_columns = model.feature_names_in_
except AttributeError:
    st.error("The model does not contain feature names. Please ensure the model is trained with feature names.")

def main():
    # Set the title of the web app
    st.title('Health Risk in Food Adulteration')

    # Add a description
    st.write('Enter Food Information.')

    # Create columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader('Food Information')

        # Add input fields for features
        product_name = st.selectbox('product_name',['Butter', 'Chicken', 'Yogurt', 'Wine', 'Bread', 'Beef', 'Juice', 'Milk', 'Cheese',
 'Honey'])
        brand = st.selectbox("Brand", ['BrandA', 'BrandB','BrandC','BrandD','BrandE'])
        category = st.selectbox("Category", ['Meat' ,'Dairy', 'Beverages', 'Bakery', 'Condiments'])
        adulterant = st.selectbox("Adulterant", ['Artificial sweeteners', 'Coloring agents', 'Water', 'Melamine', 'Chalk'])
        detection_method = st.selectbox("detection_method", ['Microbiological Analysis', 'Sensory Evaluation', 'Spectroscopy',
 'Chemical Analysis'])
        severity = st.selectbox("severity", ['Moderate' ,'Severe' ,'Minor'])
        
    # Prepare input data as a DataFrame
    input_data = pd.DataFrame({
        'product_name_Beef':[1 if product_name == 'Beef' else 0],
        'product_name_Bread':[1 if product_name == 'Bread' else 0 ],
        'product_name_Butter':[1 if product_name == 'Butter' else 0],
        'product_name_Chicken':[1 if product_name == 'Chicken' else 0],
        'product_name_Cheese':[1 if product_name == 'Cheese' else 0],
        'product_name_Honey':[1 if product_name == 'Honey' else 0],
        'product_name_Juice':[1 if product_name == 'Juice' else 0],
        'product_name_Milk':[1 if product_name == 'Milk' else 0],
        'product_name_Wine':[1 if product_name == 'Wine' else 0],
        'product_name_Yogurt':[1 if product_name == 'Yogurt' else 0],
        'brand_BrandA': [1 if brand == 'BrandA' else 0],
        'brand_BrandB': [1 if brand == 'BrandB' else 0],
        'brand_BrandC': [1 if brand == 'BrandC' else 0],
        'brand_BrandD': [1 if brand == 'BrandD' else 0],
        'brand_BrandE': [1 if brand == 'BrandE' else 0],
        'category_Bakery': [1 if category == 'Bakery' else 0],
        'category_Beverages': [1 if category == 'Beverages' else 0],
        'category_Condiments': [1 if category == 'Condiments' else 0],
        'category_Dairy': [1 if category == 'Dairy' else 0],
        'category_Meat': [1 if category == 'Meat' else 0],
        'adulterant_Artificial sweeteners': [ 1 if adulterant=='Artificail sweetners' else 0],
        'adulterant_Chalk': [1 if adulterant=='Chalk' else 0],
        'adulterant_Coloring agents': [1 if adulterant=='Coloring agents' else 0],
        'adulterant_Melamine': [1 if adulterant=='Melamine' else 0],
        'adulterant_Water': [1 if adulterant=='Water' else 0],
        'detection_method_Chemical Analysis':[1 if detection_method=='Chemical Analysis' else 0],
        'detection_method_Microbiological Analysis': [1 if detection_method=='Microbological Analysis' else 0],
        'detection_method_Sensory Evaluation': [1 if detection_method=='Sensory Evalutaion' else 0],
        'detection_method_Spectroscopy': [1 if detection_method=='Spectroscopy' else 0],
        'severity_Minor': [1 if severity == 'Minor' else 0],
        'severity_Moderate': [1 if severity == 'Moderate' else 0],
        'severity_Severe': [1 if severity == 'Severe' else 0],
    })

    # Ensure columns are in the same order as during model training
    input_data = input_data[expected_columns]

    # Prediction and results section
    with col2:
        st.subheader('Prediction')
        if st.button('Predict'):
            prediction = model.predict(input_data)
            probability = model.predict_proba(input_data)[0][1]

            # Define thresholds for health risk categories
            if probability >= 0.5:
                health_risk = "Low"
            elif 0.3 <= probability < 0.5:
                health_risk = "Moderate"
            else:
                health_risk = "High"
            
            st.write(f'Prediction: {health_risk}')
            #st.write(f'Probability: {probability:.2f}')
            
                  

            # Provide recommendations
            if health_risk == "High":
                st.error("This individual is likely to have a high health risk.")
            elif health_risk == "Moderate":
                st.warning("This individual is likely to have a moderate health risk.")
            else:
                st.success("This individual is likely to have a low health risk.")

if __name__ == "__main__":
    main()

