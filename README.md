# PyAnagram V2
Remastered version of my old PyAnagram program (trash coded)

## Algorithm
Anagrams Algorithm:
Factor of each letter / factors of repeating letters (1 if none)

Example:
`Mathematics`: 
- Length: `11`
- Repeating letters: `M, A, T`
- Formula: `11*10*9*8*7*6*5*4*3*2*1 / ((2*1) * (2*1) * (2*1)) = 4989600`, so mathematically saying, `Mathematics` has 4989600 possible variations

## Functioning
Now that the amount of variations were found, we have to actually build these variations by simply making a `while` loop that runs until the length of a list that has all the shuffled names is the same as the amount of variations possible.

```py
if not len(names) == variations: # if its still not the same:
  random.shuffle(string) # import random module
  if string not in names:
    names.append(''.join(string)) # append to the list only if its not there, preventing duplicated ones...
else: # once matched the same amount, print them all
  print('>', ', '.join(sorted(names)))
  print('>', len(names), '/', variations)
  break 
```

So that is how you can find the anagrams for a string. 

Old project had 155 lines, this one got 28 (lol)
