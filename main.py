terms = []
defins = []
print("Start by adding your terms")
term1 = input("What is your first term?: ")
defin1 = input("Now define you first term: ")
terms.append(term1)
defins.append(defin1)
add = input("Would you like to add a term?: ")
while add == "yes":
    term2 = input("What term would you like to add?: ")
    terms.append(term2)
    defin2 = input("Now define your term: ")
    defins.append(defin2)
    add = input("Would you like to add another term?: ")
else:
    study = input("Would like to study your terms?: ")
    if study == "yes":
        print("Terms: " ,str(terms) , "Definitions(In order of their corresponding terms): " ,str(defins))
        done_study = input("Would you like to add more terms?: ")
        while done_study == "yes":
            add == "yes"

    else:
        input("Would you like to add a term?: ")
        add == "yes"