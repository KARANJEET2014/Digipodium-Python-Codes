name = input('Enter you Name: ')
email = input('Enter your E-mail ID: ')
mobile = input('Enter your Mobile: ')
city = input('Enter City of Residence: ')

#nested if-else
if len(name) > 1:
    if '@' in email and len(email) > 11:
        if len(mobile) ==10 and mobile.isnumeric():
            if city in ['Lucknow', 'delhi', 'Noida']:
                print('Your data is saved, Thankyou!')
            else:
                print('Sorry, we are not available in your location')
        else:
            print('Invalid Mobile number')
    else:
        print('Invalid E-mail ID')
else:
    print('You are a Chinese')
    