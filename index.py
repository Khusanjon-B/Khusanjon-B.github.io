import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot
fig, ax = plt.subplots()
ax.plot(x, y, label="Sine Wave")
ax.legend()

# Display in Streamlit
st.pyplot(fig)