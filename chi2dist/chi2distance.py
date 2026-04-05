import numpy as np
import pandas as pd
from collections import Counter


def chi_square_distance(arr1, arr2):
    """
    Calculates chi square distance between any two same sized arrays. The values can be text as well.
    :param arr1: Array of categorical values
    :param arr2: Array of categorical values
    :return:
    """
    counter1 = Counter(arr1)
    counter2 = Counter(arr2)

    chi_square = 0
    for key in set(counter1.keys()).union(counter2.keys()):
        n1 = counter1[key] if key in counter1 else 0
        n2 = counter2[key] if key in counter2 else 0
        chi_square += ((n1 - n2) ** 2) / (n1 + n2)

    return chi_square


def pad_lists(list1, list2):
    """
    Checks if list1 and list2 have different levels, and pad them accordingly. List1 and List2 can be of
    different lengths
    :param list1: Array or list of categorical values
    :param list2: Array or list of categorical values
    :return: Padded lists with zeroes
    """
    freq1 = sorted(Counter(list1).items())
    freq2 = sorted(Counter(list2).items())

    # Get unique categories from both arrays and sort by category name
    categories = sorted(set([category for category, count in freq1] + [category for category, count in freq2]))

    # Pad frequency distributions to have the same size across both arrays
    freq1_padded = []
    freq2_padded = []
    for category in categories:
        count1 = next((count for c, count in freq1 if c == category), 0)
        count2 = next((count for c, count in freq2 if c == category), 0)
        freq1_padded.append(count1)
        freq2_padded.append(count2)

    return freq1_padded, freq2_padded, categories


def chi_square_statistic(arr1, arr2, contains_frequency=None):
    """
    Calculates the chi square statistic for 2 sample homogeneity test. The original array is converted
    into frequency distribution (contingency table) for chi square calculation. It tests the null hypothesis
    if all levels of two or more populations are drawn from similar distribution.
    The chi square statistic can also be used as proxy to chi square distance
    :param arr1: List or array of categorical values
    :param arr2: List or array of categorical values
    :param contains_frequency: if None, create freq distribution
    :return: Chi sqr statistic for homogeneity test

    Example:
    1.    row1 = [164,22,104,28] ; row2 = [859, 521, 444, 894]
          chi_square_statistic(row1, row2, contains_frequency='Yes')

    2.    row1 = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D'];    row2 = ['A','B','B','C','C','C', 'D']
          chi_square_statistic(row1, row2, contains_frequency=None)
    """
    # Test if number of levels is same in both the arrays, else throw an exception

    try:
        if not contains_frequency:
            counts1, counts2, classes = pad_lists(arr1, arr2)
            # categories1, counts1 = np.unique(arr1, return_counts=True)
            # categories2, counts2 = np.unique(arr2, return_counts=True)

            # If number of levels differ, then pad the lists appropriately with zeroes

        else:
            assert len(arr1) == len(arr2), "Length of arrays must be same"
            counts1 = arr1
            counts2 = arr2

        freq_df = pd.DataFrame({'obs_A1': counts1, 'obs_A2': counts2})
        freq_df['row_sum'] = freq_df['obs_A1'] + freq_df['obs_A2']

        col_A1_sum = freq_df['obs_A1'].sum()
        col_A2_sum = freq_df['obs_A2'].sum()
        grand_sum = col_A1_sum + col_A2_sum

        freq_df['exp_A1'] = freq_df['row_sum'].apply(lambda x: x*col_A1_sum/grand_sum)
        freq_df['exp_A2'] = freq_df['row_sum'].apply(lambda x: x * col_A2_sum / grand_sum)

        freq_df['chisqr_a1'] = freq_df.apply(lambda row: ((row['obs_A1']-row['exp_A1'])**2)/row['exp_A1'], axis=1)
        freq_df['chisqr_a2'] = freq_df.apply(lambda row: ((row['obs_A2'] - row['exp_A2']) ** 2) / row['exp_A2'], axis=1)

        # chi_sqr = freq_df['chisqr_a1'].sum() + freq_df['chisqr_a2'].sum()
        return freq_df['chisqr_a1'].sum() + freq_df['chisqr_a2'].sum()

    except AssertionError as e:
        print(e)

