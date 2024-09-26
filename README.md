# Adaptive Neuro-Fuzzy Inference System (ANFIS)-PSO-Curve-Fitting-Solver

This project demonstrates a **real-time visualization** of three algorithms—**Hill Climbing**, **Fuzzy Logic**, and **Adaptive Neuro-Fuzzy Inference System (ANFIS) PSO**—as they attempt to fit a predefined curve (based on a sine function) and minimize the difference between their predictions and the exact solution.

The project includes control panel to adjust the number of data points and the complexity of the sine curve. All updates happen in real time, providing both a visual and statistical representation of the algorithms' progress.
![ANFIS PSO Curve Fitting  Solver 2](https://github.com/user-attachments/assets/0ab7bca2-aae4-4e2b-9a25-1e61c0708bbc)

## Key Features

1. **Real-Time Algorithm Visualization**:
    - Three algorithms are visualized in real time:
        - **Hill Climbing**
        - **Fuzzy Logic**
        - **ANFIS PSO**
    - Each algorithm attempts to fit an exact sine function by adjusting its predictions over time.

2. **Interactive Control Panel**:
    - A **slider panel** allows the user to interactively adjust:
        - **Number of Data Points**: Controls the number of points used by the algorithms.
        - **Complexity of the Sine Curve**: Adjusts the frequency of the sine wave, making the problem more or less complex for the algorithms.

3. **Algorithm Updates**:
    - The **Hill Climbing** algorithm adjusts based on random steps.
    - The **Fuzzy Logic** algorithm adjusts using error reduction and step scaling.
    - The **ANFIS PSO** algorithm adjusts based on a combination of **inertia**, **cognitive** (self-learning), and **social** (group learning) components.

4. **Multiple Plotting Areas**:
    - The project includes four key visualizations:
        1. **Hill Climbing Prediction vs. Exact Solution**
        2. **Fuzzy Logic Prediction vs. Exact Solution**
        3. **ANFIS PSO Prediction vs. Exact Solution**


## Technologies and Libraries

- **Python**
- **Matplotlib**: Used for plotting real-time graphs and interactive visualizations.
- **FuncAnimation**: A part of Matplotlib, used to update the plot dynamically.
- **Matplotlib Widgets (Slider)**: Provides interactive sliders to control the number of points and the complexity of the problem in real time.

## How It Works

- The user can adjust the complexity of the sine function and the number of data points using sliders. These settings affect all three algorithms, which try to fit the exact solution by minimizing their error.
- As the algorithms run, a cost function is computed for each one based on the mean absolute error between the algorithm’s prediction and the exact sine wave.
  
## Usage

To run this project, simply execute the Python script. The project will open a graphical user interface (GUI) with four subplots. You can adjust the sliders to change the number of points or the complexity of the sine curve, and watch how each algorithm adapts in real time.

## Applications

This project can be used to demonstrate:
- Real-time optimization techniques.
- How different algorithms converge to a solution.
- Comparative performance analysis of optimization algorithms.


