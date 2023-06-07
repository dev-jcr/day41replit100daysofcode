# Dictionaries with loops

webinfo={"name":None, "url":None,"description":None,"rating":None}
title="🌟Website Rating🌟"
print(f"{title:^35}")
print()

for name in webinfo.keys():
  webinfo[name]=input(f"{name}: ")
  
print()
for name, value in webinfo.items():
  print(f"{name}:{value}")