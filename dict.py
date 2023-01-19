merge_dict={}
dict_one={"Roll.no":"04",
          "Name":"Jomol"}
dict_two={"Place":"Kannur",
          "PIN":"670706"}
for key,value in dict_one.items():
    merge_dict[key]=value
for key,value in dict_two.items():
    merge_dict[key]=value
print(merge_dict)