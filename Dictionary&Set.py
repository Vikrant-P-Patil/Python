#DICTIONARY IN PYTHON#

#used to store data values in "key:value" pairs

#they are unordered, mutable and dont follow duplicate keys

#each valu is seperated by comma

#we can even store list and tuples in dectionary


dict = {
    "name" : "lomdu",
    "age"  : 18,
    "marks": "hah",
    "list" : ["python","html"],
    "tuple" : ("dict", " set")


}

print(dict)

#we can also get specific keys inside a dictionary

print(dict["name"])

#we can reasign new values to the key sperateley

null_dict = {}
print(null_dict)

#NESTED DICTIONARY#

student = {
    "name": "don",
    "subject" : {
        "phy" : 97,
        "math" : 88
    }
}

print(student["subject"]["phy"])

#DICTIONARY METHOD#

dict.keys() #returns all keys

dict.values() #returns all values

dict.items() #returns all (key,val) pairs as tupels

dict.get("name2") #returns the key according to value, if the value does not exist it will not give error and just display "none".

dict.update({"chem" : "delhi"})
#inserts the specified items to the dictionary


#SET IN PYTHON#

#set is the collection of the unordered items 

#each element in the set must be unique and immutable

# *SETS ARE MUTABLE, BUT THE ELEMENTS IN THE SET ARE IMMUTABLE

#LISTS and DICTIONARY are never stored in a set

set1= {1,2,3,2} 
print(set1)
#repeated elements stored only once, so it resolved to {1,2,3}

null_set = set()
set2={3,4,5}

#SET METHODS#

set.add()
#adds an element, can add tuples but cannot add lists and dictionaries as set elements are immutable

set.remove()
#removes the element

set.clear()
#empties the set

set.pop()
#removes a random value in that set

set.union(set2)
#combines both set values and returns a new set
set2={3,4,5}
set1= {1,2,3,2}
print(set.union(set2))

set.interesection(set2)
#combines common values and returns new







