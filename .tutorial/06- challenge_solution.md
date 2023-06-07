# Solution (No Peeking!)
![](https://www.youtube.com/watch?v=J-ea9g4R9PI)

<details> <summary> 👀 Answer </summary>

```python
website = {"name": None, "url": None, "desc": None, "rating": None}

for name in website.keys():
  website[name] = input(f"{name}: ")

print()
for name, value in website.items():
  print(f"{name}: {value}")
```

</details>