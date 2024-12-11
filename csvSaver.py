# -*- coding: utf-8 -*-

import csv
import os

def saveResults(method, iterations, durations, filename="results.csv"):
    """
    Save results to a CSV file. Each row corresponds to a method,
    and each column corresponds to the number of iterations.

    :param method: Method name.
    :param iterations: List of iteration counts.
    :param durations: List of durations for the given method.
    :param filename: Name of the CSV file to save to.
    """
    file_exists = os.path.isfile(filename)
    try:
        with open(filename, mode="ab") as csvfile:  # Open in append binary mode
            writer = csv.writer(csvfile, lineterminator="\n")
            
            # Write the header if the file does not exist
            if not file_exists:
                writer.writerow(["Method/Iterations"] + iterations)
            
            # Write the rows for each method
            writer.writerow([method] + list(durations))
    except:
        with open(filename, mode="a", newline="", encoding="utf-8") as csvfile:  # Open in append mode with utf-8 encoding
            writer = csv.writer(csvfile, lineterminator="\n")
            
            # Write the header if the file does not exist
            if not file_exists:
                writer.writerow(["Method/Iterations"] + iterations)
            
            # Write the rows for each method
            writer.writerow([method] + list(durations))