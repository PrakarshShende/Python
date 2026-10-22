import matplotlib.pyplot as plt


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
temperatures = [12, 15, 18, 22, 26, 30]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Line plot
axes[0, 0].plot(months, temperatures, marker="o", color="royalblue")
axes[0, 0].set_title("Monthly Temperature (Line Plot)")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Temperature (°C)")
axes[0, 0].grid(True, linestyle="--", alpha=0.5)

# Bar plot
axes[0, 1].bar(months, temperatures, color="orange")
axes[0, 1].set_title("Monthly Temperature (Bar Plot)")
axes[0, 1].set_xlabel("Month")
axes[0, 1].set_ylabel("Temperature (°C)")

# Scatter plot
axes[1, 0].scatter(months, temperatures, color="seagreen", s=60)
axes[1, 0].set_title("Monthly Temperature (Scatter Plot)")
axes[1, 0].set_xlabel("Month")
axes[1, 0].set_ylabel("Temperature (°C)")
axes[1, 0].grid(True, linestyle="--", alpha=0.5)

# Histogram
axes[1, 1].hist(temperatures, bins=5, color="mediumpurple", edgecolor="black")
axes[1, 1].set_title("Temperature Distribution (Histogram)")
axes[1, 1].set_xlabel("Temperature (°C)")
axes[1, 1].set_ylabel("Number of Months")

fig.suptitle("Matplotlib Plot Examples")
plt.tight_layout()
plt.show()