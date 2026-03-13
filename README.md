# DTMF and Sinusoidal Signal Generator

## Project Description
This project is a Python-based application that generates and visualizes basic sinusoidal signals as well as DTMF (Dual-Tone Multi-Frequency) tones. The project consists of two main parts:

1. **Sinusoidal Signals:**  
   - Generates sinusoidal signals at different frequencies (`f0`, `f0/2`, `10*f0`).  
   - Plots each signal individually to visualize its behavior over time.  
   - Provides a combined plot of all three signals.  

2. **DTMF Signal Generator:**  
   - Plays the corresponding DTMF tone when a key is pressed.  
   - Interactive GUI built with Tkinter.  
   - Displays a plot of the generated signal in real time.  
   - Applies fade-in and fade-out to avoid click noises.  

## Features
- Signal generation and audio playback in Python.  
- Visualization with Matplotlib.  
- Interactive DTMF keypad GUI using Tkinter.  
- High-precision numerical calculations using NumPy.  
- Sound playback with SoundDevice library.  

## Installation and Usage
1. Ensure Python 3.x is installed.  
2. Install required packages:
   ```bash
   pip install numpy matplotlib sounddevice

3. Clone the repository or download the files:
   git clone https://github.com/atalaykarakaya/Signals-and-Systems-Homework-1.git

4. Run the scripts:
   python sinusoidal_signals.py    # For sinusoidal signals
   python dtmf_signal_gui.py       # For DTMF GUI

Purpose

Learn the behavior of sinusoidal signals in the time domain.
Understand how DTMF tones are generated and played.
Practice Python-based signal generation, audio playback, and GUI integration.
