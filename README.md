# House Price Modelling
This project utilizes machine learning techniques to analyze housing market data and predict house prices based on key features. It is aimed at creating a robust machine learning model for predicting house prices based on various features. The primary goal was to build a model with high accuracy for real estate market analysis and decision-making.

<h3>Methodology</h3>
<ol>
  <li>Initial Attempts: Linear Regression: Initial modeling using linear regression resulted in a low accuracy of 75%, prompting further exploration.<br>
Randomized Search CV: Employed randomized search cross-validation for hyperparameter tuning but didn't yield a significant improvement.</li>
  <li>Advanced Algorithms: Utilized several advanced algorithms:<br>
Gradient Booster<br>
XGBoost<br>
Random Forest<br>
Decision Tree<br>
K-Nearest Neighbors (KNN)<br>
Other Advanced Regression Algorithms</li>
<li>Model Selection: The sklearn Gradient Booster emerged as the best-performing model, exhibiting superior test accuracy and a low overfitting score among the algorithms tested.
</li>
</ol>

<h3>Model Deployment</h3>
The finalized model was extracted and deployed using Flask, offering an accessible and interactive platform for house price predictions.

<h3>Deployment Platform</h3>
The Flask-based model is hosted on PythonAnywhere, ensuring easy access and utilization for real-time predictions.

Technologies Used
Python
Scikit-learn
Flask
PythonAnywhere

Future Steps:
Continued optimization and feature engineering could further enhance the model's accuracy and generalize its application across diverse real estate datasets.
The model, built using Python and popular libraries, provides accurate price estimations, aiding in property market analysis and decision-making. It's deployed using Flask and hosted on PythonAnywhere for seamless accessibility.


