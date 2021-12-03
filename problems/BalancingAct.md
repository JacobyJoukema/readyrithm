# Balancing Act

## Overview

A local strongman competition has been booked in the same location as a cheerleading competition. The strongmen want to demonstrate their strength to the cheerleaders and lift as many of them as possible. A strongman can support the total weights of all the cheerleaders as long as the total weight in each hand are within 50 lbs of one another. Each cheerleader can support the weights of cheerleaders that weigh less then them but they cannot balance unless they have a cheerleader in each hand. Their goal is to build the largest inverted pyramid with a strongman supporting the base. For example the following inverted pyramid has a height of 3

        C  C C  C
         \ / \ /
          C   C
           \ /
            S

Given the weights of the cheerleaders determine the maximum height of the pyramid assuming the strong men must remain balanced and the cheerleaders carry 2 individuals who weigh less then themselves.

## Input

Input will be a list of integers provided through standard input representing the weights of all the cheerleaders.

### Examples

1. `100 125 150 120 90 95 90`
2. `100`
3. `135 150 120 90 90 55`
4. `90 90 90 90 90 90 90`
5. `150 250`
6. `75 250 50 50 45 45`

## Output

Your function must return or print the maximum height of the inverted pyramid. The strongman at the base is considered a height of 1.

### Examples

1. `3`
2. `1`
3. `2`
4. `2`
5. `1`
6. `3`

## Extensions

- How would you extend this program if each individuals left arm was weaker then their right arm and therefore could only hold less weight on one side?
- How would your solution change if the cheerleaders were trying to build the largest non-inverted pyramid and each layer could only support less weight then the layers above it?
