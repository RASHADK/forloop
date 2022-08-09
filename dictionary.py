dict={1:"he",2:"me",3:"you"}
print(dict[1])
print(dict[2])
print(dict[3])

print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get(1))
print(dict.get(2))

print(".....................")
dict.update({4:"She"})
print(dict)
dict["5"]="hello"
print(dict)
dict.pop(1)
print(dict)
dict.popitem()
print(dict)
del dict[2]
print(dict)
dict.clear()
print(dict)
