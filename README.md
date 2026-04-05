# Chi-Square Distance for High-Dimensional Categorical Data

[![DOI](https://zenodo.org/badge/1201937172.svg)](https://doi.org/10.5281/zenodo.19431370)

## Overview

This package provides efficient implementations of chi-square distance and chi-square statistical measures for categorical data. It is designed for computing distances between categorical distributions and performing two-sample homogeneity tests on high-dimensional categorical datasets.

## Mathematical Foundation

### Chi-Square Distance

The chi-square distance measure quantifies the dissimilarity between two categorical distributions. Given two frequency distributions represented as arrays of categorical values, the chi-square distance is computed as follows.

For two sequences of categorical data arr1 and arr2, let n₁(k) and n₂(k) denote the frequency counts for category k in arr1 and arr2 respectively. The chi-square distance is defined as:

$$d_{\chi^2}(\text{arr}_1, \text{arr}_2) = \sum_{k} \frac{(n_1(k) - n_2(k))^2}{n_1(k) + n_2(k)}$$

**Note:** Some formulations include a factor of 1/2. This implementation follows the convention without the scaling factor.

where the sum is taken over all unique categories present in either distribution. Categories absent from one distribution are assigned a frequency count of zero.

This distance metric is particularly useful for comparing categorical distributions and is sensitive to differences in category frequencies.

### Chi-Square Statistic

The chi-square statistic is used for two-sample homogeneity testing. It tests the null hypothesis that two or more populations are drawn from the same distribution. 

For a 2×k contingency table with observed frequencies O_{ij} and expected frequencies E_{ij}, the chi-square statistic is:

$$\chi^2 = \sum_{i} \sum_{j} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

The expected frequency for cell (i,j) is calculated as:

$$E_{ij} = \frac{\text{Row}_i \text{ Sum} \times \text{Col}_j \text{ Sum}}{\text{Grand Total}}$$

## Installation

**Note:** Package distribution via PyPI and uv is forthcoming. Currently, installation from source is recommended for academic and research use.

### From source

Clone the repository and install dependencies:

```bash
git clone https://github.com/ashutosh-karna/Chi-Sqr-Categorical-Distance.git
cd Chi-Sqr-Categorical-Distance
pip install -r requirements.txt
```

## Dependencies

- numpy >= 1.20.0
- pandas >= 1.0.0

## Functions

### chi_square_distance(arr1, arr2)

Computes the chi-square distance between two categorical arrays.

**Parameters:**
- `arr1`: Array or list of categorical values
- `arr2`: Array or list of categorical values

**Returns:**
- `chi_square`: Scalar value representing the chi-square distance

**Example:**
```python
from chi2dist.chi2distance import chi_square_distance

arr1 = ['A', 'A', 'B', 'B', 'C', 'D']
arr2 = ['A', 'B', 'B', 'C', 'C', 'C']

distance = chi_square_distance(arr1, arr2)
print(distance)
```

### chi_square_statistic(arr1, arr2, contains_frequency=None)

Computes the chi-square statistic for a two-sample homogeneity test.

**Parameters:**
- `arr1`: List or array of categorical values or frequency counts
- `arr2`: List or array of categorical values or frequency counts
- `contains_frequency`: If None, function treats inputs as categorical values and computes frequency distributions. If 'Yes', treats inputs as pre-computed frequency counts

**Returns:**
- `chi_square_statistic`: Scalar value representing the chi-square test statistic

**Examples:**

Using categorical data:
```python
from chi2dist.chi2distance import chi_square_statistic

row1 = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D']
row2 = ['A', 'B', 'B', 'C', 'C', 'C', 'D']

statistic = chi_square_statistic(row1, row2, contains_frequency=None)
print(statistic)
```

Using frequency counts:
```python
row1 = [164, 22, 104, 28]
row2 = [859, 521, 444, 894]

statistic = chi_square_statistic(row1, row2, contains_frequency='Yes')
print(statistic)
```

### pad_lists(list1, list2)

Internal utility function that aligns frequency distributions of two categorical arrays to include all unique categories from both arrays.

**Parameters:**
- `list1`: Array or list of categorical values
- `list2`: Array or list of categorical values

**Returns:**
- `freq1_padded`: Padded frequency counts for list1
- `freq2_padded`: Padded frequency counts for list2
- `categories`: Sorted list of all unique categories

## Use Cases

1. **Clustering Analysis**: Use chi-square distance as a distance metric in clustering algorithms for categorical data
2. **Statistical Testing**: Perform hypothesis tests to determine if two categorical distributions are significantly different
3. **Feature Comparison**: Compare feature distributions in machine learning datasets with categorical variables
4. **Data Analysis**: Analyze similarity between groups in survey or census data

## Citation

If you use this package in your research, please cite it as follows:

```bibtex
@software{karna2026,
  title={Chi-Square Distance for High-Dimensional Categorical Data},
  author={Karna, Ashutosh},
  year={2026},
  version={1.0.0},
  doi={10.5281/zenodo.19431370},
  url={https://doi.org/10.5281/zenodo.19431370}
}
```

Or in plain text:

```
Karna, A. (2026). Chi-Square Distance for High-Dimensional Categorical Data. Version 1.0.0. 
https://doi.org/10.5281/zenodo.19431370
```

## License

This software is provided as-is for research purposes. Please contact the author for more details.

## Author

Ashutosh Karna

## Contact

For questions, bug reports, or contributions regarding this package, please contact:

**Email:** ashutosh.karna@gmail.com