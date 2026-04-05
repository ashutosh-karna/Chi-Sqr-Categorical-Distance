"""
Example usage of chi-square distance and chi-square statistic functions.

This module demonstrates how to use the chi2dist package to:
1. Compute chi-square distance between categorical distributions
2. Perform chi-square homogeneity tests
3. Analyze categorical data using frequency distributions

Author: Ashutosh Karna
"""

import numpy as np
import sys
import os
from chi2dist.chi2distance import chi_square_distance, chi_square_statistic, pad_lists


def generate_categorical_data(num_samples, num_categories, seed=None):
    """
    Generate dummy categorical data.
    
    Parameters
    ----------
    num_samples : int
        Number of categorical samples to generate (dimensions).
    num_categories : int
        Number of unique categories for the data.
    seed : int, optional
        Random seed for reproducibility. Default is None.
    
    Returns
    -------
    numpy.ndarray
        Array of categorical values represented as integers.
    """
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(0, num_categories, num_samples)


# Example 1. Chi-square distance between two categorical distributions
def example_1_chi_square_distance():
    """
    Example 1: Computing chi-square distance between two categorical distributions.
    
    Demonstrates computing chi-square distance with raw categorical data.
    """
    print("=" * 80)
    print("EXAMPLE 1: Chi-Square Distance Between Two Categorical Distributions")
    print("=" * 80)
    
    # Generate two categorical datasets with 1000 dimensions and 5 categories
    arr1 = generate_categorical_data(1000, 5, seed=42)
    arr2 = generate_categorical_data(1000, 5, seed=43)
    
    print(f"\nDataset 1 shape: {arr1.shape}")
    print(f"Dataset 2 shape: {arr2.shape}")
    print(f"Number of unique categories in Dataset 1: {len(np.unique(arr1))}")
    print(f"Number of unique categories in Dataset 2: {len(np.unique(arr2))}")
    
    # Compute chi-square distance
    distance = chi_square_distance(arr1, arr2)
    
    print(f"\nChi-Square Distance: {distance:.4f}")
    print("Interpretation: A smaller value indicates more similar distributions.")
    print()


# Example 2. Chi-square distance with string categorical data
def example_2_chi_square_distance_with_strings():
    """
    Example 2: Computing chi-square distance with string categorical data.
    
    Demonstrates that chi-square distance works with non-numeric categories.
    """
    print("=" * 80)
    print("EXAMPLE 2: Chi-Square Distance with String Categories")
    print("=" * 80)
    
    # Generate categorical data with string labels
    categories = ['A', 'B', 'C', 'D', 'E']
    np.random.seed(42)
    arr1 = np.random.choice(categories, 1000)
    np.random.seed(44)
    arr2 = np.random.choice(categories, 1000)
    
    print(f"\nDataset 1 sample: {arr1[:20]}")
    print(f"Dataset 2 sample: {arr2[:20]}")
    
    # Compute chi-square distance
    distance = chi_square_distance(arr1, arr2)
    
    print(f"\nChi-Square Distance: {distance:.4f}")
    print()


# Example 3. Chi-square homogeneity test with raw categorical data
def example_3_chi_square_statistic_raw_data():
    """
    Example 3: Chi-square homogeneity test with raw categorical data.
    
    Performs a chi-square test to determine if two categorical distributions
    are significantly different.
    """
    print("=" * 80)
    print("EXAMPLE 3: Chi-Square Homogeneity Test - Raw Categorical Data")
    print("=" * 80)
    
    # Generate categorical data with different distributions
    np.random.seed(50)
    # Dataset 1: biased towards category 0
    arr1 = np.concatenate([
        np.random.choice([0, 1, 2, 3], 700, p=[0.5, 0.2, 0.2, 0.1]),
        np.random.choice([0, 1, 2, 3], 300, p=[0.2, 0.3, 0.3, 0.2])
    ])
    
    # Dataset 2: more balanced distribution
    arr2 = np.random.choice([0, 1, 2, 3], 1000, p=[0.3, 0.3, 0.2, 0.2])
    
    print(f"\nDataset 1 shape: {arr1.shape}")
    print(f"Dataset 2 shape: {arr2.shape}")
    
    # Compute chi-square statistic
    chi_sq_stat = chi_square_statistic(arr1, arr2, contains_frequency=None)
    
    print(f"\nChi-Square Statistic: {chi_sq_stat:.4f}")
    print("Interpretation: Higher values indicate distributions are significantly different.")
    print()


