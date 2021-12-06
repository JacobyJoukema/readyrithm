# Sort of a Tall Tree

## Overview

A data scientist is building a tree visualizer, she wants to demonstrate how a single set of data can be inserted into the same data structure and produce different trees. She needs you to write a function that constructs two un-balanced binary search trees out of a given array of integers. The first tree is based on the data given where the first integer of the list is the root node and the tree is build serially adding all the nodes in order give. The second tree must be constructed such that the order of insertion into the tree goes from largest to smallest. Once both trees are built the data scientist needs you to print the heights of each in the format described below.

## Input

Input will be a list of integers provided through standard input

### Examples

1. `100 190 19 85 78 10 60 50`
2. `1 2 3 4 5 6 7 8 9 10`
3. `10 9 8 7 6 5 4 3 2 1`
4. `78 78 78 78 78 78`
5. `3`
6. `1 5 4`

## Output

Your function must return or print the height of each tree in the following format `{h1} {h2}` where `h1` is the height of the unordered insertion and `h2` is the height of the largest to smallest insertion.

### Examples

1. `6 8`
2. `8 8`
3. `8 8`
4. `8 8`
5. `1 1`
6. `3 3`

## Extensions

- Adapt this program so that it produces a third tree that is balanced and outputs its height in the format `{h1} {h2} {h3}` as h3
- Create add and remove functions for your BST.
- Adapt this program to use bubble sort, merge sort and quick sort.
