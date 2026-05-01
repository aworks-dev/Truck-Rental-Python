
# Program  - Truck rental
# ---------------------------------------------------------------------
# Variable           Type            Porpose
# ---------------------------------------------------------------------
#choose              str             get input from user to choose a menu option and making while loop work
#strclass            str             2D list of information about company rentals
#time                str             takes user input choosing days or weeks options
#askclass            str             takes user input to determine which class is needed
#milesneeded         int             takes user input on how many miles are needed
#total               float           saves and displays calculations done in functions
#weeks               int             takes user input of how many weeks needed
#days                int             takes user input of how many days needed

#defining main function
def main ():
    choose="go" #stating choose variable to let while loop run
    #stating 2d list
    strclass=[["A","21.19","0.59","109.39"],["B","29.79","0.67","159.79"],["C","37.59","0.79","199.99"]]
    #making a while loop
    while choose != "X":
        #display output
        print("----------------------------------------")
        print("*             Truck Rental             *")
        print("----------------------------------------\n")
        print("For truck rental enter (R)")
        print("To exit enter (X)")
        print("note: refunds are NOT given for unused miles.")
        #asking for user input and capitalize it
        choose=input("\nEnter menu selection: ").upper()
        #if statement
        if choose == "R":
            try: #error decoding
                time=input("Is it daily rental or weekly rental? (D/W): ").upper() #asking for input and capitalize it
                if time == "D" or time == "W": #if statement to run only if input is correct for time
                    askclass=str(input("EnterClassification (A,B,C): ")).upper() #asking for input and capitalize it
                    if askclass =="A" or askclass == "B" or askclass == "C": #if statement to run only if input is correct for askclass
                        milesneeded=int(input("Enter how many miles are needed: ")) #asking for number input
                        if time =="D": #if statement for days option
                            total=func_days(time,askclass,milesneeded,strclass)#function call for func_days
                            #display output to user and taking input to go back to the loop
                            print("total: $", total,sep="")
                            input("press enter to continue")        
                        elif time == "W": #if statement for weeks option
                            total=func_weeks(time,askclass,milesneeded,strclass)#function call for func_weeks
                            #display output to user 
                            print("total: $",total,sep="")
                            input("press enter to continue")#input to go back to the loop
                    elif askclass !="A" or askclass !="B" or askclass !="C": #displaying error message if input isnt one of the options
                        print("error, input is not an option")
                        input("press enter to continue")#input to go back to the loop
                elif time != "D" or time!="W": #displaying error message if input isnt one of the options
                    print("error, input is not an option")
                    input("press enter to continue")#input to go back to the loop
            except: #displaying error message if input isnt a number
                print("error in input")
                input("press enter to continue") #input to go back to the loop
        elif choose == "X": #ending the loop option
            print("")
        else:
            print("error, input was not an option") #displaying error message if input isnt one of the options
            input("press enter to continue")#input to go back to the loop

#defining func_weeks function
def func_weeks(time,askclass,milesneeded,strclass):
    weeks=int(input("Enter how many weeks: "))#taking user input as a number
    try:#error decoding if weeks doesnt equal a number
        if askclass == "A":
            if milesneeded >= (160*weeks):#determining if miles from user input is more than 160
                #funciton caling for calc_weekly, saving it in total variable and formatting for 0.00 decimal places
                total=format(calc_weekly(float(strclass[0][3]),int(weeks),int(milesneeded),float(strclass[0][2])),'0.2f')
                return total #returning total
            else:
                #funciton caling for calc_weekly while making sure there is no refund for under 160 miles
                #saving it in total variable and formatting for 0.00 decimal places
                total=format(calc_weekly(float(strclass[0][3]),int(weeks),int(160*weeks),float(strclass[0][2])),'0.2f')
                return total #returning total
        elif askclass == "B":
            if milesneeded >= (160*weeks):#determining if miles from user input is more than 160
                #funciton caling for calc_weekly, saving it in total variable and formatting for 0.00 decimal places
                total=format(calc_weekly(float(strclass[1][3]),int(weeks),int(milesneeded),float(strclass[1][2])),'0.2f')
                return total #returning total
            else:
                #funciton caling for calc_weekly while making sure there is no refund for under 160 miles
                #saving it in total variable and formatting for 0.00 decimal places
                total=format(calc_weekly(float(strclass[1][3]),int(weeks),int(160*weeks),float(strclass[1][2])),'0.2f')
                return total
        elif askclass == "C":
            if milesneeded >= (160*weeks):#determining if miles from user input is more than 160
                #funciton caling for calc_weekly, saving it in total variable and formatting for 0.00 decimal places
                total=format(calc_weekly(float(strclass[2][3]),int(weeks),int(milesneeded),float(strclass[2][2])),'0.2f')
                return total #returning total
            else:
                #funciton caling for calc_weekly while making sure there is no refund for under 160 miles
                #saving it in total variable and formatting for 0.00 decimal places
               total=format(calc_weekly(float(strclass[2][3]),int(weeks),int(160*weeks),float(strclass[2][2])),'0.2f')
               return total #returning total
    except:
        print("error in input")#error in entering a number
        input("press enter to continue")#taking user input to return to the loop

#defining func_days function
def func_days(time,askclass,milesneeded,strclass):
    days=int(input("Enter how many days: ")) #taking user input as a number
    try:#error decoding
        if askclass == "A":
            #funciton caling for calc_daily, saving it in total variable and formatting for 0.00 decimal places
            total=format(calc_daily(float(strclass[0][1]),days,milesneeded,float(strclass[0][2])),'0.2f')
            return total #returning total
        elif askclass == "B":
            #funciton caling for calc_daily, saving it in total variable and formatting for 0.00 decimal places
            total=format(calc_daily(float(strclass[1][1]),days,milesneeded,float(strclass[1][2])),'0.2f')
            return total #returning total
        elif askclass == "C":
            #funciton caling for calc_daily, saving it in total variable and formatting for 0.00 decimal places
            total=format(calc_daily(float(strclass[2][1]),days,milesneeded,float(strclass[2][2])),'0.2f')
            return total #returning total
    except:
        print("error in input")#error in inputing a number
        input("press enter to continue")#asking for input to return to loop

#defining calc_daily function
def calc_daily(base,days,miles,milesrate): 
    total=(base*days)+(miles*milesrate)
    return total #returning total

#defining calc_weekly function
def calc_weekly(base,weeks,miles,milesrate):
    total=(base*weeks)+((miles-(160*weeks))*milesrate)
    return total #returning total

main()           

##Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
##Type "help", "copyright", "credits" or "license()" for more information.
##>>> 
##----------------------------------------
##*             Truck Rental             *
##----------------------------------------
##
##For truck rental enter (R)
##To exit enter (X)
##note: refunds are NOT given for unused miles.
##
##Enter menu selection: r
##Is it daily rental or weekly rental? (D/W): d
##EnterClassification (A,B,C): b
##Enter how many miles are needed: 135
##Enter how many days: 2
##total: $150.03
##press enter to continue
##----------------------------------------
##*             Truck Rental             *
##----------------------------------------
##
##For truck rental enter (R)
##To exit enter (X)
##note: refunds are NOT given for unused miles.
##
##Enter menu selection: r
##Is it daily rental or weekly rental? (D/W): w
##EnterClassification (A,B,C): c
##Enter how many miles are needed: 390
##Enter how many weeks: 2
##total: $455.28
##press enter to continue
##----------------------------------------
##*             Truck Rental             *
##----------------------------------------
##
##For truck rental enter (R)
##To exit enter (X)
##note: refunds are NOT given for unused miles.
##
##Enter menu selection: x
##
##>>> 
