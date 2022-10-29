# Python code to demonstrate
# To Sort and Reverse a String
# using list() + sort() + join()

# initializing string
test_string = "walkinthepark"

# printing original string
print("The original string : " + str(test_string))

# using list() + sort() + join
# To Sort and reverse a String
temp = list(test_string)
temp.sort(reverse=True)
res = "".join(temp)

# print result
print("String after reverse sorting : " + res)
