## Bangalore Home Price Prediction

This project is a full-stack machine learning application designed to predict home prices in Bangalore, India. It combines a trained regression model with a user-friendly web interface, allowing users to estimate property prices based on features such as location, square footage, number of bedrooms, and bathrooms.

**Features**

- Predicts home prices in Bangalore using machine learning
- Interactive web interface for user input and displaying results
- Backend API built with Flask for serving predictions
- End-to-end workflow: data preprocessing, model training, deployment, and real-time inference

**Project Structure**

- **Data Science Pipeline:**  
  - Data loading and cleaning  
  - Outlier detection and removal  
  - Feature engineering and dimensionality reduction  
  - Model selection and hyperparameter tuning (GridSearchCV, K-Fold cross-validation)  
  - Model training using scikit-learn (Linear Regression)  
  - Model serialization for deployment

- **Backend:**  
  - Flask-based API to handle prediction requests  
  - Model loaded from serialized file (`banglore_home_prices_model.pickle`)  
  - API endpoint for predicting price based on user input

- **Frontend:**  
  - HTML, CSS, and JavaScript interface  
  - Form for users to input property details  
  - Displays predicted price returned from the backend server

**Technologies Used**

- Python, Jupyter Notebook
- Pandas, NumPy, scikit-learn, Matplotlib
- Flask (for API backend)
- HTML, CSS, JavaScript (for frontend)
**How to Run**

1. Clone the repository.
2. Install dependencies:  
   ```
   pip install -r requirements.txt
   ```
3. Start the Flask server:  
   ```
   python server.py
   ```
4. Open `app.html` in your browser and interact with the application.

**Usage**

- Enter the required property details (location, area, bedrooms, bathrooms) in the web form.
- Click "Estimate Price" to receive the predicted home price instantly.

**Dataset**

- The model is trained on the Bengaluru House Price dataset (available on Kaggle).

**Contributing**

Contributions are welcome! Please open an issue or submit a pull request for improvements or bug fixes.

---

This project demonstrates the complete cycle of a data science solution, from data preprocessing and model building to deployment as a web application, making it a practical reference for real estate price prediction using machine learning.
