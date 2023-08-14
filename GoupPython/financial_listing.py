#!C:\Users\vkamp\Desktop\QAP4\QAP-4-Files-VA\myenv\Scripts\python.exe

from datetime import datetime

def financial_listings():    
    print()
    print('HAB TAXI SERVICES FINANCIAL LISTINGS ') 
    print()
    print('DRIVER    TRANSACTION         TRANSACTION        HST           TOTAL') 
    print('ID         DATE                 AMOUNT                ')
    print('======================================================================')  

    # Read revenues records from file

    with open('../DataFiles/Revenue.dat', 'r') as file:
        # intiating accumulator variables for totals
        total_transactions = 0
        tot_hst = 0
        tot_cost = 0
        tot_tran_count = 0
        for record in file:
            record.strip()
            
            #reading each record and slicing elements and assigning elements to variables
            
            line = record.split(',')
            transaction_id=line[0].strip() 
            tran_date=line[1].strip()
            description=line[2].strip()
            driver_id=line[3].strip() 
            tran_amount=float(line[4].strip())
            hst=float(line[5].strip())
            total=float(line[6].strip())
            
            # Incrementing accumulators
            tot_tran_count +=1
            total_transactions +=tran_amount
            tot_hst += hst
            tot_cost += total  
            
            # formating dates
            tran_date = tran_date.replace('/','-')
            datetime.strptime(tran_date,"%Y-%m-%d")
            
            # printing drivers financial listings  
            print(f'{driver_id:<5}     {tran_date:<20s}   ${tran_amount:<10}     ${hst:<9.2f}    ${total:<9.2f} ') 
    print('======================================================================') 
    print(f'Total transactions: {tot_tran_count}           ${total_transactions:<10.2f}     ${tot_hst:<10.2f}   ${tot_cost:<10.2f}') 
    print()