#Example 4. Chi-square homogeneity test with pre-computed frequency counts
def example_4_chi_square_statistic_with_frequencies():
    """
    Example 4: Chi-square homogeneity test with pre-computed frequency counts.
    
    Demonstrates chi-square test when data is already in frequency form.
    """
    print("=" * 80)
    print("EXAMPLE 4: Chi-Square Homogeneity Test - Frequency Counts")
    print("=" * 80)
    
    # Pre-computed frequency counts for 4 categories across 2 samples
    freq_sample1 = [164, 22, 104, 28]  # Frequencies for categories 0, 1, 2, 3
    freq_sample2 = [859, 521, 444, 894]  # Frequencies for the same categories
    
    print(f"\nSample 1 frequencies: {freq_sample1}")
    print(f"Sample 1 total: {sum(freq_sample1)}")
    print(f"\nSample 2 frequencies: {freq_sample2}")
    print(f"Sample 2 total: {sum(freq_sample2)}")
    
    # Compute chi-square statistic
    chi_sq_stat = chi_square_statistic(freq_sample1, freq_sample2, contains_frequency='Yes')
    
    print(f"\nChi-Square Statistic: {chi_sq_stat:.4f}")
    print()


# Example 5. Understanding the pad_lists functionality
def example_5_pad_lists_functionality():
    """
    Example 5: Understanding the pad_lists functionality.
    
    Demonstrates how pad_lists aligns frequency distributions when
    the two distributions have different categories.
    """
    print("=" * 80)
    print("EXAMPLE 5: Padding Lists with Different Categories")
    print("=" * 80)
    
    # Generate data with potentially different categories
    arr1 = np.array(['A', 'A', 'B', 'C', 'C', 'C', 'D'])
    arr2 = np.array(['A', 'B', 'B', 'C', 'C', 'D', 'D', 'D', 'E'])
    
    print(f"\nArray 1: {arr1}")
    print(f"Array 2: {arr2}")
    
    # Pad the lists
    freq1_padded, freq2_padded, categories = pad_lists(arr1, arr2)
    
    print(f"\nUnique categories (sorted): {categories}")
    print(f"\nPadded frequencies for Array 1: {freq1_padded}")
    print(f"Padded frequencies for Array 2: {freq2_padded}")
    print("\nExplanation: Both frequency distributions now include all categories,")
    print("with zeros for missing categories.")
    print()


def example_6_multiple_pairwise_comparisons():
    """
    Example 6: Computing pairwise chi-square distances between multiple datasets.
    
    Demonstrates how to compare 10 categorical datasets using chi-square distance.
    """
    print("=" * 80)
    print("EXAMPLE 6: Pairwise Chi-Square Distance Matrix (10 Datasets)")
    print("=" * 80)
    
    # Generate 10 categorical datasets with 1000 dimensions each
    num_datasets = 10
    num_dimensions = 1000
    num_categories = 5
    
    datasets = [
        generate_categorical_data(num_dimensions, num_categories, seed=i)
        for i in range(num_datasets)
    ]
    
    print(f"\nGenerated {num_datasets} categorical datasets")
    print(f"Each dataset has {num_dimensions} dimensions")
    print(f"Number of categories: {num_categories}")
    
    # Compute pairwise distances
    print("\nPairwise Chi-Square Distances (sample of 5x5 matrix):")
    print("-" * 60)
    
    distances = []
    for i in range(min(5, num_datasets)):
        row_distances = []
        for j in range(min(5, num_datasets)):
            if i == j:
                dist = 0.0
            else:
                dist = chi_square_distance(datasets[i], datasets[j])
            row_distances.append(dist)
            print(f"Distance(Dataset_{i}, Dataset_{j}): {dist:.4f}")
        distances.append(row_distances)
    
    print("\nNote: A distance matrix of 0 on the diagonal indicates")
    print("self-comparison. Off-diagonal elements show pairwise distances.")
    print()


def example_7_effect_of_sample_size():
    """
    Example 7: Effect of sample size on chi-square distance.
    
    Demonstrates how chi-square distance changes with different sample sizes.
    """
    print("=" * 80)
    print("EXAMPLE 7: Effect of Sample Size on Chi-Square Distance")
    print("=" * 80)
    
    # Use the same random seed for reproducibility
    np.random.seed(100)
    
    # Generate a base distribution
    base_dist = generate_categorical_data(10000, 5, seed=100)
    
    sample_sizes = [50, 100, 250, 500, 1000]
    
    print(f"\nComputing chi-square distance with varying sample sizes...")
    print(f"Comparing against base distribution (n=10000)")
    print("-" * 60)
    
    for size in sample_sizes:
        # Generate sample from different distribution
        sample = generate_categorical_data(size, 5, seed=101)
        distance = chi_square_distance(base_dist[:size], sample)
        print(f"Sample size: {size:4d} | Chi-Square Distance: {distance:.4f}")
    
    print("\nObservation: Distance values may vary with sample size due to")
    print("statistical fluctuations in the distributions.")
    print()


