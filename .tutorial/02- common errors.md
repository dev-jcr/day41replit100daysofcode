# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Make The Brackets Go Away!

👉 What is the problem here?

```python
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for name in myDictionary.items():
  print(f"{name}")
```

<details> <summary> 👀 Answer </summary>

We only gave the loop one variable instead of two.
```python
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for name, value in myDictionary.items():
  print(f"{name} {value}")
```

</details>

