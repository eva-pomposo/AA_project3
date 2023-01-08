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

exact_counts_Nazareth = pd.read_csv('results/exact_counts_Nazareth.txt', sep="\s+", header=0, names=["letter", "order", "count"])
csuros_counter_Nazareth = pd.read_csv('results/csuros_counter_Nazareth.txt', sep="\s+", header=0, names=["letter", "order", "count"])
lossy_count_Nazareth = pd.read_csv('results/lossy_count_Nazareth.txt', sep="\s+", header=0, names=["letter", "k", "order", "count"])

barChartCounts(exact_counts_Nazareth, csuros_counter_Nazareth, lossy_count_Nazareth)
barChartCountsLossyCount(lossy_count_Nazareth)

exact_counts_Romeo_and_Juliet_dutch = pd.read_csv('results/exact_counts_Romeo_and_Juliet_dutch.txt', sep="\s+", header=0, names=["letter", "order", "count"])
csuros_counter_Romeo_and_Juliet_dutch = pd.read_csv('results/csuros_counter_Romeo_and_Juliet_dutch.txt', sep="\s+", header=0, names=["letter", "order", "count"])
lossy_count_Romeo_and_Juliet_dutch = pd.read_csv('results/lossy_count_Romeo_and_Juliet_dutch.txt', sep="\s+", header=0, names=["letter", "k", "order", "count"])

exact_counts_Romeo_and_Juliet_english = pd.read_csv('results/exact_counts_Romeo_and_Juliet_english.txt', sep="\s+", header=0, names=["letter", "order", "count"])
csuros_counter_Romeo_and_Juliet_english = pd.read_csv('results/csuros_counter_Romeo_and_Juliet_english.txt', sep="\s+", header=0, names=["letter", "order", "count"])
lossy_count_Romeo_and_Juliet_english = pd.read_csv('results/lossy_count_Romeo_and_Juliet_english.txt', sep="\s+", header=0, names=["letter", "k", "order", "count"])

exact_counts_Romeo_and_Juliet_finnish = pd.read_csv('results/exact_counts_Romeo_and_Juliet_finnish.txt', sep="\s+", header=0, names=["letter", "order", "count"])
csuros_counter_Romeo_and_Juliet_finnish = pd.read_csv('results/csuros_counter_Romeo_and_Juliet_finnish.txt', sep="\s+", header=0, names=["letter", "order", "count"])
lossy_count_Romeo_and_Juliet_finnish = pd.read_csv('results/lossy_count_Romeo_and_Juliet_finnish.txt', sep="\s+", header=0, names=["letter", "k", "order", "count"])

exact_counts_Romeo_and_Juliet_french = pd.read_csv('results/exact_counts_Romeo_and_Juliet_french.txt', sep="\s+", header=0, names=["letter", "order", "count"])
csuros_counter_Romeo_and_Juliet_french = pd.read_csv('results/csuros_counter_Romeo_and_Juliet_french.txt', sep="\s+", header=0, names=["letter", "order", "count"])
lossy_count_Romeo_and_Juliet_french = pd.read_csv('results/lossy_count_Romeo_and_Juliet_french.txt', sep="\s+", header=0, names=["letter", "k", "order", "count"])

exact_counts_Romeo_and_Juliet_german = pd.read_csv('results/exact_counts_Romeo_and_Juliet_german.txt', sep="\s+", header=0, names=["letter", "order", "count"])
csuros_counter_Romeo_and_Juliet_german = pd.read_csv('results/csuros_counter_Romeo_and_Juliet_german.txt', sep="\s+", header=0, names=["letter", "order", "count"])
lossy_count_Romeo_and_Juliet_german = pd.read_csv('results/lossy_count_Romeo_and_Juliet_german.txt', sep="\s+", header=0, names=["letter", "k", "order", "count"])

# Create a figure with 5 subplots
fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9), (ax10, ax11, ax12), (ax13, ax14, ax15)) = plt.subplots(5, 3, figsize=(23, 23))

# Plot the exact counts
ax1.bar(exact_counts_Romeo_and_Juliet_dutch["letter"], exact_counts_Romeo_and_Juliet_dutch["count"])
ax1.set_title("Exact counter (Romeo and Juliet, Dutch)")
ax1.set_xlabel("Letter")
ax1.set_ylabel("Count")

ax4.bar(exact_counts_Romeo_and_Juliet_english["letter"], exact_counts_Romeo_and_Juliet_english["count"])
ax4.set_title("Exact counter (Romeo and Juliet, English)")
ax4.set_xlabel("Letter")
ax4.set_ylabel("Count")

ax7.bar(exact_counts_Romeo_and_Juliet_finnish["letter"], exact_counts_Romeo_and_Juliet_finnish["count"])
ax7.set_title("Exact counter (Romeo and Juliet, Finnish)")
ax7.set_xlabel("Letter")
ax7.set_ylabel("Count")

