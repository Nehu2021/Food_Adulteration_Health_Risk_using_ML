## Food_Adulteration_Health_Risk_using_ML
# Project Overview
This project aims to predict the health risk due to food adulteration based on adulteration type and product using gradient boosting model. The project includes a Streamlit web application that allows users to input product name, adulteration type, chemicals and get predictions.
# Project Details
The dataset used for this project includes various products , adulterants and detection method also it contains information about health risk, such as:
1. product_name
2. brand
3. category
4. adulterant
5. detection_method
6. severity
7. health_risk

# Model
A Gradient Boosting Model was trained on the basis of the features listed above, excluding the 'health_risk' column. 

# Streamlit App
The Streamlit app provides an interactive interface to input product name, brand, category, adulterant, detection method, severity and visualize the predictions. The app includes:
1. A form to input product name, brand, category, adulterant, detection method, severity
2. A "Predict" button to generate prediction

# Installation
# Prerequisites
Ensure you have the following installed:

Python 3.1.2 or higher

Git
# Steps
1. Clone the repository
git clone https://github.com/Nehu2021/Food_Adulteration_Health_Risk_using_ML.git

3. Navigate to the project directory
Change your current working directory to the project directory.

cd Food_Adulteration

5. Install dependencies
Install the required packages using pip.

pip install -r requirements.txt

# Run the predictor

This model is pre-trained so simply run the predictor.

   streamlit run app.py
   
After execution, open your web browser and go to [http://192.168.1.64:8501] to access the application.

# If you want to train the model on your own:

1. Install Jupyter Notebook: If you haven't already installed Jupyter Notebook, you can do so using pip:

pip install notebook

2. Open the Notebook: Once Jupyter Notebook is installed, navigate to the directory where lung_cancer_analysis.ipynb is located using your command line or terminal.

3. Start Jupyter Notebook: Run the following command to start the Jupyter Notebook server:

jupyter notebook
