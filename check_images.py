#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# PROGRAMMER: Your Name Here
# DATE CREATED: YYYY-MM-DD
# REVISED DATE: YYYY-MM-DD
#
# PURPOSE: 
# Classifies pet images using a pretrained CNN model, compares these
# classifications to the true identity of the pets in the images, and
# summarizes how well the CNN performed. The true labels are extracted
# from filenames, and results are analyzed for accuracy across three
# CNN architectures to determine which performs best.
#
# Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
#

# NOTE:
# Please make sure to select the correct virtual environment to avoid package issues.
# To ensure project files (images, dogfile) are found across different environments,
# I added automatic path detection using the os package instead of hardcoded paths.
# This centralizes path handling here for easy updates and clarity.
# Alternatively, this logic of detecting path using os could go in get_input_args.py, but main.py is clearer as the entry point. 

# -------------------- Imports --------------------
from time import time
from print_functions_for_lab_checks import *

# Imports custom-defined functions
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results
import os

# -------------------- Main Program --------------------
def main():

    start_time = time()

    # Step 1: Get command line arguments
    in_arg = get_input_args()
    check_command_line_arguments(in_arg)

    # Step 2: Dynamically detect base path of current script
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

    # Step 3: Fix argument paths by joining with BASE_PATH (if not already absolute)
    if not os.path.isabs(in_arg.dir):
        in_arg.dir = os.path.join(BASE_PATH, in_arg.dir)

    if not os.path.isabs(in_arg.dogfile):
        in_arg.dogfile = os.path.join(BASE_PATH, in_arg.dogfile)

    # Now your args are ready with correct paths
    results = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results)

    classify_images(in_arg.dir, results, in_arg.arch)
    check_classifying_images(results)

    adjust_results4_isadog(results, in_arg.dogfile)
    check_classifying_labels_as_dogs(results)

    results_stats = calculates_results_stats(results)
    check_calculating_results(results, results_stats)

    print_results(results, results_stats, in_arg.arch,
                  print_incorrect_dogs=True, print_incorrect_breed=True)

    # Final timing
    end_time = time()
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          f"{int(tot_time // 3600):02d}:{int((tot_time % 3600) // 60):02d}:{int((tot_time % 3600) % 60):02d}")

if __name__ == "__main__":
    main()