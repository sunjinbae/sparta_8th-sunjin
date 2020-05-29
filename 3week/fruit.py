#fruits = ['사과','배','감','귤']

#for fruit in fruits:
 #   print(fruit);

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
# count = 0

# for fruit in fruits:
#     if fruit=='사과':
#         count += 1
# print(count)
#ctrl + / > 영역 모두 주석

def count_fruit(fruit_name):
    count = 0
    for fruit in fruits:
        if fruit == fruit_name:
            count +=1
    return count
# print(count_fruit("귤"))

people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

def get_age(person_name):
    age = None
    for person in people:
        if person["name"] == person_name:
            age = person["age"]
           # age = person.get("age",0)    //age 값을 불러오고 없는 경우 디폴트로 0을 채워넣는다.
    if age is None:
        return "해당 이름의 나이가 없습니다."
    return age
print(get_age("carry"))
print(get_age("sunjin"))

