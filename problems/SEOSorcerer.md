# SEO Sorcerer

## Overview

A digital marketing agency is looking to build a backlink explorer so they can easily identify websites that reference their clients products and services. A member of your team has written a web scrapping tool that generates a list of urls and the links that each page has on it's site. Links can be categorized as internal, meaning they point to somewhere else on the same site, or external, meaning they point to a different site entirely. Given a list of urls and their referenced links create a function that returns the total number of internal links and external links that point to each site. URLs will always be given without a subdomain or protocol. A site can be defined as a collection of pages with a common domain name.

## Input

Input will start with 1 integer denoting the number of web pages that have been scraped, `n` followed by `n` sets of page and link relations separated by one line. Input can be summarized as

```
n
page-0
page-0-link-0 page-0-link-1 page-0-link-2 page-0-link-3
...
page-n
page-n-link-0 page-n-link-1 page-n-link-2

```

### Examples

1.

```
2
google.com
google.com/feeling-lucky google.com/search
google.com/feeling-lucky
google.com/search
```

2.

```
2
store.com
store.com/products store.com/hire store.com/buy
blog.com
store.com/products/1 store.com/products/2 store.com/products/3 blog.com/home blog.com/posts/1
```

3.

```
3
wiki.com/history
museum.com/dinosaurs college.com/history dogs.com/hunting
wiki.com/donate
paypal.com/wiki-donate wiki.com/home
museum.com/home
museum.com/dinosaurs museum.com/history wiki.com/museums
```

4. `78 78 78 78 78 78`
5. `3`
6. `1 5 4`

## Output

Output will be given on `n` lines where each line is a site domain followed by the number of internal and external links space separated

### Examples

1.

```
google.com 3 0
```

2.

```
store.com 3 3
blog.com 2 0
```

3.

```
wiki.com 1 1
museum.com 2 1
college.com 0 1
dogs.com 0 1
paypal.com 0 1

```

## Extensions

- What data structure did you choose and why?
- What is the complexity of your algorithm?
