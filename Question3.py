import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Loading the file path
filePath = 'weight-height.csv'

# Check if the file exists in the given path
if not os.path.isfile(filePath):
    print(f"Error: The file '{filePath}' was not found. Please check the file path.")
else:
    # Step 2: Read the CSV file
    data = pd.read_csv(filePath)

    # Step 3: Heights and Weights
    lengths_in_inches = data['Height'].values  # Heights in inches
    weights_in_pounds = data['Weight'].values  # Weights in pounds

    # Step 4: Converting lengths to centimeters and weights to kilograms
    lengths_in_cm = lengths_in_inches * 2.54  # 1 inch = 2.54 cm
    weights_in_kg = weights_in_pounds * 0.453592  # 1 pound = 0.453592 kg

    # Step 5: Calculating the means of lengths and weights
    mean_length_cm = np.mean(lengths_in_cm)
    mean_weight_kg = np.mean(weights_in_kg)

    # Step 6: Plot the histogram for heights in cm
    plt.figure(figsize=(8, 6))
    plt.hist(lengths_in_cm, bins=20, color='Red', edgecolor='Blue', alpha=0.7)
    plt.title('Histogram of Heights (cm)', fontsize=14)
    plt.xlabel('Height (cm)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    # Print the means
    print(f"Mean Height: {mean_length_cm:.2f} cm")
    print(f"Mean Weight: {mean_weight_kg:.2f} kg")
