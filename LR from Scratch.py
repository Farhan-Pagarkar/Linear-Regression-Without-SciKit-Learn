import pandas as pd
import matplotlib.pyplot as plt

def linear_regression(file_path, x_col=None, y_col=None, L=0.0001, Epochs=250):

    data = pd.read_csv(file_path)
    
 
    if x_col is None or y_col is None:
        x_col, y_col = data.columns[0], data.columns[1]

    def gradient_descent(m_now, b_now, points, L):
        m_gradient = b_gradient = 0
        n = len(points)

        for i in range(n):
            x = points.iloc[i][x_col]
            y = points.iloc[i][y_col]
            m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
            b_gradient += -(2/n) * (y - (m_now * x + b_now))

        m = m_now - m_gradient * L
        b = b_now - b_gradient * L
        return m, b


    m, b = 0, 0
    for _ in range(Epochs):
        m, b = gradient_descent(m, b, data, L)

    print(f"Equation: y = {m:.4f}x + {b:.4f}")

    # Plot
    plt.scatter(data[x_col], data[y_col], color="red")
    plt.plot(data[x_col], m * data[x_col] + b, color="black")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()

    return m, b
