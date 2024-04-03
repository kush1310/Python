# AUTHOR:- KUSH SHAH
d1 = {'Andhra Pradesh': 'Amaravati', 'Arunachal Pradesh': 'Itanagar', 'Assam': 'Dispur', 'Bihar': 'Patna', 'Chhattisgarh': 'Raipur', 'Goa': 'Panaji', 'Gujarat': 'Gandhinagar', 'Haryana': 'Chandigarh', 'Himachal Pradesh': 'Shimla', 'Jharkhand': 'Ranchi', 'Karnataka': 'Bengaluru', 'Kerala': 'Thiruvananthapuram', 'Madhya Pradesh': 'Bhopal', 'Maharashtra': 'Mumbai', 'Manipur': 'Imphal', 'Meghalaya': 'Shillong', 'Mizoram': 'Aizawl', 'Nagaland': 'Kohima', 'Odisha': 'Bhubaneswar', 'Punjab': 'Chandigarh', 'Rajasthan': 'Jaipur', 'Sikkim': 'Gangtok', 'Tamil Nadu': 'Chennai', 'Telangana': 'Hyderabad', 'Tripura': 'Agartala', 'Uttar Pradesh': 'Lucknow', 'Uttarakhand': 'Dehradun', 'West Bengal': 'Kolkata'}
for key, value in d1.items():
    capital = input("Enter capital of " + key + ": ")
    if capital == value.lower():
        print("Correct")
    else:
        print("Incorrect")

# 2nd method
import random

capital_dic={'Andhra Pradesh': 'Amaravati', 'Arunachal Pradesh': 'Itanagar', 'Assam': 'Dispur', 'Bihar': 'Patna', 'Chhattisgarh': 'Raipur', 'Goa': 'Panaji', 'Gujarat': 'Gandhinagar', 'Haryana': 'Chandigarh', 'Himachal Pradesh': 'Shimla', 'Jharkhand': 'Ranchi', 'Karnataka': 'Bengaluru', 'Kerala': 'Thiruvananthapuram', 'Madhya Pradesh': 'Bhopal', 'Maharashtra': 'Mumbai', 'Manipur': 'Imphal', 'Meghalaya': 'Shillong', 'Mizoram': 'Aizawl', 'Nagaland': 'Kohima', 'Odisha': 'Bhubaneswar', 'Punjab': 'Chandigarh', 'Rajasthan': 'Jaipur', 'Sikkim': 'Gangtok', 'Tamil Nadu': 'Chennai', 'Telangana': 'Hyderabad', 'Tripura': 'Agartala', 'Uttar Pradesh': 'Lucknow', 'Uttarakhand': 'Dehradun', 'West Bengal': 'Kolkata'}
States=list(capital_dic.keys())

print ('Let\'s learn India States and Capitals. 10 rounds. Enter exit to quit the game.')
point=0

for i in range(10):
    state=random.choice(States)
    capital = capital_dic[state]
    user_guess = input('what is the capital of %s?'%state )
    if user_guess.lower() == 'exit':  
        break
    elif user_guess.title() == capital:
        point+=1
        print('Correct! Your score is %d' %point)
    else:
        print('Incorrect. The capital of {} is {}.'.format(state,capital))
print('We are done. Your final score is %d, thank you.' %point)