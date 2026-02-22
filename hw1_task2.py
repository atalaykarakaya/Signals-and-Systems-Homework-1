import numpy as np
import sounddevice as sd
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


fs = 44100        # Native macOS & standard Windows sample rate
T = 0.4           # Tone duration (seconds)
fade_time = 0.05  # Fade-in/out duration (prevents click noise)

sd.default.samplerate = fs
sd.default.channels = 1

# DTMF FREQUENCY TABLE


dtmf = {
    "1": (697, 1209), "2": (697, 1336), "3": (697, 1477), "A": (697, 1633),
    "4": (770, 1209), "5": (770, 1336), "6": (770, 1477), "B": (770, 1633),
    "7": (852, 1209), "8": (852, 1336), "9": (852, 1477), "C": (852, 1633),
    "*": (941, 1209), "0": (941, 1336), "#": (941, 1477), "D": (941, 1633),
}

# SIGNAL GENERATION FUNCTION

def generate_tone(key):
    f1, f2 = dtmf[key]

    # Time axis
    t = np.linspace(0, T, int(fs*T), endpoint=False)

    # Generate DTMF signal
    signal = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)

    # Normalize (avoid clipping)
    signal = signal / np.max(np.abs(signal))

    # Apply fade-in and fade-out
    fade_samples = int(fade_time * fs)
    fade_in = np.linspace(0, 1, fade_samples)
    fade_out = np.linspace(1, 0, fade_samples)

    signal[:fade_samples] *= fade_in
    signal[-fade_samples:] *= fade_out

    # Play sound
    sd.stop()
    sd.play(signal, fs)

    # Update plot (show first few milliseconds)
    ax.clear()
    ax.plot(t[:2000], signal[:2000])
    ax.set_title(f"DTMF Signal for Key {key}")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.grid(True)
    canvas.draw()

# GUI DESIGN

root = tk.Tk()
root.title("DTMF Signal Generator")
root.geometry("650x750")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

# Title
title_label = ttk.Label(root, text="DTMF Keypad", font=("Helvetica", 20))
title_label.pack(pady=15)

# Keypad Frame
keypad_frame = ttk.Frame(root)
keypad_frame.pack()

keys = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]

for r in range(4):
    for c in range(4):
        key = keys[r][c]
        btn = ttk.Button(
            keypad_frame,
            text=key,
            width=8,
            command=lambda k=key: generate_tone(k)
        )
        btn.grid(row=r, column=c, padx=8, pady=8)

# EMBEDDED PLOT AREA

fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=25)

ax.set_title("DTMF Signal")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude")
ax.grid(True)

root.mainloop()
