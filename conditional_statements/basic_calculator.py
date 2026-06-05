# As I've read the article on if else statement in python I'll practice basic calculator using if else statement

# option = input("Please Enter Required Operation: \n A:+\n B:-\n C:X\n D:/ \n", )
# option = option.capitalize()

# val1 = int(input("Please Enter Value 1:::::::"))
# val2 = int(input("Please Enter Value 2:::::::"))

# if(option == "A"):
#     print("Answer:", val1 + val2)
# elif(option == "B"):
#     print("Answer:", val1 - val2)
# elif(option == "C"):
#     print("Answer:", val1 * val2)
# elif(option == "D"):
#     print("Answer:", val1 / val2)
# else:
    # print("Sorry Wrong Incorrect Selection")

# Above are the basic patterns and keywords for if & else statement. by following these statements and rules we can also do nested conditional statements. logics are same but method is little bit different.


# As we know that, in other programmin languages like js and dart we have a concept of switch statement which is considered to be faster than traditional if & else statement. Let us see this concept in python.
# number = 2

# match number:
#     case 1:
#         print("One")
#     case 2 | 3:
#         print("Two or Three")
#     case _:
#         print("Other number")



# str_name = "Mohsin"
# str_name = "Hasan"
# str_name = "Brother"
str_name = "Arbab"


match str_name:
    case "Arbab":
        print("Brother")
    case "Hasan" | "Mohsin":
        print("Myself")
    case _:
        print("No one else")


