import numpy as np
import urllib.request

urllib.request.urlretrieve(
    'https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', 
    'climate.txt')
climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)
print(climate_data)
print(climate_data.shape)
weights = np.array([0.3, 0.2, 0.5])
yields = climate_data @ weights
print(yields) 
print(yields.shape)
#concatenates the yields and climate_data matrices to form one matric climate_results
climate_results = np.concatenate((climate_data, yields.reshape(10000, 1)), axis=1)
print(climate_results)
''' There are a couple of subtleties here:
Since we wish to add new columns, we pass the argument axis=1 to np.concatenate. The axis argument specifies the dimension for concatenation.
The arrays should have the same number of dimensions, and the same length along each except the dimension used for concatenation.
We use the np.reshape function to change the shape of yields from (10000,) to (10000,1). '''
np.savetxt('climate_results.txt', 
           climate_results, 
           fmt='%.2f', 
           delimiter=',',
           header='temperature,rainfall,humidity,yeild_apples', 
           comments='') 

#calculating total monthly installement for a loan
import math

def loan_emi(amount, duration, rate, down_payment=0):
    """Calculates the equal montly installment (EMI) for a loan.
    
    Arguments:
        amount - Total amount to be spent (loan + down payment)
        duration - Duration of the loan (in months)
        rate - Rate of interest (monthly)
        down_payment (optional) - Optional intial payment (deducted from amount)
    """
    loan_amount = amount - down_payment
    try:
        emi = loan_amount * rate * ((1+rate)**duration) / (((1+rate)**duration)-1)
    except ZeroDivisionError:
        emi = loan_amount / duration
    emi = math.ceil(emi)
    return emi