# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*
```python
myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

for name in myDictionary.items():
  print(f"{name}:{value}")

  if (name == "strength"):
  if value > 100:
    print("Whoa, SO STRONG")
  else:
    print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")
```
<details> <summary> 👀 Answer </summary>

  ```python 
  
myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

for name, value in myDictionary.items():
  print(f"{name}: {value}")

if (name == "strength"): 
  if value > 100: # This nested if wasn't indented properly
    print("Whoa, SO STRONG")
  else:
    print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")
```
</details>