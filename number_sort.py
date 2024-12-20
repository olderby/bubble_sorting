

#attempt to convert the strings into integers throw 
def validate_strings(array_of_strings):
    array_of_integers = []
    for each in array_of_strings:
        try:
            #try to convert to integer and add it to the array of integers variablez
            array_of_integers.append(int(each))
        except:
            #if you can't return an error message then break out of the loop
            print(f"Could not convert {each} to a number`")

    return array_of_integers


#sort the numbers without built in functions but using bubble sort
def bbl_sort(array_of_integers):
    #get the length of the array
    count = len(array_of_integers)
    #save an original copy of array_of_integers
    copy = array_of_integers
    #for each element up to length of the array -1 do the following
    for j in range(count):
        #set a swap flag to track if swapped
        swapped = False
        #for each element in the entire length of the array do the following
        for i in range(0, count - j - 1):
            #if this element is larger than the one next in line
            if copy[i] > copy[i + 1]:
                #swap this element with the next element
                copy[i], copy[i + 1] = copy[i + 1], copy[i]
                #track if the element was swapped with a swapped flag
                swapped = True
            #if there was no swap break out of this loop
        if (swapped == False):
            break
    return array_of_integers

def main():
    #accept a series of number space separated from the user as one string
    string_of_numbers = input("Enter a series of numbers separated by a single space e.g. '1 2 4': ")

    #handle and empty string first
    if string_of_numbers.isspace() or string_of_numbers == "":
        print("No values were entered")

    else:
        #create an array of strings of numbers splitting up user input
        array_of_strings = string_of_numbers.split(" ")
        #create an array of integers of numbers
        array_of_integers = validate_strings(array_of_strings)
        print(array_of_integers)
        print(bbl_sort(array_of_integers))

if __name__ == "__main__":
    main()
