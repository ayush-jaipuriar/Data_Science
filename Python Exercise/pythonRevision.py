#formatted Strings
name = 'Ayush'
age = 21
print(f'Hi {name}! You are {age} years old')

#List slicing , taking reference and taking copy
amazon_cart = ['laptop', 'sunglasses', 'toys', 'grapes']
new_cart = amazon_cart #new_cart takes the reference of amazon_cart hence any changes made to new_cart gets reflected on amazon_cart as well
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

amazon_cart = ['laptop', 'sunglasses', 'toys', 'grapes']
new_cart = amazon_cart[:] # here a copy of list amazon_cart gets stored in new_cart hence any changes made to new_card does not get reflected on amazon_card
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

#List remove methods
fruits = ['apple', 'mango', 'banana']
x = fruits.pop()
print(x)
print(fruits)
fruits.remove('apple')
print(fruits)

#List methods
letters = ['a','b','c','d']
print(letters.index('b')) #list.index(element) method
#print(letters.index('e')) #returns ValueError

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

#List sort() method
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)

def myFunc(e):
	return len(e)
cars.sort(key=myFunc) #sorting according to key
print(cars)
def myFunc(e):
  return e['year']

cars = [ #sorting a dict based list according to the 'year' key
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)

#join() string method 
words = ['Coding', 'is','fun']
print(' '.join(words))
name = ['Mr', 'Jaipuriar']
print('.'.join(name))

#list unpacking
a,b,*others,e,f = [1,2,3,4,5,6,7]
print(a)
print(b)
print(others)
print(e)
print(f)

#None
a= None
print(a)

#Dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")
y = car.get("price", 15000)

print(x)
print(y)

print(car.keys())
car.update({'color':'white'})
print(car)

#SETS 
my_set = {'Apple', 'Mango', 'Banana'}
print(my_set)
my_set.add('Grapes')
print(my_set)
my_set.update(['Orange', 'Pineapple'])
print(my_set)
for items in my_set:
	print(items)
