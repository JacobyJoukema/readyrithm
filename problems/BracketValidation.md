# Bracket Validation

## Overview

You have been tasked with writing a parsing function for a new programming language to ensure that brackets are properly nested. This language uses three types of brackets "{", "[", and "<". This language allows for infinite nesting of brackets but at each level the bracket requires the respective closing bracket. For example "{<[]>}" has the appropriate closing bracket at each level, whereas "{>}" has a ">" closing bracket at the same level as a "{" opening bracket.

## Input

The compiler provides your function with a string of brackets limited to the following characters "{", "}", "[", "]", "<", ">"

### Examples

1. {}
2. <[]{<>}>
3. {><>}
4. <<><<<<>>>>>

## Output

Your function must print a string to console. If the brackets are properly nested output: "Valid" if the brackets are improperly nested output "Error: {i}" where i is the index of the error in the input string.

### Examples

1. Valid
2. Valid
3. Error: 1
4. Valid
