# [Software Sauna](https://www.softwaresauna.com/) Code Challenge

- Path following algorithm in ASCII Map
- Find the position of character `@`
- Follow the path, stop when character `x` is reached

## Code Challenge

Write a piece of code that takes ASCII map as an input and outputs the collected letters and the list of characters of the travelled path.

  - Input: 
    - ASCII map (hard-coded, in a file, copied from a magic scroll - your choice)
  - Output:
    - Collected letters
    - Path as characters

What we are looking for in the solution (things which will bring you points ;)):

- clean code
    - small methods/functions/classes
    - good naming
    - minimise code duplication
    - separation of logic (e.g. walking around the map) and scaffolding (e.g. loading the map)
- tests
    - acceptance tests with pasted examples from below
    - microtests - small bits of logic should be tested separately (possible if clean code principles are observed, see above) ... for more on microtests see [this article](https://www.geepawhill.org/2020/06/12/microtest-tdd-more-definition)

## Valid maps

### Map 1 - a basic example

```
  @---A---+
          |
  x-B-+   C
      |   |
      +---+
```

Expected result: 
- Letters ```ACB```
- Path as characters ```@---A---+|C|+---+|+-B-x```

### Map 2 - go straight through intersections

```
  @
  | +-C--+
  A |    |
  +---B--+
    |      x
    |      |
    +---D--+
```

Expected result: 
- Letters ```ABCD```
- Path as characters ```@|A+---B--+|+--C-+|-||+---D--+|x```

### Map 3 - letters may be found on turns

```
  @---A---+
          |
  x-B-+   |
      |   |
      +---C
```

Expected result: 
- Letters ```ACB```
- Path as characters ```@---A---+|||C---+|+-B-x```

### Map 4 - do not collect a letter from the same location twice

```
     +-O-N-+
     |     |
     |   +-I-+
 @-G-O-+ | | |
     | | +-+ E
     +-+     S
             |
             x
```

Expected result: 
- Letters ```GOONIES```
- Path as characters ```@-G-O-+|+-+|O||+-O-N-+|I|+-+|+-I-+|ES|x```

### Map 5 - keep direction, even in a compact space

```
 +-L-+
 |  +A-+
@B+ ++ H
 ++    x
```

Expected result: 
- Letters ```BLAH```
- Path as characters ```@B+++B|+-L-+A+++A-+Hx```

## Invalid maps:

### Map 6 - no start

```
     -A---+
          |
  x-B-+   C
      |   |
      +---+
```

Expected result: Error

### Map 7 - no end

```
   @--A---+
          |
    B-+   C
      |   |
      +---+
```

Expected result: Error

### Map 8 - multiple starts

```
   @--A-@-+
          |
  x-B-+   C
      |   |
      +---+
```

Expected result: Error

### Map 9 - multiple ends

```
   @--A---+
          |
  x-Bx+   C
      |   |
      +---+
```

Expected result: Error

### Map 10 - T forks

```
        x-B
          |
   @--A---+
          |
     x+   C
      |   |
      +---+
```

Expected result: Error

### Map 11 - broken path

```
   @--A-+
        |
         
        B-x
```

Expected result: Error

### Map 12 - multiple starting paths

```
  -B-@-A-x
```

Expected result: Error

### Map 13 - fake turn

```
  @-A-+-B-x
```

Expected result: Error


## In the end, let's keep things simple

- the only valid characters are the ones appearing in the example maps; anything else found must result in an error
- turns can be letters or `+`
- it doesn't matter what lays beyond `x` on the path

Notice: Valid input examples are mostly jagged matrices (rows don't contain the same number of elements) so that's evidently OK.
