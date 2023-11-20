import tkinter as tk
from tkinter import ttk
import io
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import requests



def fetch_data_and_plot():
    data = requests.get("http://localhost:5000/getAveragesFromSongFeatures").json()

    labels = list(data.keys())
    values = list(data.values())

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_xlabel("X-axis Label")
    ax.set_ylabel("Y-axis Label")
    ax.set_title("Bar Graph")

   
    image_stream = io.BytesIO()
    FigureCanvasAgg(fig).print_png(image_stream)

    return image_stream