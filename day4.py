#task 1
"""contact = {"abc": 4561,"xyz": 4125,"tyd": 8766}
contact["ads"]= 5621
for name,num in contact.items():
    print(name,num)

print("\n\n",contact.get("ads"))"""



#task 2
"""raw_logs = ["ID01","ID02","ID01","ID05","IDO2","ID01","ID08"]
unique_users = set(raw_logs)
print(unique_users)
print("ID05" in unique_users)
print("ID10" in unique_users)
print(len(unique_users))"""

#task3
friend_a = {"python", "cooking", "hiking", "movies"}
friend_b = {"hiking", "gaming", "movies","photography", "python"}
print(friend_a | friend_b)
print(friend_a & friend_b)
print(friend_a - friend_b)
