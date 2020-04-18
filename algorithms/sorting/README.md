# Iterative Sorting

## Selection Sorting
Selection happens when we iterate through a list of items. As we are iterating though the list we are seeking to find the mallest value. Whenever we find we swap it with the 0th index. We then iterate over the list again but now we only look at the values after the 0th index. We continute this process until all values are sorted.

Time Complexity: O(n^2)