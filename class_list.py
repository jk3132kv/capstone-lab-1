# create an empty list to store the class names
classes = []

# ask the user for the number of classes they are taking
num_classes = int(input('How many classes are you taking this semester? '))

#loop through and ask for the name of each class
for i in range(num_classes):
    class_name = input(f'Enter the name of class {i + 1}: ')
    classes.append(class_name)

# print all the items in the list, one per line
for class_name in classes:
    print(class_name)