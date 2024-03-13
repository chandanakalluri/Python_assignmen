from Python_assignmen.src.assignment6.util import patt_l


def main():
    thickness = int(input("Enter the thickness: "))
    character = input("Enter the character: ")

    pattern_list = patt_l(thickness, character)

    for line in pattern_list:
        print(line)
main()