def example_8_categorical_feature_analysis():
    """
    Example 8: Analyzing categorical features from survey data.
    
    Demonstrates real-world usage with simulated survey responses.
    """
    print("=" * 80)
    print("EXAMPLE 8: Categorical Feature Analysis - Survey Data")
    print("=" * 80)
    
    # Simulate survey responses (e.g., satisfaction levels)
    satisfaction_levels = [1, 2, 3, 4, 5]  # 1=Very Dissatisfied to 5=Very Satisfied
    
    # Group 1: Before intervention (more negative responses)
    np.random.seed(102)
    group_before = np.random.choice(satisfaction_levels, 1000, 
                                    p=[0.3, 0.25, 0.2, 0.15, 0.1])
    
    # Group 2: After intervention (more positive responses)
    np.random.seed(103)
    group_after = np.random.choice(satisfaction_levels, 1000,
                                   p=[0.1, 0.15, 0.2, 0.3, 0.25])
    
    print(f"\nGroup Before (n={len(group_before)}):")
    unique, counts = np.unique(group_before, return_counts=True)
    for cat, count in zip(unique, counts):
        print(f"  Level {cat}: {count} responses ({100*count/len(group_before):.1f}%)")
    
    print(f"\nGroup After (n={len(group_after)}):")
    unique, counts = np.unique(group_after, return_counts=True)
    for cat, count in zip(unique, counts):
        print(f"  Level {cat}: {count} responses ({100*count/len(group_after):.1f}%)")
    
    # Perform chi-square test
    chi_sq_stat = chi_square_statistic(group_before, group_after, contains_frequency=None)
    
    print(f"\nChi-Square Statistic: {chi_sq_stat:.4f}")
    print("Interpretation: High value suggests the intervention had a significant effect.")
    print()


def example_9_distance_symmetry():
    """
    Example 9: Verifying distance symmetry property.
    
    Demonstrates that chi-square distance is symmetric: d(A,B) = d(B,A)
    """
    print("=" * 80)
    print("EXAMPLE 9: Distance Symmetry Property")
    print("=" * 80)
    
    arr1 = generate_categorical_data(1000, 4, seed=200)
    arr2 = generate_categorical_data(1000, 4, seed=201)
    
    dist_1_to_2 = chi_square_distance(arr1, arr2)
    dist_2_to_1 = chi_square_distance(arr2, arr1)
    
    print(f"\nDistance from Array 1 to Array 2: {dist_1_to_2:.6f}")
    print(f"Distance from Array 2 to Array 1: {dist_2_to_1:.6f}")
    print(f"Difference: {abs(dist_1_to_2 - dist_2_to_1):.10f}")
    print("\nVerification: The distances are symmetric (difference is near zero).")
    print()


def example_10_identical_distributions():
    """
    Example 10: Computing distance for identical distributions.
    
    Demonstrates that chi-square distance between identical distributions is zero.
    """
    print("=" * 80)
    print("EXAMPLE 10: Chi-Square Distance for Identical Distributions")
    print("=" * 80)
    
    # Create identical datasets
    arr1 = generate_categorical_data(1000, 5, seed=300)
    arr2 = arr1.copy()  # Identical copy
    
    distance = chi_square_distance(arr1, arr2)
    
    print(f"\nDataset 1 and Dataset 2 are identical copies.")
    print(f"Chi-Square Distance: {distance:.10f}")
    print("\nVerification: Distance is zero (or very close to zero) for identical distributions.")
    print()


def main():
    """
    Main function to run all examples.
    
    This function executes all ten examples demonstrating various aspects
    of chi-square distance and chi-square statistics for categorical data analysis.
    """
    print("\n")
    print("#" * 80)
    print("# Chi-Square Distance and Chi-Square Statistic - Example Usage")
    print("# Author: Ashutosh Karna")
    print("#" * 80)
    print("\n")
    
    example_1_chi_square_distance()
    example_2_chi_square_distance_with_strings()
    example_3_chi_square_statistic_raw_data()
    example_4_chi_square_statistic_with_frequencies()
    example_5_pad_lists_functionality()
    example_6_multiple_pairwise_comparisons()
    example_7_effect_of_sample_size()
    example_8_categorical_feature_analysis()
    example_9_distance_symmetry()
    example_10_identical_distributions()
    
    print("#" * 80)
    print("# All examples completed successfully!")
    print("#" * 80)
    print("\n")


if __name__ == "__main__":
    main()

