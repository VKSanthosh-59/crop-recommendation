
# AI-Powered Crop Recommendation System

This web-based application recommends the most suitable crop to grow based on key agricultural features such as soil nutrients and weather conditions. Built using Python, scikit-learn, and Streamlit, the model predicts the best crop for cultivation using a trained machine learning algorithm.

## Live Demo

Access the deployed application here:  
https://VKSanthosh-59-crop-recommendation.streamlit.app/

## Technologies Used

- Python
- Scikit-learn
- Streamlit
- NumPy and Pandas
- Git and GitHub
- Streamlit Cloud (deployment)

## Features

- Accepts user input for nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall
- Uses a Random Forest classifier trained on real agricultural data
- Provides real-time crop recommendation
- Easy-to-use interface deployed on the web

## Input Parameters

| Parameter     | Description                   |
|---------------|-------------------------------|
| Nitrogen      | Amount of nitrogen in soil     |
| Phosphorous   | Amount of phosphorous in soil  |
| Potassium     | Amount of potassium in soil    |
| Temperature   | Ambient temperature in Celsius |
| Humidity      | Relative humidity in percentage|
| pH            | Soil pH level                  |
| Rainfall      | Annual rainfall in mm          |

## Installation and Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/VKSanthosh-59/crop-recommendation.git
   cd crop-recommendation
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run crop_app.py
   ```

## Project Structure

```
├── crop_app.py           # Streamlit application
├── crop_model.pkl        # Trained machine learning model
├── requirements.txt      # Required Python libraries
```

## Future Improvements

- Integrate real-time weather data via OpenWeather API
- Include model performance metrics and confidence scores
- Expand to regional recommendations using geospatial data

## Author

Santhosh Veeramani Kanmani  
Master of Data Science, University of Western Australia  
GitHub: [VKSanthosh-59](https://github.com/VKSanthosh-59)
