# Eye Popping Filters

## Overview

Instagram is testing some new camera filters. Images go through a number of steps starting with identifying the face of the user, followed by mapping their facial features and finally applying the desired filter over each frame. You have been tasked to assist in the creation of a filter that increases the size of a persons eyes. You are provided a 2D character array describing all the features of the image using characters. Characters used to describe the image are as follows: `B` represents a background `H` represents hair, `F` represents part of the face, `N` represents part of a nose, `E` represents parts of the eyes. `M` represents parts of the mouth. Your function must expand each eye grouping by one pixel in all directions. You can assume that their will always be two groupings of eyes and you can write over other features to acheive this but you cannot change the size of the image. For example

```
B B B B B B B
B E B B B E B
B B B B B B B
```

is transformed into

```
E E E B E E E
E E E B E E E
E E E B E E E
```

## Input

Input will start with 2 integers representing the height `h` and width `w` of the image filter. It will then be followed by `h` lines of space separated characters of `w` length.

### Examples

1.

```
3 7
B B B B B B B
B E B B B E B
B B B B B B B
```

2.

```
10 10
B B B B B B B B B B
B B B B B B H H B B
B B H H H H H H B B
B B F E F F F E B B
B B F F F F F F B B
B B F F F N F F B B
B B B F M M F B B B
B B B B B B B B B B
B B B B B B B B B B
B B B B B B B B B B
```

3.

```
10 15
B B B B B B B B B B B B B B B
B B B B B B B B B B B B B B B
F F F F F F F F F F F F F F F
F F F E E E F F F F F E E E E
F F F E E E F F F F F E E E E
F F F E E E F F F F F B E F F
F F F F F F F F F F F F F F F
F F F F F F F N N F F F F F F
F F F F F F F N N F F F F F F
F F F F F F F F F F F F F F F
```

4. `78 78 78 78 78 78`
5. `3`
6. `1 5 4`

## Output

Your function must print the transformed image in the same manor as the input. You do not need to print the height and width.

### Examples

1.

```
E E E B E E E
E E E B E E E
E E E B E E E
```

2.

```
B B B B B B B B B B
B B B B B B H H B B
B B E E E H E E E B
B B E E E F E E E B
B B E E E F E E E B
B B F F F N F F B B
B B B F M M F B B B
B B B B B B B B B B
B B B B B B B B B B
B B B B B B B B B B
```

3.

```
B B B B B B B B B B B B B B B
B B B B B B B B B B B B B B B
F F E E E E E F F F E E E E E
F F E E E E E F F F E E E E E
F F E E E E E F F F E E E E E
F F E E E E E F F F E E E E E
F F E E E E E F F F F E E E F
F F F F F F F N N F F F F F F
F F F F F F F N N F F F F F F
F F F F F F F F F F F F F F F
```

## Extensions

- What is the complexity of your algorithm? Can it be improved?
- Adjust your program so it also outputs the area of each eye grouping. If there is only one grouping print the area followed by 0.
- Create a new function that switches the positions of the nose and mouth of a person.
- Create a new function that rotates the image 90 degrees clockwise.
