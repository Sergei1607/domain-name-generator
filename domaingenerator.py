# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:44:07 2021

@author: serge
"""

def main():
    pronoum = []
    adj = []
    noun = []
    sub = []
    
    
    def randomgenerator(pro, adj, noun, sub):
        print("\n")
        print("Your random domain names are: \n")
        for i in pro:
             for j in adj:
                 for k in noun:
                     for l in sub:
                         print(i+j+k+l)
        

    def values():
        
        star= input("Do you want to start creating your random domain names? y/n: ").lower()
   
        if star == "y":
        
            
            p1 = True
            while p1:
                pro = input("Pick your pronoums or type 'q' for exit: ")
                if pro != "q":
                    pronoum.append(pro)
                else:
                    p1 = False
                
            ad1 = True
            while ad1:
                 ad = input("Pick your adjectives or type 'q' for exit: ")
                 if ad != "q":
                     adj.append(ad)
                 else:
                    ad1 = False   
                
            no1 = True
            while no1:
                no = input("Pick your noums or type 'q' for exit: ")
                if no != "q":
                     noun.append(no)
                else:
                    no1 = False   
                
            sub1 = True
            while sub1:
                su = input("Pick your subs or type 'q' for exit: ")
                if su != "q":
                    sub.append(su)
                else:
                    sub1 = False   
                         
            randomgenerator(pronoum, adj, noun, sub)
            
        else:
            print("\n")
            print("See you soon!")
                
            
    values()
    print("\n")
    
    

main()


