import numpy as np
import matplotlib.pyplot as plt


f0 = 82  # Base frequency (given for our group)

# Define required frequencies
f1 = f0
f2 = f0 / 2
f3 = 10 * f0

# Sampling frequency (chosen according to Nyquist)
fs = 10000  # Hz (greater than 2*f3 = 1640 Hz)



T1 = 1 / f1
T2 = 1 / f2
T3 = 1 / f3

# Create time vectors covering 3 full periods
t1 = np.arange(0, 3*T1, 1/fs)
t2 = np.arange(0, 3*T2, 1/fs)
t3 = np.arange(0, 3*T3, 1/fs)



# Generate sinusoidal signals
x1 = np.sin(2 * np.pi * f1 * t1)
x2 = np.sin(2 * np.pi * f2 * t2)
x3 = np.sin(2 * np.pi * f3 * t3)

# For the summed signal, use a common time axis
# We select the longest time interval (3*T2)
t_sum = np.arange(0, 3*T2, 1/fs)

x1_sum = np.sin(2 * np.pi * f1 * t_sum)
x2_sum = np.sin(2 * np.pi * f2 * t_sum)
x3_sum = np.sin(2 * np.pi * f3 * t_sum)

x_total = x1_sum + x2_sum + x3_sum



plt.figure(figsize=(10, 9))

# First subplot (f1)
plt.subplot(4, 1, 1)
plt.plot(t1, x1)
plt.title("Signal 1 (f1 = 82 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Second subplot (f2)
plt.subplot(4, 1, 2)
plt.plot(t2, x2)
plt.title("Signal 2 (f2 = 41 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Third subplot (f3)
plt.subplot(4, 1, 3)
plt.plot(t3, x3)
plt.title("Signal 3 (f3 = 820 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Sum of signals
plt.subplot(4, 1, 4)
plt.plot(t_sum, x_total)
plt.title("Sum of Three Signals")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
