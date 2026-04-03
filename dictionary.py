#Write a program to check the frequency of a value in a dictionary - {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.

test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

print("The original dictionary : " + str(test_dict))

K = 2

count = 0
for key in test_dict:
    if test_dict[key] == K:
        count += 1


print("Frequency of k is :" + str(count))


#Write a program to return the country code for various countries. Here’s a dictionary of different country codes - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}

country_code = {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}

print("Country code for India is :-- ")
print(country_code.get('India','Not found'))

print("country_code for japan" )
print(country_code.get('japan','Not found'))
