# ANFIS-PSO-Curve-Fitting-Solver
Real-Time Algorithm Performance and Cost Function Visualization
This project demonstrates a real-time visualization of three algorithms—Hill Climbing, Fuzzy Logic, and ANFIS PSO—as they attempt to fit a predefined curve (based on a sine function) and minimize the difference between their predictions and the exact solution. The project includes dynamic updates to the cost function for each algorithm, as well as a control panel to adjust the number of data points and the complexity of the sine curve. All updates happen in real time, providing both a visual and statistical representation of the algorithms' progress.

Key Features:
Real-Time Algorithm Visualization:

Three algorithms are visualized in real time:
Hill Climbing
Fuzzy Logic
ANFIS PSO
Each algorithm attempts to fit an exact sine function by adjusting its predictions over time.
Dynamic Cost Function Plot:

The cost function (i.e., the error between the algorithm’s prediction and the exact solution) is calculated and plotted in real time for each algorithm.
This provides insight into how quickly each algorithm is converging to a solution or minimizing its error.
Interactive Control Panel:

A slider panel allows the user to interactively adjust:
Number of Data Points: Controls the number of points used by the algorithms.
Complexity of the Sine Curve: Adjusts the frequency of the sine wave, making the problem more or less complex for the algorithms.
Changes to these settings dynamically update both the real-time visualization of the algorithms and their corresponding cost functions.
Algorithm Updates:

Each algorithm attempts to minimize its cost by comparing its prediction to the exact solution and adjusting its values accordingly.
The Hill Climbing algorithm adjusts based on random steps.
The Fuzzy Logic algorithm adjusts using error reduction and step scaling.
The ANFIS PSO algorithm adjusts based on a combination of inertia, cognitive (self-learning), and social (group learning) components.
Multiple Plotting Areas:

The project includes four key visualizations:
Hill Climbing Prediction vs. Exact Solution
Fuzzy Logic Prediction vs. Exact Solution
ANFIS PSO Prediction vs. Exact Solution
Cost Function Evolution: Shows the cost function (error) for all three algorithms over time, indicating their convergence rates.
Technologies and Libraries:
Python
Matplotlib: Used for plotting real-time graphs and interactive visualizations.
FuncAnimation: A part of Matplotlib, used to update the plot dynamically.
Matplotlib Widgets (Slider): Provides interactive sliders to control the number of points and the complexity of the problem in real time.
How It Works:
The user can adjust the complexity of the sine function and the number of data points using sliders. These settings affect all three algorithms, which try to fit the exact solution by minimizing their error.
As the algorithms run, a cost function is computed for each one based on the mean absolute error between the algorithm’s prediction and the exact sine wave. This cost is plotted over time, showing how each algorithm converges to the solution.
The interactive plot provides both a visual representation of the algorithms' progress and a statistical analysis of their performance through the cost function.
Usage:
To run this project, simply execute the Python script. The project will open a graphical user interface (GUI) with four subplots. You can adjust the sliders to change the number of points or the complexity of the sine curve, and watch how each algorithm adapts in real time.

Applications:
This project can be used to demonstrate:

Real-time optimization techniques.
How different algorithms converge to a solution.
Comparative performance analysis of optimization algorithms.
Visualization of cost functions over time, offering insight into algorithm efficiency.

