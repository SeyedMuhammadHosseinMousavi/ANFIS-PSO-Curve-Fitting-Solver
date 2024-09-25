import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
from matplotlib.gridspec import GridSpec

# Define the exact solution with adjustable complexity
def exact_solution(x, complexity):
    return np.sin(x) + 0.5 * np.sin(complexity * x)

# Create initial x values and complexity level
x_exact = np.linspace(0, 10, 500)  # More points for smoother curves
complexity = 3
y_exact = exact_solution(x_exact, complexity)

# Initial number of points
n_points = 50

# Initialize random data for each method
x_points = np.linspace(0, 10, n_points)
y_hill_climbing = np.random.uniform(-2, 2, n_points)
y_fuzzy = np.random.uniform(-2, 2, n_points)
y_anfis_pso = np.random.uniform(-2, 2, n_points)

# Set up the figure layout using GridSpec
fig = plt.figure(figsize=(7, 6))  # Adjust figure size
gs = GridSpec(3, 1, figure=fig)  # Create 3 rows, 1 column for the plots

# Create subplots for each method using GridSpec
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[2, 0])

# Plot the original exact solution in each subplot
line_exact1, = ax1.plot(x_exact, y_exact, 'k-', label='Exact Solution', linewidth=2)
line_exact2, = ax2.plot(x_exact, y_exact, 'k-', label='Exact Solution', linewidth=2)
line_exact3, = ax3.plot(x_exact, y_exact, 'k-', label='Exact Solution', linewidth=2)

# Add "Training Data" lines for all subplots
line_training_hill, = ax1.plot(x_points, y_hill_climbing, 'g--', label='Training Data', linewidth=2)
line_training_fuzzy, = ax2.plot(x_points, y_fuzzy, 'g--', label='Training Data', linewidth=2)
line_training_pso, = ax3.plot(x_points, y_anfis_pso, 'g--', label='Training Data', linewidth=2)

# Initial plots for each method
line_hill_climbing, = ax1.plot(x_points, y_hill_climbing, 'bo-', label='Hill Climbing', linewidth=2)
line_fuzzy, = ax2.plot(x_points, y_fuzzy, 'ro-', label='Fuzzy Logic', linewidth=2)
line_anfis_pso, = ax3.plot(x_points, y_anfis_pso, 'o-', color='purple', label='ANFIS PSO', linewidth=2)

# Labels, legends on top of the plot in a line format
for ax in (ax1, ax2, ax3):
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.0), ncol=3, fontsize=10, 
              frameon=True, facecolor='white', edgecolor='black', shadow=True, 
              fancybox=True, title_fontsize='medium', 
              title='',  # Removed title from legend
              prop={'weight': 'bold'})  # Made legend text bold

# Function to update the number of points and reinitialize the data
def update_points(val):
    global n_points, x_points, y_hill_climbing, y_fuzzy, y_anfis_pso, y_exact, complexity

    n_points = int(slider_points.val)  # Get value from the slider for number of points
    complexity = slider_complexity.val  # Get value from the slider for complexity

    # Update the exact solution with the new complexity
    y_exact = exact_solution(x_exact, complexity)

    # Update x_points and random y data based on new n_points
    x_points = np.linspace(0, 10, n_points)
    y_hill_climbing = np.random.uniform(-2, 2, n_points)
    y_fuzzy = np.random.uniform(-2, 2, n_points)
    y_anfis_pso = np.random.uniform(-2, 2, n_points)

    # Update the training data lines
    line_training_hill.set_data(x_points, y_hill_climbing)
    line_training_fuzzy.set_data(x_points, y_fuzzy)
    line_training_pso.set_data(x_points, y_anfis_pso)

    # Update the actual method lines
    line_hill_climbing.set_data(x_points, y_hill_climbing)
    line_fuzzy.set_data(x_points, y_fuzzy)
    line_anfis_pso.set_data(x_points, y_anfis_pso)

    # Update the exact solution curve in all subplots
    line_exact1.set_ydata(y_exact)
    line_exact2.set_ydata(y_exact)
    line_exact3.set_ydata(y_exact)

    # Redraw the figure so the changes are applied immediately
    fig.canvas.draw_idle()

# Hill Climbing Update
def update_hill_climbing(frame):
    global y_hill_climbing
    
    # Hill climbing step
    for i in range(n_points):
        step = np.random.uniform(-0.05, 0.05)
        new_val = y_hill_climbing[i] + step
        if abs(new_val - exact_solution(x_points[i], complexity)) < abs(y_hill_climbing[i] - exact_solution(x_points[i], complexity)):
            y_hill_climbing[i] = new_val

    line_hill_climbing.set_ydata(y_hill_climbing)
    
    return line_hill_climbing, line_training_hill

# Fuzzy Logic Update Function
def update_fuzzy(frame):
    global y_fuzzy

    errors = np.abs(y_exact[np.linspace(0, 499, n_points, dtype=int)] - y_fuzzy)
    step_sizes = 0.05 * (1 - errors / max(errors))
    y_fuzzy += step_sizes * (y_exact[np.linspace(0, 499, n_points, dtype=int)] - y_fuzzy)

    line_fuzzy.set_ydata(y_fuzzy)
    
    return line_fuzzy, line_training_fuzzy

# ANFIS PSO Update
def update_anfis_pso(frame):
    global y_anfis_pso

    errors = np.abs(y_exact[np.linspace(0, 499, n_points, dtype=int)] - y_anfis_pso)
    step_sizes = 0.05 * (1 - errors / max(errors))
    inertia = 0.7
    cognitive = 0.1 * (y_exact[np.linspace(0, 499, n_points, dtype=int)] - y_anfis_pso)
    social = 0.2 * (y_exact[np.linspace(0, 499, n_points, dtype=int)] - y_anfis_pso)
    y_anfis_pso += inertia * np.random.uniform(-0.05, 0.05, n_points) + cognitive + social + step_sizes

    line_anfis_pso.set_ydata(y_anfis_pso)
    
    return line_anfis_pso, line_training_pso

# Create a new figure and add sliders outside the main figure for controlling points and complexity
slider_fig = plt.figure(figsize=(7, 3))  # Separate figure for sliders

# Slider for number of points
ax_slider_points = slider_fig.add_axes([0.1, 0.6, 0.8, 0.1], facecolor='lightgoldenrodyellow')
slider_points = Slider(ax_slider_points, '', 10, 200, valinit=n_points, valstep=1)
slider_fig.text(0.5, 0.75, 'Num Points', ha='center', va='center')  # Title above slider

# Slider for complexity
ax_slider_complexity = slider_fig.add_axes([0.1, 0.3, 0.8, 0.1], facecolor='lightgoldenrodyellow')
slider_complexity = Slider(ax_slider_complexity, '', 1, 10, valinit=complexity, valstep=0.5)
slider_fig.text(0.5, 0.45, 'Complexity', ha='center', va='center')  # Title above slider

# Attach the update function to the sliders
slider_points.on_changed(update_points)
slider_complexity.on_changed(update_points)

# Animation stop on window close
def on_close(event):
    print("Closing animation...")
    plt.close()  # Ensure the animation stops

# Attach the close event
fig.canvas.mpl_connect('close_event', on_close)

# Create the animations
ani1 = FuncAnimation(fig, update_hill_climbing, frames=200, interval=100, blit=True)
ani2 = FuncAnimation(fig, update_fuzzy, frames=200, interval=100, blit=True)
ani3 = FuncAnimation(fig, update_anfis_pso, frames=200, interval=100, blit=True)

plt.show()
