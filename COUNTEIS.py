country_code = {'India' : '0091',
                'Australia' : '0011',
                'Nepal' : '00977'}
print("Country code for india-")
print(country_code.get('India' , 'Not Found'))
print("Country code for Australia-")
print(country_code.get('Australia' , 'Not Found'))
print("Country code for Nepal-")
print(country_code.get('Nepal' , 'Not Found'))
print("Country code for USA-")
print(country_code.get('USA' , 'Not Found'))