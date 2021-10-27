signature = input('Insert signature type: ')
billing = float(input('Insert annual billing: '))
percentage = 00

if signature.lower() == 'basic':
    percentage = 0.3
elif signature.lower() == 'silver':
    percentage = 0.2
elif signature.lower() == 'gold':
    percentage = 0.1
elif signature.lower() == 'platinum':
    percentage = 0.05

bonus = billing * percentage
print('Bonus value is: {:.2f}'.format(bonus))