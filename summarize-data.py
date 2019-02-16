# Dependencies
from spread import variance, standard_deviation, zipped_z_scores

def summarize(title, arr):
    print(f"Summarizing {title} \n")
    print(f"Variance: {variance(arr)} \n")
    print(f"Standard Deviation: {standard_deviation(arr)} \n")
    print(f"Z-Scores: {zipped_z_scores(arr)} \n")
    
prices = [4, 425, 984, 2932, 49]
summarize("Prices", prices)
