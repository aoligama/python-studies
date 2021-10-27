quantityTransactions = int(input('How many transactions did you make today? '))
amount = 0
totalAmount = 0
average = 0

if quantityTransactions > 0:
    for f in range(quantityTransactions):
        amount += float(input('Transaction Amount: '))
        
    average = amount / quantityTransactions
    print('Total Value: ${:.2f}'.format(amount))
    print('Average Value: ${:.2f}'.format(average))
else:
    print('No transactions performed, total amount: $0.00')