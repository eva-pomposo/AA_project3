import pandas as pd
import matplotlib.pyplot as plt

def barChartCounts(exact_counts, csuros_counter, lossy_count):
    # Plot the exact counts
    plt.bar(exact_counts["letter"], exact_counts["count"])
    plt.title("Exact counter")
    plt.xlabel("Letter")
    plt.ylabel("Count")
    plt.savefig("graphics/exact_counter_counts.png")
    plt.clf()

    # Plot the counts of the Csuros counter
    plt.bar(csuros_counter["letter"], csuros_counter["count"], color="orange")
    plt.title("Csurös’ counter")
    plt.xlabel("Letter")
    plt.ylabel("Count")
    plt.savefig("graphics/csuros_counter_counts.png")
    plt.clf()

    # Plot the counts of the Lossy-Count algorithm
    plt.bar(lossy_count["letter"][lossy_count['k'] == 3], lossy_count["count"][lossy_count['k'] == 3], color="yellowGreen")
    plt.title("Lossy-Count (Top-3)")
    plt.xlabel("Letter")
    plt.ylabel("Count")
    plt.savefig("graphics/lossy_count_top3_counts.png")
    plt.clf()

    plt.bar(lossy_count["letter"][lossy_count['k'] == 5], lossy_count["count"][lossy_count['k'] == 5], color="olive")
    plt.title("Lossy-Count (Top-5)")
    plt.xlabel("Letter")
    plt.ylabel("Count")
    plt.savefig("graphics/lossy_count_top5_counts.png")
    plt.clf()

    plt.bar(lossy_count["letter"][lossy_count['k'] == 10], lossy_count["count"][lossy_count['k'] == 10], color="green")
    plt.title("Lossy-Count (Top-10)")
    plt.xlabel("Letter")
    plt.ylabel("Count")
    plt.savefig("graphics/lossy_count_top10_counts.png")
    plt.clf()

exact_counts_Nazareth = pd.read_csv('results/exact_counts_Nazareth.txt', sep="\s+", header=0, names=["letter", "order", "count"])
csuros_counter_Nazareth = pd.read_csv('results/csuros_counter_Nazareth.txt', sep="\s+", header=0, names=["letter", "order", "count"])
lossy_count_Nazareth = pd.read_csv('results/lossy_count_Nazareth.txt', sep="\s+", header=0, names=["letter", "k", "order", "count"])

barChartCounts(exact_counts_Nazareth, csuros_counter_Nazareth, lossy_count_Nazareth)

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