'''

Temperatura = 10.5

emri = "Greta"

mosha = 17

print(Temperatura)
print(mosha)
print(emri)


print(type(Temperatura))
print(type(mosha))
print(type(emri))

'''

#Kalkulime

x = 8

y = 9

result = x+y

print(result)

#update values

age = 30

age += 1

print(age)

#combinate values

first_name = "Greta"
last_name ="Gercari"

full_name = first_name +" "+last_name

print(full_name)

#array (lists)

fav_colors = ["red", "green", "yellow", "purpule"]
first = fav_colors[0]
second = fav_colors[1]

print(first)
print(second)

#methods for list
#append - add an item at the end of the list
fav_colors.append("orange")
print(fav_colors)

#inser - add element in a specific index
fav_colors.insert(2, "white")
print(fav_colors)

#remove

fav_colors.remove("green")
print(fav_colors)

del fav_colors[4]
print(fav_colors)

#update

fav_colors[0] = "pink"
print(fav_colors)