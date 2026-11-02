#List datastructure


products=["Bread", "Milk","Sugar", "Blueband"]
print(f"My products {products}")

products[0]="Cake"
print(f"Update products {products}")

products.pop()
print(products)
for p in products:
    print(p)
#tuple datastructure
#immutable,unchangeable
#used on item that dont change

location=("Nairobi","Uganda","Tanzania")
print(location)

#set datastructure
#removes duplicates
mystock={"hp","lenova","dell","hp"}
print(mystock)

#dictionary datastructure
customer={
    "name":"Eric",
    "age": "30",
    "city":"Nairobi",
    "proffession":"Software Engineer"
}
print(f"Name: {customer['name']}")

#store product and their prices
shop={
    "Bread":130,
    "Milk":90,
    "Sugar":190
}
for product,price in shop.items():
    print(product,"cost ksh",price)
print("Milk cost ksh",shop["Milk"])

#imagine you are building a school system that
#calculates the average mark of a student
marks=[76,83,67,90,79]
total=0
for mark in marks:
    total=total+mark
average=total /len(marks)
print(f"Total Marks:{total}")
print(f"Average Marks:{average}")

#create a complex
#calculator using input output and loops