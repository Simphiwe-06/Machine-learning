import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

heights = np.array([150, 160, 170, 180, 190])  # in cm
weights = np.array([65, 70, 75, 80, 85])       # in km

heights = heights.reshape(-1, 1)

model = LinearRegression()
model.fit(heights, weights)

heights_new = np.array([155, 165, 175, 185]).reshape(-1, 1)
weights_pred = model.predict(heights_new)


plt.scatter(heights, weights, color='blue', label='Actual weights')
plt.plot(heights_new, weights_pred, color='red', label='Predicted weights')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.legend()
plt.show()

print(f"The generated prediction for heights {heights_new.flatten()}: {weights_pred}")
