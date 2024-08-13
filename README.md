# Machine-learning
Example of Machine learning to predict weight based on the relationship of the input height

1. We create the Dataset

Creating two arrays, first one is carries "heights" and second one "weights", which represent the heights and weights of individuals, respectively. We assume the relationship to be linear: "weight = 3.1 * height + 14". This is just an example relationship

2. We adjust the Data
The "scikit-learn" library expects the input data to be in a 2D array format. The "reshape(-1, 1)" method is used to convert the 1D array of heights into a 2D array with one column.

3. We create and train the Model
We create a `LinearRegression` model using "scikit-learn" and train it on our dataset with the `fit()` method. The model learns the relationship between height and weight.

4. We then start to make predictions
We create a new array of heights ("heights_new") for which we want to predict the corresponding weights. The "predict()" method is used to generate these predictions based on the model we trained.

5. We visualize the Results
We use `matplotlib` to plot the actual data points and the line representing our model's predictions. This visualization helps us see how well our model fits the data.

6. Print output the predictions
Finally, we print the predicted weights for the new heights.


