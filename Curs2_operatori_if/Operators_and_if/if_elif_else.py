# if conditon1:
#     do something if condition1 is true
# elif condition2:
#     do something if condition2 is true
# elif condition3:
#     do something if condition3 is true
# else:
#     do something else if none of condition above are true

age = int(input("Age: \n"))
if age <= 2:
    print("You are a baby")
elif age <= 12:
    print("You are a child")
elif age <= 18:
    print("You are adolescent")
elif age <= 65:
    print("You are adult")
else:
    print("You are retired")


# if milk_at_shop:
#     if zuzu:
#         buy zuzu
#     else:
#         buy something else
# else:
#     dont buy nothing

if age > 18:
    print("You are major")
    if age > 65:
        print("you are retired")
    else:
        print("you are adult")
else:
    print("You are minor")
    if age < 2:
        print("you are a baby")
    elif age <= 12:
        print("you are child")
    else:
        print("you are adolescent")