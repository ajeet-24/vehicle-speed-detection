import streamlit as st
import pandas as pd

st.title("Traffic Monitoring Dashboard")

df = pd.read_csv("vehicle_data.csv")

st.subheader("Raw Vehicle Data")
st.dataframe(df)

# Vehicle type counts
st.subheader("Vehicle Type Distribution")
vehicle_counts = df["vehicle_type"].value_counts()
st.bar_chart(vehicle_counts)

# Direction analysis
st.subheader("Traffic Direction Analysis")
direction_counts = df["direction"].value_counts()
st.bar_chart(direction_counts)

# Speed statistics
st.subheader("Speed Statistics")
st.write("Average speed:", int(df["speed_kmh"].mean()))
st.write("Maximum speed:", df["speed_kmh"].max())

# Speed chart
st.subheader("Speed Distribution")
st.line_chart(df["speed_kmh"])

# Show processed video
st.subheader("Processed Detection Video")
st.video("output_vid.mp4")