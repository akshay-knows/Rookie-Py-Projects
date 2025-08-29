'''This program converts a sentence into individual list elements (words)'''
import os

os.system("cls")
input("\nThis program converts a sentence into individual list elements (words) \n ---Press 'Enter' to Continue---\n")

while True:
    string = input("Enter or paste your sentence: \n")

    # Split the sentence into words
    finallist = string.split()

    print("\nConverted List:", finallist, "\n")

    choice = input("Would you like to continue? \ny = Yes\nn = No\n:: ").strip().lower()
    if choice == "n":
        break

os.system("cls")
print("\n\nAlright \n\n\n!! Bye for now")
