#Price Prediction
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from scipy.stats import t

#Step 1 : Train-test split 
# X = Independent ; y = Dependent ; 20% Testing, 80% Testing
X = InderaSubang_data[["Square Feet"]]
y = InderaSubang_data["Transaction Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Step 2 : Fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

#Predict and calculate residuals
y_pred_train = model.predict(X_train)
residuals = y_train - y_pred_train

# Residual=Difference between actual (y_train) and predicted values (y_pred_train).

# Calculate Residual Standard Deviation (RSD)
std_residuals = np.std(residuals)

# Number of samples
N = len(y_train)

# Standard error (SE)
SE = std_residuals / np.sqrt(N)

# Define confidence level and t-critical value (For small datasets (𝑁≤30), 
# use the t-distribution critical values based on degrees of freedom (𝑑𝑓=𝑁−2)
confidence_level = 0.90  # 90% CI
df_degrees = N - 2  # Degrees of freedom
t_critical = t.ppf((1 + confidence_level) / 2, df_degrees)

#Step 4 : Function to calculate predicted price and confidence interval
def predict_price_ci(square_feet, model, SE, t_critical):
    example_input = pd.DataFrame({'Square Feet': [square_feet]})
    predicted_price = model.predict(example_input)[0]
    
    # Confidence Interval
    margin_of_error = t_critical * SE
    lower_bound = predicted_price - margin_of_error
    upper_bound = predicted_price + margin_of_error
    
    return predicted_price, lower_bound, upper_bound

# Predict with 90% CI for a given square feet
square_feet = 1711  # Example input
predicted_price, lower_bound, upper_bound = predict_price_ci(square_feet, model, SE, t_critical)

# Display results
print(f"Predicted Price for {square_feet} square feet: RM {predicted_price:,.0f}")
print(f"90% Confidence Interval: RM {lower_bound:,.0f} - RM {upper_bound:,.0f}")

#Compare against actual Transaction
InderaSubang_Sqr1711=df[df['Square Feet']==1711]
InderaSubang_Sqr1711[['Scheme Name/Area','Unit Level','Transaction Price','Square Feet','Transaction Date']]
