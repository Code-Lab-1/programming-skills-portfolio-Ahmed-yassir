guests = ["yousif","musa", "saeed","tayseer","tariq"]

name = guests[0].title()
print(name+ ", please come to lunch.")

name = guests[1].title()
print(name+ ", please come to lunch.")

name = guests[2].title()
print(name+ ", please come to lunch.")

name = guests[1].title()
print("\nSorry, " + name + " cant make it to lunch.")

del(guests[1])
guests.insert(1, "ahmed","ali")

name = guests[0].title()
print("\n" + name + ", please come to lunch.")

name = guests[1].title()
print(name + ", please come to lunch.")

name = guests[2].title()
print(name + ", please come to lunch.")