ax10.bar(exact_counts_Romeo_and_Juliet_french["letter"], exact_counts_Romeo_and_Juliet_french["count"])
ax10.set_title("Exact counter (Romeo and Juliet, French)")
ax10.set_xlabel("Letter")
ax10.set_ylabel("Count")

ax13.bar(exact_counts_Romeo_and_Juliet_german["letter"], exact_counts_Romeo_and_Juliet_german["count"])
ax13.set_title("Exact counter (Romeo and Juliet, German)")
ax13.set_xlabel("Letter")
ax13.set_ylabel("Count")

# Plot the Csuros Counters
ax2.bar(csuros_counter_Romeo_and_Juliet_dutch["letter"], csuros_counter_Romeo_and_Juliet_dutch["count"], color="orange")
ax2.set_title("Csurös’ counter (Romeo and Juliet, Dutch)")
ax2.set_xlabel("Letter")
ax2.set_ylabel("Count")

ax5.bar(csuros_counter_Romeo_and_Juliet_english["letter"], csuros_counter_Romeo_and_Juliet_english["count"], color="orange")
ax5.set_title("Csurös’ counter (Romeo and Juliet, English)")
ax5.set_xlabel("Letter")
ax5.set_ylabel("Count")

ax8.bar(csuros_counter_Romeo_and_Juliet_finnish["letter"], csuros_counter_Romeo_and_Juliet_finnish["count"], color="orange")
ax8.set_title("Csurös’ counter (Romeo and Juliet, Finnish)")
ax8.set_xlabel("Letter")
ax8.set_ylabel("Count")

ax11.bar(csuros_counter_Romeo_and_Juliet_french["letter"], csuros_counter_Romeo_and_Juliet_french["count"], color="orange")
ax11.set_title("Csurös’ counter (Romeo and Juliet, French)")
ax11.set_xlabel("Letter")
ax11.set_ylabel("Count")

ax14.bar(csuros_counter_Romeo_and_Juliet_german["letter"], csuros_counter_Romeo_and_Juliet_german["count"], color="orange") 
ax14.set_title("Csurös’ counter (Romeo and Juliet, German)")
ax14.set_xlabel("Letter")
ax14.set_ylabel("Count")

# Plot the Lossy Counters
ax3.bar(lossy_count_Romeo_and_Juliet_dutch["letter"][lossy_count_Romeo_and_Juliet_dutch['k'] == 10], lossy_count_Romeo_and_Juliet_dutch["count"][lossy_count_Romeo_and_Juliet_dutch['k'] == 10], color="green")
ax3.set_title("Lossy-Count Top-10 (Romeo and Juliet, Dutch)")
ax3.set_xlabel("Letter")
ax3.set_ylabel("Count")

ax6.bar(lossy_count_Romeo_and_Juliet_english["letter"][lossy_count_Romeo_and_Juliet_english['k'] == 10], lossy_count_Romeo_and_Juliet_english["count"][lossy_count_Romeo_and_Juliet_english['k'] == 10], color="green")
ax6.set_title("Lossy-Count Top-10 (Romeo and Juliet, English)")
ax6.set_xlabel("Letter")
ax6.set_ylabel("Count")

ax9.bar(lossy_count_Romeo_and_Juliet_finnish["letter"][lossy_count_Romeo_and_Juliet_finnish['k'] == 10], lossy_count_Romeo_and_Juliet_finnish["count"][lossy_count_Romeo_and_Juliet_finnish['k'] == 10], color="green")
ax9.set_title("Lossy-Count Top-10 (Romeo and Juliet, Finnish)")
ax9.set_xlabel("Letter")
ax9.set_ylabel("Count")

ax12.bar(lossy_count_Romeo_and_Juliet_french["letter"][lossy_count_Romeo_and_Juliet_french['k'] == 10], lossy_count_Romeo_and_Juliet_french["count"][lossy_count_Romeo_and_Juliet_french['k'] == 10], color="green")
ax12.set_title("Lossy-Count Top-10 (Romeo and Juliet, French)")
ax12.set_xlabel("Letter")
ax12.set_ylabel("Count")

ax15.bar(lossy_count_Romeo_and_Juliet_german["letter"][lossy_count_Romeo_and_Juliet_german['k'] == 10], lossy_count_Romeo_and_Juliet_german["count"][lossy_count_Romeo_and_Juliet_german['k'] == 10], color="green")
ax15.set_title("Lossy-Count Top-10 (Romeo and Juliet, German)")
ax15.set_xlabel("Letter")
ax15.set_ylabel("Count")

plt.savefig("graphics/Romeo_and_Juliet.png")