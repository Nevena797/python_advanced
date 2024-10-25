from collections import deque

water_quantity = int(input())
people = deque()
name = input()

while name != "Start":
    people.append(name)
    name = input()

command = input()

while command != "End":
    data = command.split()
    if len(data) == 1:
        liters_wanted = int(data[0])

        if water_quantity >= liters_wanted:
            water_quantity -= liters_wanted
            person = people.popleft()
            print(f"{person} got water")
        else:
            person = people.popleft()
            print(f"{person} must wait")
    else:
        liters_to_fill = int(data[1])
        water_quantity += liters_to_fill
    command = input()
print(f"{water_quantity} liters left")
