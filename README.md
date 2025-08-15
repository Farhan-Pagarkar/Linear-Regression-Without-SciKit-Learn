Linear Regression Without Scikit-Learn

This project implements Linear Regression from scratch in Python using Gradient Descent — without relying on machine learning libraries like Scikit-Learn.
It demonstrates how to calculate the slope (m) and intercept (b) manually and visualize the results.

Features

Loads dataset using Pandas

Implements Gradient Descent algorithm manually

Iteratively updates model parameters

Visualizes data points and regression line using Matplotlib

 Files

linear_regression_data.csv – Sample dataset containing x and y values

linear_regression.py – Main script implementing gradient descent and plotting the results

⚙️ How It Works

Initialize parameters (m, b) to 0

Loop over data for a fixed number of epochs

Calculate gradients for slope and intercept

Update parameters using the learning rate (L)

Plot the final regression line alongside the data points
