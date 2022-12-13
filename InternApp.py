import numpy as np
import pandas as pd
import sys
import time
import tkinter as tk
from tkinter import filedialog

#to upload population and product files
def main():

    words = "Hello, in order to start traversing through csv files, You will need to upload the master files.\n"
    typeWrite(words)
    time.sleep(1)

    words = "Please upload Product master first when the file Explorer opens.\n"
    typeWrite(words)
    time.sleep(2)
    prodMaster = uploadFile()

    words = "Excellent! Now please do the same for Population Master.\n"
    typeWrite(words)
    time.sleep(2)
    popMaster = uploadFile()

    words = "Wonderful! Redirecting to main menu....\n\n"
    typeWrite(words)
    time.sleep(1)

    mainmenu(prodMaster, popMaster)
    return prodMaster, popMaster

def mainmenu(prodMaster, popMaster):
    #main menu
    menu = {}
    menu['1']="Product update/lookup." 
    menu['2']="Product results."
    menu['3']="Population update/lookup."
    menu['4']="Population results."
    menu['5']="Exit"


    while True: 
        options=menu.keys()
        for entry in options: 
            print(entry, menu[entry])

        selection=int(input("Please Select A Number:"))
        if selection ==int('1'): 
            res1 = prodLookup(prodMaster)
            
        elif selection ==int('2'): 
            time.sleep(1)
            words = "\nDownloading and saving as Product_Results.csv  ...\n"
            typeWrite(words)
            
            res1.to_csv('Product_Results.csv', encoding = 'utf-8', index = False)
            print()
            
        elif selection == int('3'):
            res2 = popLookup(popMaster)
            
        elif selection == int('4'):
            time.sleep(1)
            words = "\nDownloading and saving as Population_Results.csv ...\n"
            typeWrite(words)
            
            res2.to_csv('Population_Results.csv', encoding = 'utf-8', index = False)
            print()
            
        elif selection == int('5'): 
            break
        
        else: 
            print("Invalid Input! Please Select one of the options above") 

def uploadFile():
    #for opening up file explorer and returning filepath
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    file = pd.read_csv(file_path)
    
    return file


def typeWrite(words):
    for char in words:
        time.sleep(0.018)
        sys.stdout.write(char)
        sys.stdout.flush()

#prompts file upload, then checks whether product file is a lookup by seeing if column 'Product' exists
def prodLookup(prodMaster):
    lookup = uploadFile()

    if 'Product' in lookup:
        time.sleep(1)
        words = "\n This is an update file...\n"
        typeWrite(words)

        prodRes = pd.concat([prodMaster, lookup]).drop_duplicates(['Zip'], keep ='last')

        print("\n Product update Success, proceed to option 2 to download results!\n")
        
    else:
        time.sleep(1)
        words = "\n This is a lookup file... \n"
        typeWrite(words)
        
        arr = lookup['Zip'].to_numpy()
        prodRes = prodMaster.loc[prodMaster['Zip'].isin(arr)]
        print('\nPreview:\n', prodRes.head(), '\n')

    return prodRes 

def popLookup(popMaster):   
    lookup = uploadFile()

    if 'Recorded' in lookup:
        time.sleep(1)
        words = "\n This is an update file...\n"
        typeWrite(words)

        popRes = pd.concat([popMaster, lookup]).drop_duplicates(['Zip', 'Modified User'], keep ='last')

        print("\n Population update Success, proceed to option 4 to download results!\n")
        
    else:
        time.sleep(1)
        words = "\n This is a lookup file... \n"
        typeWrite(words)

        arr = lookup['Zip'].to_numpy()
        popRes = popMaster.loc[popMaster['Zip'].isin(arr)]
        print('\nPreview:\n', popRes.head(), '\n')

    return popRes



main()

# missing from lookup: N/A values are ommited when they should be displayed as N/A

# missing from Update: Updated values append at the end, values update despite recently modified user not
# being changed

