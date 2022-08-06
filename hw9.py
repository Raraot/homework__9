import functools
RTY = {}

def input_error(func):                                                    # декоратор обробки помилок
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            print("""You have not entered all the data!!!
--------------------------------------------------------------------------------------------------
for adding new phone number please input:   add name tel.      (example: add Volodymyr 345-45-45)
for change please input:                    change name tel.   (example: change Volodymyr 2345789)
for reading please input:                   phone name         (example: phone Volodymyr)
--------------------------------------------------------------------------------------------------""")
        except KeyError:
            print("This user was not found in the phone book!")
        except ValueError:
            print("Invalid value. Try again.")
    return wrapper


def welcome(func):                                                        # декоратор оформлення привітання
    def inner(*args, **kwargs):
        print("-"*32+"\nWelcome to Assistant Console Bot\n"+"-"*32)
        return func(*args, **kwargs)
    return inner


@ input_error
def handler(vvod):                                                        # функція обробки команд
    if vvod.lower() == "hello":
        return "How can I help you?"
    elif vvod.lstrip()[0:3].lower() == "add":
        RTY[vvod.split(" ")[1]] = vvod.split(" ")[2]
    elif "change" in vvod.lower():
        RTY[vvod.split(" ")[1]] = vvod.split(" ")[2]
    elif "phone" in vvod.lower():
        return RTY[vvod.split(" ")[1]]
    elif "show all" in vvod.lower():
        if RTY == {}:
            my_string ="Your phone book is empty."
        else:
            my_string ="Display full phone book:\n"
            for key, value in RTY.items():
                my_string += ('{:<12} {:<15}\n'.format(key, value))
        return my_string
    else:
        return "Unknown command, please input correct data or command!"


@ welcome
def main():
    while True:
        vvod = input(": ")
        if vvod.strip().lower() in [".", "good bye", "close", "exit", "stop", "palyanytsya"]:
            print("Good bye!")
            break
        else:
            print_me = handler(vvod)
            if print_me != None:                                                # необхідне прінтування 
                print(print_me)
            continue


if __name__ == '__main__':
    main()