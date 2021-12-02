# Subway Navigator

## Overview

You have been tasked to create a subway navigation system that counts the number of stops ridden by passengers. This software will be used in a number of cities and needs to be able to accomodate different subway systems and will directly effect how much each passenger pays as it is used in the payment system. You will be provided with the following data.

1. The structure of the subway system
2. Start and End Station

## Input

Input will be provided in the following formats:

### Subway System Structure

A subway can be described by listing the stations throughout each line. For example a simple system consisting of three stations along a single line would be described as follows:

```
Alpha Bravo Charlie
```

This system could be further complicated by describing another line as follows:

```
Delta Bravo Echo
```

In this updated example there are two lines that intersect at the Bravo station. Subway system structure will be given as follows in the command line

```
n
1-line
...
n-line
```

Where n is the number of lines in the system, and each line is an ordered list of stations.

### Start and End Stations

Start and end stations will be entered after the final subway line in the format: {Start} {End} or

```
Alpha Echo
```

### Examples

1.

```
1
Alpha Bravo
Alpha Bravo
```

2.

```
1
Alpha Bravo
Bravo Alpha
```

3.

```
2
Alpha Bravo Charlie
Delta Bravo Echo
Alpha Echo
```

4.

```
3
Alpha Bravo Charlie Delta Echo
Bravo Foxtrot Golf
Delta Hotel Echo
Foxtrot Echo
```

## Output

Your function must return or print the number of stations traversed from start to finish. Count the end station but not the start station.

### Examples

1. 1
2. 1
3. 2
4. 4

## Extensions

How would you extend this program to accomodate distance traveled between each station?
How would you deal with invalid start and end points?
What information must you assume about a passenger based on the given information?
