import numpy as np

def gradient_descent(x, y):
    m_curr = 0  # Initial slope
    b_curr = 0  # Initial intercept
    n = len(x)  # Number of data points
    iterations = 1000  # Number of iterations
    learning_rate = 0.01  # Learning rate (increased for faster convergence)

    for i in range(iterations):
        y_predict = m_curr * x + b_curr  # Predicted values
        cost = (1/n) * sum((y - y_predict) ** 2)  # Mean Squared Error

        md = -(2/n) * sum(x * (y - y_predict))  # Derivative w.r.t m
        bd = -(2/n) * sum(y - y_predict)  # Derivative w.r.t b

        m_curr = m_curr - learning_rate * md  # Update slope
        b_curr = b_curr - learning_rate * bd  # Update intercept

        if i % 100 == 0:  # Print every 100 iterations
            print(f"Iteration {i}: m = {m_curr:.4f}, b = {b_curr:.4f}, cost = {cost:.4f}")

    return m_curr, b_curr

# Define dataset
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

# Call gradient descent function
m_final, b_final = gradient_descent(x, y)
print(f"\nFinal values: m = {m_final:.4f}, b = {b_final:.4f}")
