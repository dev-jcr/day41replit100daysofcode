# Dictionaries With Loops

Loops and lists are a perfect pair. Dictionaries and loops are a bit trickier.  This is because each dictionary item is made up of two parts - the name of the key and the actual value of that key.



## I've Lost My Keys!
Let's set up a looped dictionary.

👉 Using a `for` loop, like we would with a list, will output the values, _but not the keys_.  Not ideal. 

```python
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for i in myDictionary:
  print(myDictionary[i])

```
##
👉 This loop uses the `.values()` method, which can be run on a data type. We still only get the value, and not the key.

```python
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for value in myDictionary.values():
  print(value)

```

## I've Got The Key...I've Got The Secret

There is a better way! 

Here's a loop that will output both key **and** value.  

👉 The `.items()` function returns the key name and value. Note that I've supplied the loop with two arguments: 'name' and 'value').

This example will just output the names and values using an fString.

```python
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for name,value in myDictionary.items():
  print(f"{name}:{value}")
```

## A Bit Iffy

Let's go one step further and use some `if` statements inside the loop.

👉 This example makes a comment about the strength key.

```python
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for name,value in myDictionary.items():
  print(f"{name}:{value}")

  if (name == "strength"):
    print("Whoa, SO STRONG!")
```
##
👉This example uses **nested** `if` statements to react to the key name **and** the value stored within it.

```python
myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

for name,value in myDictionary.items():
  print(f"{name}:{value}")

  if (name == "strength"):
    if value > 100:
      print("Whoa, SO STRONG")
    else:
      print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")
```

### Try it out and harness the power of iteration with your dictionary!