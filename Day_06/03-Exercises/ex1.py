import os

path = os.path.dirname(__file__)

file = open(f"{path}/members.txt", 'r')
members = file.readlines()
file.close()

member = input("Enter a new member: ")
members.append(member + "\n")

file = open(f"{path}/members.txt", 'w')
file.writelines(members)
file.close()
