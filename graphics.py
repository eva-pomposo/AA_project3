import pandas as pd
import matplotlib.pyplot as plt

def barChartCounts(exact_counts, csuros_counter, lossy_count):
    # Create a figure with 3 subplots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

    # Plot the exact counts
    ax1.bar(exact_counts["letter"], exact_counts["count"])
    ax1.set_title("Exact counter")
    ax1.set_xlabel("Letter")
    ax1.set_ylabel("Count")

    # Plot the counts of the Csuros counter
    ax2.bar(csuros_counter["letter"], csuros_counter["count"], color="orange")
    ax2.set_title("Csurös’ counter")
    ax2.set_xlabel("Letter")
    ax2.set_ylabel("Count")

    # Plot the counts of the Lossy-Count algorithm
    ax3.bar(lossy_count["letter"][lossy_count['k'] == 10], lossy_count["count"][lossy_count['k'] == 10], color="green")
    ax3.set_title("Lossy-Count (Top-10)")
    ax3.set_xlabel("Letter")
    ax3.set_ylabel("Count")

    # Show the plot
    plt.savefig("graphics/barChartCounts.png")
    
    return

def barChartCountsLossyCount(lossy_count):
    # Create a figure with 3 subplots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

    # Plot the counts of the Lossy-Count algorithm
    ax1.bar(lossy_count["letter"][lossy_count['k'] == 3], lossy_count["count"][lossy_count['k'] == 3], color="yellowGreen")
    ax1.set_title("Lossy-Count (Top-3)")
    ax1.set_xlabel("Letter")
    ax1.set_ylabel("Count")
    
    # Plot the counts of the Lossy-Count algorithm
    ax2.bar(lossy_count["letter"][lossy_count['k'] == 5], lossy_count["count"][lossy_count['k'] == 5], color="olive")
    ax2.set_title("Lossy-Count (Top-5)")
    ax2.set_xlabel("Letter")
    ax2.set_ylabel("Count")
    
    # Plot the counts of the Lossy-Count algorithm
    ax3.bar(lossy_count["letter"][lossy_count['k'] == 10], lossy_count["count"][lossy_count['k'] == 10], color="green")
    ax3.set_title("Lossy-Count (Top-10)")
    ax3.set_xlabel("Letter")
    ax3.set_ylabel("Count")

    # Show the plot
    plt.savefig("graphics/barChartCountsLossyCount.png")
    
    return

exact_counts_Christuslegenden_german = pd.read_csv('results/exact_counts_Christuslegenden_german.txt', sep="\s+", header=0, names=["letter", "order", "count"])
csuros_counter_Christuslegenden_german = pd.read_csv('results/csuros_counter_Christuslegenden_german.txt', sep="\s+", header=0, names=["letter", "order", "count"])
lossy_count_Christuslegenden_german = pd.read_csv('results/lossy_count_Christuslegenden_german.txt', sep="\s+", header=0, names=["letter", "k", "order", "count"])

barChartCounts(exact_counts_Christuslegenden_german, csuros_counter_Christuslegenden_german, lossy_count_Christuslegenden_german)
barChartCountsLossyCount(lossy_count_Christuslegenden_german)