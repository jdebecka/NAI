import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

bmi_life_data = pd.read_csv(
    '/Users/juliadebecka/Documents/GitHub/NAI/Language_Classifier/Udacity_ML_Course/BMI_Life_Model/Resources/bmi_and_life_expectancy.csv')

predict = "Life expectancy"
y = np.array(bmi_life_data[[predict]])
X = np.array(bmi_life_data[["BMI"]])

model = LinearRegression()
model.fit(X, y)
laos_life_exp = model.predict([[21.07931]])
laos_life_exp = laos_life_exp[0][0]
print(laos_life_exp)
