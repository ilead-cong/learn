##############################################################
#
##################################################################

while True:
    try:
        a = float(input('first number :'))
        b = float(input('second number :'))
        r = a/b
        print("{0} / {1} = {2}".format(a, b, r))
        break
    except (ZeroDivisionError, ValueError):
        print("the second number cna not be zero. Try again.")
    #except ValueError:
        #print('please enter number. Try again')
    
    except:
        break