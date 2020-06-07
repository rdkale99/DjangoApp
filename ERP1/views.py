import numpy as np
from django.shortcuts import render
from .models import values
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html');

def calculate(request):
    
    CO = float(request.POST["CO"])
    CTF = float(request.POST["CTF"])
    GSBC = float(request.POST["GSBC"])
    AO = float(request.POST["AO"])
    PRD = float(request.POST["PRD"])
    WFA = float(request.POST["WFA"])
    RO = float(request.POST["RO"])
    
    Flowrate = float(request.POST["Flowrate"])
    Hours = float(request.POST["Hours"])
    
    # OTHER LOSSES
    CTS_Losses = float(request.POST["CTS_Losses"])
    WW = float(request.POST["WW"])
    UEXLOS = float(request.POST["UEXLOS"])
    TheCTS_Losses = float(request.POST["TheCTS_Losses"])
    TheWW = float(request.POST["TheWW"])
    TheUEXLOS = float(request.POST["TheUEXLOS"])
    

    # AssumptionInput

    P1_Ass1 = float(request.POST["P1_Ass1"])
    P1_Ass2 = float(request.POST["P1_Ass2"])
    P1_Ass3 = float(request.POST["P1_Ass3"])
    P1_Ass4 = float(request.POST["P1_Ass4"])
    P1_Ass4 = round(Flowrate/Hours,2)
    

    P1_TheAss1 = float(request.POST["P1_TheAss1"])
    P1_TheAss2 = float(request.POST["P1_TheAss2"])
    P1_TheAss3 = float(request.POST["P1_TheAss3"])
    P1_TheAss4 = round(Flowrate/Hours,2)
    


    ###########
    P2_Ass1 = float(request.POST["P2_Ass1"])
    P2_Ass2 = float(request.POST["P2_Ass2"])
    P2_Ass3 = float(request.POST["P2_Ass3"])
    P2_Ass4 = float(request.POST["P2_Ass4"])
    
    P2_TheAss1 = float(request.POST["P2_TheAss1"])
    P2_TheAss2 = float(request.POST["P2_TheAss2"])
    P2_TheAss3 = float(request.POST["P2_TheAss3"])
    P2_TheAss4 = float(request.POST["P2_TheAss4"])
    
    #############
    P3_Ass1 = float(request.POST["P3_Ass1"])
    P3_Ass2 = float(request.POST["P3_Ass2"])
    P3_Ass3 = float(request.POST["P3_Ass3"])
    P3_Ass4 = float(request.POST["P3_Ass4"])
    
    P3_TheAss1 = float(request.POST["P3_TheAss1"])
    P3_TheAss2 = float(request.POST["P3_TheAss2"])
    P3_TheAss3 = float(request.POST["P3_TheAss3"])
    P3_TheAss4 = float(request.POST["P3_TheAss4"])

    #############
    P4_Ass1 = float(request.POST["P4_Ass1"])
    P4_Ass2 = float(request.POST["P4_Ass2"])
    P4_Ass3 = float(request.POST["P4_Ass3"])
    P4_Ass4 = float(request.POST["P4_Ass4"])
    
    
    
    
    P4_TheAss1 = float(request.POST["P4_TheAss1"])
    P4_TheAss2 = float(request.POST["P4_TheAss2"])
    P4_TheAss3 = float(request.POST["P4_TheAss3"])
    P4_TheAss4 = float(request.POST["P4_TheAss4"])
  
    #############
    P5_Ass1 = float(request.POST["P5_Ass1"])
    P5_Ass2 = float(request.POST["P5_Ass2"])
    P5_Ass3 = float(request.POST["P5_Ass3"])
    P5_Ass4 = float(request.POST["P5_Ass4"])
    
    P5_TheAss1 = float(request.POST["P5_TheAss1"])
    P5_TheAss2 = float(request.POST["P5_TheAss2"])
    P5_TheAss3 = float(request.POST["P5_TheAss3"])
    P5_TheAss4 = float(request.POST["P5_TheAss4"])

    #############
    P6_Ass1 = float(request.POST["P6_Ass1"])
    P6_Ass2 = float(request.POST["P6_Ass2"])
    P6_Ass3 = float(request.POST["P6_Ass3"])
    P6_Ass4 = float(request.POST["P6_Ass4"])
  
    P6_TheAss1 = float(request.POST["P6_TheAss1"])
    P6_TheAss2 = float(request.POST["P6_TheAss2"])
    P6_TheAss3 = float(request.POST["P6_TheAss3"])
    P6_TheAss4 = float(request.POST["P6_TheAss4"])

    #############

    # PROCESS INPUT
    P1_FlowPercent = float(request.POST["P1_FlowPercent"])
    P1_Var1 = float(request.POST["P1_Var1"])
    P1_Var2 = float(request.POST["P1_Var2"])
    P1_Var3 = float(request.POST["P1_Var3"])
    P1_Impurities = float(request.POST["P1_Impurities"])
    P1_Mass = float(request.POST["P1_Mass"])
    P1_Wax1 = float(request.POST["P1_Wax1"])
    
    P1_Mass = P1_Var1+(P1_Var2*30/10000)+P1_Var3+P1_Impurities

    
    ##################

    P2_Var1 = float(request.POST["P2_Var1"])
    P2_Var2 = float(request.POST["P2_Var2"])
    P2_Var3 = float(request.POST["P2_Var3"])
    P2_Impurities = float(request.POST["P2_Impurities"])
    P2_Mass = float(request.POST["P2_Mass"])
    P2_Wax1 = float(request.POST["P2_Wax1"])

    
    P2_Mass = P2_Var1+(P2_Var2*30/10000)+P2_Var3+P2_Impurities

    
    ##################

    P3_Var1 = float(request.POST["P3_Var1"])
    P3_Var2 = float(request.POST["P3_Var2"])
    P3_Var3 = float(request.POST["P3_Var3"])
    P3_Impurities = float(request.POST["P3_Impurities"])
    P3_Mass = float(request.POST["P3_Mass"])
    P3_Wax1 = float(request.POST["P3_Wax1"])

   
    P3_Mass = P3_Var1+(P3_Var2*30/10000)+P3_Var3+P3_Impurities

    ##################

    P4_Var1 = float(request.POST["P4_Var1"])
    P4_Var2 = float(request.POST["P4_Var2"])
    P4_Var3 = float(request.POST["P4_Var3"])
    P4_Impurities = float(request.POST["P4_Impurities"])
    P4_Mass = float(request.POST["P4_Mass"])
    P4_Wax1 = float(request.POST["P4_Wax1"])

    
    P4_Mass = P4_Var1+(P4_Var2*30/10000)+P4_Var3+P4_Impurities

    
    ##################

    P5_Var1 = float(request.POST["P5_Var1"])
    P5_Var2 = float(request.POST["P5_Var2"])
    P5_Var3 = float(request.POST["P5_Var3"])
    P5_Impurities = float(request.POST["P5_Impurities"])
    P5_Mass = float(request.POST["P5_Mass"])
    P5_Wax1 = float(request.POST["P5_Wax1"])

    
    P5_Mass = P5_Var1+(P5_Var2*30/10000)+P5_Var3+P5_Impurities

    
    ##################

    P6_Var1 = float(request.POST["P6_Var1"])
    P6_Var2 = float(request.POST["P6_Var2"])
    P6_Var3 = float(request.POST["P6_Var3"])
    P6_Impurities = float(request.POST["P6_Impurities"])
    P6_Mass = float(request.POST["P6_Mass"])
    P6_Wax1 = float(request.POST["P6_Wax1"])

    
    P6_Mass = P6_Var1+(P6_Var2*30/10000)+P6_Var3+P6_Impurities

    
    ##################
    
    P7_Var1 = float(request.POST["P7_Var1"])
    P7_Var2 = float(request.POST["P7_Var2"])
    P7_Var3 = float(request.POST["P7_Var3"])
    P7_Impurities = float(request.POST["P7_Impurities"])

    

    #################################################################################################
    # Function for GoalSeek

    def GoalSeek(fun, goal, x0, fTol=0.0001, MaxIter=1000):
        # Initial check
        if fun(x0) == goal:
            print('Exact solution found')
            return x0

        # Line Search Method
        step_sizes = np.logspace(-1, 4, 6)
        scopes = np.logspace(1, 5, 5)

        vFun = np.vectorize(fun)

        for scope in scopes:
            break_nested = False
            for step_size in step_sizes:

                cApos = np.linspace(x0, x0+step_size*scope, int(scope))
                cAneg = np.linspace(x0, x0-step_size*scope, int(scope))

                cA = np.concatenate((cAneg[::-1], cApos[1:]), axis=0)

                fA = vFun(cA)-goal

                if np.any(np.diff(np.sign(fA))):

                    index_lb = np.nonzero(np.diff(np.sign(fA)))

                    if len(index_lb[0]) == 1:

                        index_ub = index_lb+np.array([1])

                        x_lb = np.asscalar(np.array(cA)[index_lb][0])
                        x_ub = np.asscalar(np.array(cA)[index_ub][0])
                        break_nested = True
                        break
                    else:  # Two or more roots possible

                        index_ub = index_lb+np.array([1])

                        print('Other solution possible at around, x0 = ',
                              np.array(cA)[index_lb[0][1]])

                        x_lb = np.asscalar(np.array(cA)[index_lb[0][0]])
                        x_ub = np.asscalar(np.array(cA)[index_ub[0][0]])
                        break_nested = True
                        break

            if break_nested:
                break
        if not x_lb or not x_ub:
            print('No Solution Found')
            return

        # Bisection Method
        iter_num = 0
        error = 10

        while iter_num < MaxIter and fTol < error:

            x_m = (x_lb+x_ub)/2
            f_m = fun(x_m)-goal

            error = abs(f_m)

            if (fun(x_lb)-goal)*(f_m) < 0:
                x_ub = x_m
            elif (fun(x_ub)-goal)*(f_m) < 0:
                x_lb = x_m
            elif f_m == 0:
                print('Exact solution found')
                return x_m
            else:
                print('Failure in Bisection Method')

            iter_num += 1

        return x_m
    ################################################################################



    #################################################################################################
    def fun(P2_Iter):
            P1_calc1 = ((P1_Var2*30/10000*P1_FlowPercent) -
                        (P2_Var2*30/10000*P2_Iter))*(10000/(30*P1_FlowPercent))
            P1_calc1withfactor = P1_calc1*30/10000
            P1_calc2 = (P1_Impurities*P1_FlowPercent -
                        P2_Impurities*P2_Iter)/P1_FlowPercent
            P1_Loss1 = (((P1_calc1withfactor+P1_calc2) /
                         ((100-P1_Ass1)/100))-(P1_calc1withfactor+P1_calc2))
            P1_Loss1withfactor = P1_Loss1 + \
                ((P1_Ass3*P1_Ass2)/(P1_Ass4*1000)*100)
            P1_calc3 = (P1_Var3*P1_FlowPercent -
                        P2_Var3*P2_Iter)/P1_FlowPercent
            P1_calc4 = (P1_Wax1-P2_Wax1)*100/1000000
            P1_calc5 = P1_Loss1withfactor+P1_calc2+P1_calc1withfactor+P1_calc3+P1_calc4
            P2_FlowPercent = P1_FlowPercent-P1_calc5
            return P2_Iter-P2_FlowPercent

    # (ii)  Define the goal (result)
    goal = 0

    # (iii) Define a starting point
    x0 = 100

    P2_Iter = GoalSeek(fun, goal, x0)
    
    P1_calc1 = ((P1_Var2*30/10000*P1_FlowPercent) -
                (P2_Var2*30/10000*P2_Iter))*(10000/(30*P1_FlowPercent))
    P1_calc1withfactor = P1_calc1*30/10000
    P1_calc2 = (P1_Impurities*P1_FlowPercent -
                P2_Impurities*P2_Iter)/P1_FlowPercent
    P1_Loss1 = (((P1_calc1withfactor+P1_calc2) /
                 ((100-P1_Ass1)/100))-(P1_calc1withfactor+P1_calc2))
    P1_Loss1withfactor = P1_Loss1 + \
        ((P1_Ass3*P1_Ass2)/(P1_Ass4*1000)*100)
    P1_calc3 = (P1_Var3*P1_FlowPercent-P2_Var3*P2_Iter)/P1_FlowPercent
    P1_calc4 = (P1_Wax1-P2_Wax1)*100/1000000
    P1_calc5 = P1_Loss1withfactor+P1_calc2+P1_calc1withfactor+P1_calc3+P1_calc4
    P2_FlowPercent = P1_FlowPercent-P1_calc5
    


    #################################################################################################

    def fun2(P3_Iter):
            P2_calc1 = ((P2_Var2*30/10000*P2_FlowPercent) -
                        (P3_Var2*30/10000*P3_Iter))*(10000/(30*P1_FlowPercent))
            P2_calc1withfactor = P2_calc1*30/10000
            P2_Loss1 = ((P2_FlowPercent*P2_Var1) -
                        (P3_Iter*P2_Var1))/P1_FlowPercent
            P2_calc3 = (P2_Impurities*P2_FlowPercent -
                        P3_Impurities*P3_Iter)/P1_FlowPercent
            P2_Loss1withfactor = (((P2_Loss1+P2_calc1withfactor+P2_calc3)/(
                (100-P2_Ass1)/100))-(P2_calc1withfactor+P2_calc3+P2_Loss1))
            P2_calc2 = P2_Loss1withfactor + \
                ((P2_Ass3*P2_Ass2)/(P1_Ass4*1000)*100)
            P2_calc4 = ((P2_Var3*P2_FlowPercent -
                         P3_Var3*P3_Iter))/P1_FlowPercent
            P2_calc5 = P2_Loss1+P2_calc2+P2_calc3+P2_calc1withfactor+P2_calc4
            P3_FlowPercent = P2_FlowPercent-P2_calc5
            return P3_Iter-P3_FlowPercent

    # (ii)  Define the goal (result)
    goal = 0

    # (iii) Define a starting point
    x0 = 100

    P3_Iter = GoalSeek(fun2, goal, x0)
    
    P2_calc1 = ((P2_Var2*30/10000*P2_FlowPercent) -
                (P3_Var2*30/10000*P3_Iter))*(10000/(30*P1_FlowPercent))
    P2_calc1withfactor = P2_calc1*30/10000
    P2_Loss1 = ((P2_FlowPercent*P2_Var1) -
                (P3_Iter*P2_Var1))/P1_FlowPercent
    P2_calc3 = (P2_Impurities*P2_FlowPercent -
                P3_Impurities*P3_Iter)/P1_FlowPercent
    P2_Loss1withfactor = (((P2_Loss1+P2_calc1withfactor+P2_calc3) /
                           ((100-P2_Ass1)/100))-(P2_calc1withfactor+P2_calc3+P2_Loss1))
    P2_calc2 = P2_Loss1withfactor + \
        ((P2_Ass3*P2_Ass2)/(P1_Ass4*1000)*100)
    P2_calc4 = ((P2_Var3*P2_FlowPercent-P3_Var3*P3_Iter)) / \
        P1_FlowPercent
    P2_calc5 = P2_Loss1+P2_calc2+P2_calc3+P2_calc1withfactor+P2_calc4
    P3_FlowPercent = P2_FlowPercent-P2_calc5
    


    #################################################################################################

    def fun3(P4_Iter):
            P3_calc1 = ((P3_Var2*30/10000*P3_FlowPercent) -
                        (P4_Var2*30/10000*P4_Iter))*(10000/(30*P1_FlowPercent))
            P3_calc1withfactor = P3_calc1*30/10000
            P3_Loss1 = ((P3_FlowPercent*P3_Var1) -
                        (P4_Iter*P4_Var1))/(P1_FlowPercent)
            P3_Loss1withfactor = P3_Ass1
            P3_calc2 = ((P3_Impurities*P3_FlowPercent-P4_Impurities*P4_Iter) /
                        P1_FlowPercent)+((P3_Var3*P3_FlowPercent-P4_Var3*P4_Iter)/P1_FlowPercent)
            P3_calc5 = P3_calc1withfactor+P3_Loss1+P3_Loss1withfactor+P3_calc2
            P4_FlowPercent = P3_Iter-P3_calc5
            return P4_Iter-P4_FlowPercent

    # (ii)  Define the goal (result)
    goal = 0

    # (iii) Define a starting point
    x0 = 100

    P4_Iter = GoalSeek(fun3, goal, x0)
    

    P3_calc1 = ((P3_Var2*30/10000*P3_FlowPercent) -
                (P4_Var2*30/10000*P4_Iter))*(10000/(30*P1_FlowPercent))
    P3_calc1withfactor = P3_calc1*30/10000
    P3_Loss1 = ((P3_FlowPercent*P3_Var1) -
                (P4_Iter*P4_Var1))/(P1_FlowPercent)
    P3_Loss1withfactor = P3_Ass1
    P3_calc2 = ((P3_Impurities*P3_FlowPercent-P4_Impurities*P4_Iter) /
                P1_FlowPercent)+((P3_Var3*P3_FlowPercent-P4_Var3*P4_Iter)/P1_FlowPercent)
    P3_calc5 = P3_calc1withfactor+P3_Loss1+P3_Loss1withfactor+P3_calc2
    P4_FlowPercent = P3_Iter-P3_calc5
    

    #################################################################################################

    def fun4(P5_Iter):
            P4_calc1 = ((P4_Var2*30/10000*P4_FlowPercent) -
                        (P5_Var2*30/10000*P5_Iter))*(10000/(30*P1_FlowPercent))
            P4_calc1withfactor = P4_calc1*30/10000
            P4_Loss1 = ((P4_Ass3*((100-P4_Ass2)/100))/10 *
                        (P4_Ass1/(100-P4_Ass1)))*(P4_FlowPercent/P1_FlowPercent)
            P4_Loss1withfactor = (
                P4_Var1*P4_FlowPercent-P5_Var1*P5_Iter)/(P1_FlowPercent)
            P4_calc2 = ((P4_Impurities*P4_FlowPercent-P5_Impurities*P5_Iter) /
                        P1_FlowPercent)+((P4_Var3*P4_FlowPercent-P5_Var3*P5_Iter)/P1_FlowPercent)
            P4_calc4 = (P4_Wax1-P5_Wax1)*100/1000000
            P4_calc5 = P4_calc1withfactor+P4_Loss1+P4_Loss1withfactor+P4_calc2+P4_calc4
            P5_FlowPercent = P4_Iter-P4_calc5
            return P5_Iter-P5_FlowPercent

    # (ii)  Define the goal (result)
    goal = 0

    # (iii) Define a starting point
    x0 = 100

    P5_Iter = GoalSeek(fun4, goal, x0)
    

    P4_calc1 = ((P4_Var2*30/10000*P4_FlowPercent) -
                (P5_Var2*30/10000*P5_Iter))*(10000/(30*P1_FlowPercent))
    P4_calc1withfactor = P4_calc1*30/10000
    P4_Loss1 = ((P4_Ass3*((100-P4_Ass2)/100))/10 *
                (P4_Ass1/(100-P4_Ass1)))*(P4_FlowPercent/P1_FlowPercent)
    P4_Loss1withfactor = (P4_Var1*P4_FlowPercent -
                          P5_Var1*P5_Iter)/(P1_FlowPercent)
    P4_calc2 = ((P4_Impurities*P4_FlowPercent-P5_Impurities*P5_Iter) /
                P1_FlowPercent)+((P4_Var3*P4_FlowPercent-P5_Var3*P5_Iter)/P1_FlowPercent)
    P4_calc4 = (P4_Wax1-P5_Wax1)*100/1000000
    P4_calc5 = P4_calc1withfactor+P4_Loss1+P4_Loss1withfactor+P4_calc2+P4_calc4
    P5_FlowPercent = P4_Iter-P4_calc5
    

    #################################################################################################

    def fun5(P6_Iter):
            P5_calc1 = ((P5_Var2*30/10000*P5_FlowPercent) -
                        (P6_Var2*30/10000*P6_Iter))*(10000/(30*P1_FlowPercent))
            P5_calc1withfactor = P5_calc1*30/10000
            P5_Loss1 = ((P5_Ass3*((100-P5_Ass2)/100))/10 *
                        (P5_Ass1/(100-P5_Ass1)))*(P5_FlowPercent/P1_FlowPercent)
            P5_Loss1withfactor = (
                P5_Var1*P5_FlowPercent-P6_Var1*P6_Iter)/(P1_FlowPercent)
            P5_calc2 = ((P5_Impurities*P5_FlowPercent-P6_Impurities*P6_Iter) /
                        P1_FlowPercent)+((P5_Var3*P5_FlowPercent-P6_Var3*P6_Iter)/P1_FlowPercent)
            P5_calc4 = (P5_Wax1-P6_Wax1)*100/1000000
            P5_calc5 = P5_calc1withfactor+P5_Loss1+P5_Loss1withfactor+P5_calc2+P5_calc4
            P6_FlowPercent = P5_Iter-P5_calc5
            return P6_Iter-P6_FlowPercent

    # (ii)  Define the goal (result)
    goal = 0

    # (iii) Define a starting point
    x0 = 100

    P6_Iter = GoalSeek(fun5, goal, x0)
    
    P5_calc1 = ((P5_Var2*30/10000*P5_FlowPercent) -
                (P6_Var2*30/10000*P6_Iter))*(10000/(30*P1_FlowPercent))
    P5_calc1withfactor = P5_calc1*30/10000
    P5_Loss1 = ((P5_Ass3*((100-P5_Ass2)/100))/10 *
                (P5_Ass1/(100-P5_Ass1)))*(P5_FlowPercent/P1_FlowPercent)
    P5_Loss1withfactor = (P5_Var1*P5_FlowPercent -
                          P6_Var1*P6_Iter)/(P1_FlowPercent)
    P5_calc2 = ((P5_Impurities*P5_FlowPercent-P6_Impurities*P6_Iter) /
                P1_FlowPercent)+((P5_Var3*P5_FlowPercent-P6_Var3*P6_Iter)/P1_FlowPercent)
    P5_calc4 = (P5_Wax1-P6_Wax1)*100/1000000
    P5_calc5 = P5_calc1withfactor+P5_Loss1+P5_Loss1withfactor+P5_calc2+P5_calc4
    P6_FlowPercent = P5_Iter-P5_calc5
    


    #################################################################################################

    def fun6(P7_Iter):
            P6_calc1 = ((P6_Var2*30/10000*P6_FlowPercent) -
                        (P7_Var2*30/10000*P7_Iter))*(10000/(30*P1_FlowPercent))
            P6_calc1withfactor = P6_calc1*30/10000
            P6_Loss1 = (((P6_Var1*P6_FlowPercent-P7_Var1*P7_Iter) /
                         P6_FlowPercent)*P6_Ass1/100)*(P6_FlowPercent/P1_FlowPercent)
            P6_Loss1withfactor = (
                P6_Var1*P6_FlowPercent-P7_Var1*P7_Iter)/(P5_FlowPercent)
            P6_calc2 = ((P6_Var3*P6_FlowPercent-P7_Var3*P7_Iter)/P1_FlowPercent) + \
                ((P6_Impurities*P6_FlowPercent-P7_Impurities*P7_Iter)/P1_FlowPercent)
            P6_calc5 = P6_calc1withfactor+P6_Loss1+P6_Loss1withfactor+P6_calc2
            P7_FlowPercent = P6_Iter-P6_calc5
            return P7_Iter-P7_FlowPercent
    # (ii)  Define the goal (result)
    goal = 0

    # (iii) Define a starting point
    x0 = 100

    P7_Iter = GoalSeek(fun6, goal, x0)
    

    P6_calc1 = ((P6_Var2*30/10000*P6_FlowPercent) -
                (P7_Var2*30/10000*P7_Iter))*(10000/(30*P1_FlowPercent))
    P6_calc1withfactor = P6_calc1*30/10000
    P6_Loss1 = (((P6_Var1*P6_FlowPercent-P7_Var1*P7_Iter) /
                 P6_FlowPercent)*P6_Ass1/100)*(P6_FlowPercent/P1_FlowPercent)
    P6_Loss1withfactor = (P6_Var1*P6_FlowPercent -
                          P7_Var1*P7_Iter)/(P5_FlowPercent)
    P6_calc2 = ((P6_Var3*P6_FlowPercent-P7_Var3*P7_Iter)/P1_FlowPercent) + \
        ((P6_Impurities*P6_FlowPercent-P7_Impurities*P7_Iter)/P1_FlowPercent)
    P6_calc5 = P6_calc1withfactor+P6_Loss1+P6_Loss1withfactor+P6_calc2
    P7_FlowPercent = P6_Iter-P6_calc5
    

    #####################################################
    # OYA TABLE
    TUCMASS = P1_Mass
    YIELD = P7_FlowPercent-CTS_Losses-WW-UEXLOS
    FLOWLOSS = 100-YIELD
    TUCFACT = (100-YIELD)/TUCMASS


    #################################################################################################
    # Actual OMB A=V/Yr  B=VALUE   C=%   D=VALUE    E=FS   Table Data Calc
    B_FLOWOP = YIELD
    A_OInput = Flowrate
    A_OLCT = (CTS_Losses*Flowrate)/100
    A_SDGG = (P1_calc5-P1_calc2-P1_calc3)/100*Flowrate
    A_AO = (P2_calc5-P2_calc3-P2_calc4+P3_calc5 -
            P3_calc5-P3_calc2)/100*Flowrate

    A_OIC = (P4_calc5-P4_calc2)/100*Flowrate
    A_OIWFA = (P5_calc5-P5_calc2)/100*Flowrate
    A_PMI = (P1_Var3+P1_Impurities-P7_Var3-P7_Impurities)*Flowrate/100
    A_D = (P6_calc5-P6_calc2)/100*Flowrate
    A_WW = WW*Flowrate/100
    A_UEXLOS = UEXLOS*Flowrate/100
    A_FLOWOP = B_FLOWOP/100*Flowrate
    A_TOTAL = A_OLCT+A_SDGG+A_AO+A_OIC+A_OIWFA+A_PMI+A_D+A_WW+A_UEXLOS+A_FLOWOP
    
    B_OLCT = A_OLCT/A_OInput*100
    B_SDGG = A_SDGG/A_OInput*100
    B_AO = A_AO/A_OInput*100
    B_OIC = A_OIC/A_OInput*100
    B_OIWFA = A_OIWFA/A_OInput*100
    B_PMI = A_PMI/A_OInput*100
    B_D = A_D/A_OInput*100
    B_WW = A_WW/A_OInput*100
    B_UEXLOS = A_UEXLOS/A_OInput*100
    B_FLOWOP = YIELD
    B_TOTAL = B_OLCT+B_SDGG+B_AO+B_OIC+B_OIWFA+B_PMI+B_D+B_WW+B_UEXLOS+B_FLOWOP
    
    C_OLCT = A_OLCT*CTF/1000
    C_SDGG = A_SDGG*GSBC/1000
    C_AO = A_AO*AO/1000
    C_OIC = A_OIC*GSBC/1000
    C_OIWFA = A_OIWFA*WFA/1000
    C_PMI = A_PMI*0/1000
    C_D = A_D*PRD/1000
    C_WW = A_WW*0/1000
    C_UEXLOS = A_UEXLOS*0/1000
    C_FLOWOP = A_FLOWOP*RO/1000
    C_TOTAL = C_AO+C_OIC+C_OIWFA+C_PMI+C_D+C_WW+C_UEXLOS+C_FLOWOP
    
    D_OLCT = (B_OLCT*CO/100)-(C_OLCT*1000/Flowrate)
    D_SDGG = (B_SDGG*CO/100)-(C_SDGG*1000/Flowrate)
    D_AO = (B_AO*CO/100)-(C_AO*1000/Flowrate)
    D_OIC = (B_OIC*CO/100)-(C_OIC*1000/Flowrate)
    D_OIWFA = (B_OIWFA*CO/100)-(C_OIWFA*1000/Flowrate)
    D_PMI = (B_PMI*CO/100)-(C_PMI*1000/Flowrate)
    D_D = (B_D*CO/100)-(C_D*1000/Flowrate)
    D_WW = (B_WW*CO/100)-(C_WW*1000/Flowrate)
    D_UEXLOS = (B_UEXLOS*CO/100)-(C_UEXLOS*1000/Flowrate)
    D_TOTAL = D_OLCT+D_SDGG+D_AO+D_OIC+D_OIWFA+D_PMI+D_D+D_WW+D_UEXLOS
    
    FS = D_TOTAL
    


    #################################################################################################
    # Theorotical Calculation

    def func(P2_TheIter):
            P1_Thecalc1 = ((P1_Var2*30/10000*P1_FlowPercent) -
                           (P2_Var2*30/10000*P2_TheIter))*(10000/(30*P1_FlowPercent))
            P1_Thecalc1withfactor = P1_Thecalc1*30/10000
            P1_Thecalc2 = (P1_Impurities*P1_FlowPercent -
                           P2_Impurities*P2_TheIter)/P1_FlowPercent
            P1_TheLoss1 = (((P1_Thecalc1withfactor+P1_Thecalc2) /
                            ((100-P1_TheAss1)/100))-(P1_Thecalc1withfactor+P1_Thecalc2))
            P1_TheLoss1withfactor = P1_TheLoss1 + \
                ((P1_TheAss3*P1_TheAss2)/(P1_TheAss4*1000)*100)
            P1_Thecalc3 = (P1_Var3*P1_FlowPercent-P2_Var3 *
                           P2_TheIter)/P1_FlowPercent
            P1_Thecalc4 = (P1_Wax1-P2_Wax1)*100/1000000
            P1_Thecalc5 = P1_TheLoss1withfactor+P1_Thecalc2 + \
                P1_Thecalc1withfactor+P1_Thecalc3+P1_Thecalc4
            P2_TheFlowPercent = P1_FlowPercent-P1_Thecalc5
            return P2_TheIter-P2_TheFlowPercent

    # (ii)  Define the goal (result)
    goal = 0

    # (iii) Define a starting point
    x0 = 100

    P2_TheIter = GoalSeek(func, goal, x0)
    

    P1_Thecalc1 = ((P1_Var2*30/10000*P1_FlowPercent) -
                   (P2_Var2*30/10000*P2_TheIter))*(10000/(30*P1_FlowPercent))
    P1_Thecalc1withfactor = P1_Thecalc1*30/10000
    P1_Thecalc2 = (P1_Impurities*P1_FlowPercent -
                   P2_Impurities*P2_TheIter)/P1_FlowPercent
    P1_TheLoss1 = (((P1_Thecalc1withfactor+P1_Thecalc2) /
                    ((100-P1_TheAss1)/100))-(P1_Thecalc1withfactor+P1_Thecalc2))
    P1_TheLoss1withfactor = P1_TheLoss1 + \
        ((P1_TheAss3*P1_TheAss2)/(P1_TheAss4*1000)*100)
    P1_Thecalc3 = (P1_Var3*P1_FlowPercent-P2_Var3 *
                   P2_TheIter)/P1_FlowPercent
    P1_Thecalc4 = (P1_Wax1-P2_Wax1)*100/1000000
    P1_Thecalc5 = P1_TheLoss1withfactor+P1_Thecalc2 + \
        P1_Thecalc1withfactor+P1_Thecalc3+P1_Thecalc4
    P2_TheFlowPercent = P1_FlowPercent-P1_Thecalc5
    

    #################################################################################################

    def func2(P3_TheIter):
            P2_Thecalc1 = ((P2_Var2*30/10000*P2_TheFlowPercent) -
                           (P3_Var2*30/10000*P3_TheIter))*(10000/(30*P1_FlowPercent))
            P2_Thecalc1withfactor = P2_Thecalc1*30/10000
            P2_TheLoss1 = ((P2_TheFlowPercent*P2_Var1) -
                           (P3_TheIter*P2_Var1))/P1_FlowPercent
            P2_Thecalc3 = (P2_Impurities*P2_TheFlowPercent -
                           P3_Impurities*P3_TheIter)/P1_FlowPercent
            P2_TheLoss1withfactor = (((P2_TheLoss1+P2_Thecalc1withfactor+P2_Thecalc3)/(
                (100-P2_TheAss1)/100))-(P2_Thecalc1withfactor+P2_Thecalc3+P2_TheLoss1))
            P2_Thecalc2 = P2_TheLoss1withfactor + \
                ((P2_TheAss3*P2_TheAss2)/(P1_TheAss4*1000)*100)
            P2_Thecalc4 = ((P2_Var3*P2_TheFlowPercent -
                            P3_Var3*P3_TheIter))/P1_FlowPercent
            P2_Thecalc5 = P2_TheLoss1+P2_Thecalc2 + \
                P2_Thecalc3+P2_Thecalc1withfactor+P2_Thecalc4
            P3_TheFlowPercent = P2_TheFlowPercent-P2_Thecalc5
            return P3_TheIter-P3_TheFlowPercent

    # (ii)  Define the goal (result)
    goal = 0

    # (iii) Define a starting point
    x0 = 100

    P3_TheIter = GoalSeek(func2, goal, x0)
    
    P2_Thecalc1 = ((P2_Var2*30/10000*P2_TheFlowPercent) -
                   (P3_Var2*30/10000*P3_TheIter))*(10000/(30*P1_FlowPercent))
    P2_Thecalc1withfactor = P2_Thecalc1*30/10000
    P2_TheLoss1 = ((P2_TheFlowPercent*P2_Var1) -
                   (P3_TheIter*P2_Var1))/P1_FlowPercent
    P2_Thecalc3 = (P2_Impurities*P2_TheFlowPercent -
                   P3_Impurities*P3_TheIter)/P1_FlowPercent
    P2_TheLoss1withfactor = (((P2_TheLoss1+P2_Thecalc1withfactor+P2_Thecalc3)/(
        (100-P2_TheAss1)/100))-(P2_Thecalc1withfactor+P2_Thecalc3+P2_TheLoss1))
    P2_Thecalc2 = P2_TheLoss1withfactor + \
        ((P2_TheAss3*P2_TheAss2)/(P1_TheAss4*1000)*100)
    P2_Thecalc4 = ((P2_Var3*P2_TheFlowPercent -
                    P3_Var3*P3_TheIter))/P1_FlowPercent
    P2_Thecalc5 = P2_TheLoss1+P2_Thecalc2 + \
        P2_Thecalc3+P2_Thecalc1withfactor+P2_Thecalc4
    P3_TheFlowPercent = P2_TheFlowPercent-P2_Thecalc5
    


    #################################################################################################

    def func3(P4_TheIter):
            P3_Thecalc1 = ((P3_Var2*30/10000*P3_TheFlowPercent) -
                           (P4_Var2*30/10000*P4_TheIter))*(10000/(30*P1_FlowPercent))
            P3_Thecalc1withfactor = P3_Thecalc1*30/10000
            P3_TheLoss1 = ((P3_TheFlowPercent*P3_Var1) -
                           (P4_TheIter*P4_Var1))/(P1_FlowPercent)
            P3_TheLoss1withfactor = P3_TheAss1
            P3_Thecalc2 = ((P3_Impurities*P3_TheFlowPercent-P4_Impurities*P4_TheIter) /
                           P1_FlowPercent)+((P3_Var3*P3_TheFlowPercent-P4_Var3*P4_TheIter)/P1_FlowPercent)
            P3_Thecalc5 = P3_Thecalc1withfactor+P3_TheLoss1+P3_TheLoss1withfactor+P3_Thecalc2
            P4_TheFlowPercent = P3_TheIter-P3_Thecalc5
            return P4_TheIter-P4_TheFlowPercent

    # (ii)  Define the goal (result)
    goal = 0

    # (iii) Define a starting point
    x0 = 100

    P4_TheIter = GoalSeek(func3, goal, x0)
    
    P3_Thecalc1 = ((P3_Var2*30/10000*P3_TheFlowPercent) -
                   (P4_Var2*30/10000*P4_TheIter))*(10000/(30*P1_FlowPercent))
    P3_Thecalc1withfactor = P3_Thecalc1*30/10000
    P3_TheLoss1 = ((P3_TheFlowPercent*P3_Var1) -
                   (P4_TheIter*P4_Var1))/(P1_FlowPercent)
    P3_TheLoss1withfactor = P3_TheAss1
    P3_Thecalc2 = ((P3_Impurities*P3_TheFlowPercent-P4_Impurities*P4_TheIter) /
                   P1_FlowPercent)+((P3_Var3*P3_TheFlowPercent-P4_Var3*P4_TheIter)/P1_FlowPercent)
    P3_Thecalc5 = P3_Thecalc1withfactor+P3_TheLoss1+P3_TheLoss1withfactor+P3_Thecalc2
    P4_TheFlowPercent = P3_TheIter-P3_Thecalc5
    


    #################################################################################################

    def func4(P5_TheIter):
            P4_Thecalc1 = ((P4_Var2*30/10000*P4_TheFlowPercent) -
                           (P5_Var2*30/10000*P5_TheIter))*(10000/(30*P1_FlowPercent))
            P4_Thecalc1withfactor = P4_Thecalc1*30/10000
            P4_TheLoss1 = ((P4_TheAss3*((100-P4_TheAss2)/100))/10 *
                           (P4_TheAss1/(100-P4_TheAss1)))*(P4_TheFlowPercent/P1_FlowPercent)
            P4_TheLoss1withfactor = (
                P4_Var1*P4_TheFlowPercent-P5_Var1*P5_TheIter)/(P1_FlowPercent)
            P4_Thecalc2 = ((P4_Impurities*P4_TheFlowPercent-P5_Impurities*P5_TheIter) /
                           P1_FlowPercent)+((P4_Var3*P4_TheFlowPercent-P5_Var3*P5_TheIter)/P1_FlowPercent)
            P4_Thecalc4 = (P4_Wax1-P5_Wax1)*100/1000000
            P4_Thecalc5 = P4_Thecalc1withfactor+P4_TheLoss1 + \
                P4_TheLoss1withfactor+P4_Thecalc2+P4_Thecalc4
            P5_TheFlowPercent = P4_TheIter-P4_Thecalc5
            return P5_TheIter-P5_TheFlowPercent

    # (ii)  Define the goal (result)
    goal = 0

    # (iii) Define a starting point
    x0 = 100

    P5_TheIter = GoalSeek(func4, goal, x0)
    

    P4_Thecalc1 = ((P4_Var2*30/10000*P4_TheFlowPercent) -
                   (P5_Var2*30/10000*P5_TheIter))*(10000/(30*P1_FlowPercent))
    P4_Thecalc1withfactor = P4_Thecalc1*30/10000
    P4_TheLoss1 = ((P4_TheAss3*((100-P4_TheAss2)/100))/10 *
                   (P4_TheAss1/(100-P4_TheAss1)))*(P4_TheFlowPercent/P1_FlowPercent)
    P4_TheLoss1withfactor = (
        P4_Var1*P4_TheFlowPercent-P5_Var1*P5_TheIter)/(P1_FlowPercent)
    P4_Thecalc2 = ((P4_Impurities*P4_TheFlowPercent-P5_Impurities*P5_TheIter) /
                   P1_FlowPercent)+((P4_Var3*P4_TheFlowPercent-P5_Var3*P5_TheIter)/P1_FlowPercent)
    P4_Thecalc4 = (P4_Wax1-P5_Wax1)*100/1000000
    P4_Thecalc5 = P4_Thecalc1withfactor+P4_TheLoss1 + \
        P4_TheLoss1withfactor+P4_Thecalc2+P4_Thecalc4
    P5_TheFlowPercent = P4_TheIter-P4_Thecalc5
    

    #################################################################################################

    def func5(P6_TheIter):
            P5_Thecalc1 = ((P5_Var2*30/10000*P5_TheFlowPercent) -
                           (P6_Var2*30/10000*P6_TheIter))*(10000/(30*P1_FlowPercent))
            P5_Thecalc1withfactor = P5_Thecalc1*30/10000
            P5_TheLoss1 = ((P5_TheAss3*((100-P5_TheAss2)/100))/10 *
                           (P5_TheAss1/(100-P5_TheAss1)))*(P5_TheFlowPercent/P1_FlowPercent)
            P5_TheLoss1withfactor = (
                P5_Var1*P5_TheFlowPercent-P6_Var1*P6_TheIter)/(P1_FlowPercent)
            P5_Thecalc2 = ((P5_Impurities*P5_TheFlowPercent-P6_Impurities*P6_TheIter) /
                           P1_FlowPercent)+((P5_Var3*P5_TheFlowPercent-P6_Var3*P6_TheIter)/P1_FlowPercent)
            P5_Thecalc4 = (P5_Wax1-P6_Wax1)*100/1000000
            P5_Thecalc5 = P5_Thecalc1withfactor+P5_TheLoss1 + \
                P5_TheLoss1withfactor+P5_Thecalc2+P5_Thecalc4
            P6_TheFlowPercent = P5_TheIter-P5_Thecalc5
            return P6_TheIter-P6_TheFlowPercent

    # (ii)  Define the goal (result)
    goal = 0

    # (iii) Define a starting point
    x0 = 100

    P6_TheIter = GoalSeek(func5, goal, x0)
    
    P5_Thecalc1 = ((P5_Var2*30/10000*P5_TheFlowPercent) -
                   (P6_Var2*30/10000*P6_TheIter))*(10000/(30*P1_FlowPercent))
    P5_Thecalc1withfactor = P5_Thecalc1*30/10000
    P5_TheLoss1 = ((P5_TheAss3*((100-P5_TheAss2)/100))/10 *
                   (P5_TheAss1/(100-P5_TheAss1)))*(P5_TheFlowPercent/P1_FlowPercent)
    P5_TheLoss1withfactor = (
        P5_Var1*P5_TheFlowPercent-P6_Var1*P6_TheIter)/(P1_FlowPercent)
    P5_Thecalc2 = ((P5_Impurities*P5_TheFlowPercent-P6_Impurities*P6_TheIter) /
                   P1_FlowPercent)+((P5_Var3*P5_TheFlowPercent-P6_Var3*P6_TheIter)/P1_FlowPercent)
    P5_Thecalc4 = (P5_Wax1-P6_Wax1)*100/1000000
    P5_Thecalc5 = P5_Thecalc1withfactor+P5_TheLoss1 + \
        P5_TheLoss1withfactor+P5_Thecalc2+P5_Thecalc4
    P6_TheFlowPercent = P5_TheIter-P5_Thecalc5
    


    #################################################################################################

    def func6(P7_TheIter):
            P6_Thecalc1 = ((P6_Var2*30/10000*P6_TheFlowPercent) -
                           (P7_Var2*30/10000*P7_TheIter))*(10000/(30*P1_FlowPercent))
            P6_Thecalc1withfactor = P6_Thecalc1*30/10000
            P6_TheLoss1 = (((P6_Var1*P6_TheFlowPercent-P7_Var1*P7_TheIter) /
                            P6_TheFlowPercent)*P6_TheAss1/100)*(P6_TheFlowPercent/P1_FlowPercent)
            P6_TheLoss1withfactor = (
                P6_Var1*P6_TheFlowPercent-P7_Var1*P7_TheIter)/(P5_TheFlowPercent)
            P6_Thecalc2 = ((P6_Var3*P6_TheFlowPercent-P7_Var3*P7_TheIter)/P1_FlowPercent)+(
                (P6_Impurities*P6_TheFlowPercent-P7_Impurities*P7_TheIter)/P1_FlowPercent)
            P6_Thecalc5 = P6_Thecalc1withfactor+P6_TheLoss1+P6_TheLoss1withfactor+P6_Thecalc2
            P7_TheFlowPercent = P6_TheIter-P6_Thecalc5
            return P7_TheIter-P7_TheFlowPercent

    # (ii)  Define the goal (result)
    goal = 0

    # (iii) Define a starting point
    x0 = 100

    P7_TheIter = GoalSeek(func6, goal, x0)
    

    P6_Thecalc1 = ((P6_Var2*30/10000*P6_TheFlowPercent) -
                   (P7_Var2*30/10000*P7_TheIter))*(10000/(30*P1_FlowPercent))
    P6_Thecalc1withfactor = P6_Thecalc1*30/10000
    P6_TheLoss1 = (((P6_Var1*P6_TheFlowPercent-P7_Var1*P7_TheIter) /
                    P6_TheFlowPercent)*P6_TheAss1/100)*(P6_TheFlowPercent/P1_FlowPercent)
    P6_TheLoss1withfactor = (
        P6_Var1*P6_TheFlowPercent-P7_Var1*P7_TheIter)/(P5_TheFlowPercent)
    P6_Thecalc2 = ((P6_Var3*P6_TheFlowPercent-P7_Var3*P7_TheIter)/P1_FlowPercent)+(
        (P6_Impurities*P6_TheFlowPercent-P7_Impurities*P7_TheIter)/P1_FlowPercent)
    P6_Thecalc5 = P6_Thecalc1withfactor+P6_TheLoss1+P6_TheLoss1withfactor+P6_Thecalc2
    P7_TheFlowPercent = P6_TheIter-P6_Thecalc5
    

    #################################################################################################
    # OYA TABLE
    TheTUCMASS = P1_Mass
    TheYIELD = P7_TheFlowPercent-TheCTS_Losses-TheWW-TheUEXLOS
    TheFLOWLOSS = 100-TheYIELD
    TheTUCFACT = (100-TheYIELD)/TheTUCMASS


    #################################################################################################
    # Theorotical OMB A=V/Yr  B=VALUE   C=%   D=VALUE    E=FS   Table Data Calc
    B_TheFLOWOP = TheYIELD
    A_TheOInput = Flowrate
    A_TheOLCT = (TheCTS_Losses*Flowrate)/100
    A_TheSDGG = (P1_Thecalc5-P1_Thecalc2-P1_Thecalc3)/100*Flowrate
    A_TheAO = (P2_Thecalc5-P2_Thecalc3-P2_Thecalc4 +
               P3_Thecalc5-P3_Thecalc5-P3_Thecalc2)/100*Flowrate

    A_TheOIC = (P4_Thecalc5-P4_Thecalc2)/100*Flowrate
    A_TheOIWFA = (P5_Thecalc5-P5_Thecalc2)/100*Flowrate
    A_ThePMI = (P1_Var3+P1_Impurities-P7_Var3-P7_Impurities)*Flowrate/100
    A_TheD = (P6_Thecalc5-P6_Thecalc2)/100*Flowrate
    A_TheWW = TheWW*Flowrate/100
    A_TheUEXLOS = TheUEXLOS*Flowrate/100
    A_TheFLOWOP = B_TheFLOWOP/100*Flowrate
    A_TheTOTAL = A_TheOLCT+A_TheSDGG+A_TheAO+A_TheOIC + \
        A_TheOIWFA+A_ThePMI+A_TheD+A_TheWW+A_TheUEXLOS+A_TheFLOWOP
    
    B_TheOLCT = A_TheOLCT/A_TheOInput*100
    B_TheSDGG = A_TheSDGG/A_TheOInput*100
    B_TheAO = A_TheAO/A_TheOInput*100
    B_TheOIC = A_TheOIC/A_TheOInput*100
    B_TheOIWFA = A_TheOIWFA/A_TheOInput*100
    B_ThePMI = A_ThePMI/A_TheOInput*100
    B_TheD = A_TheD/A_TheOInput*100
    B_TheWW = A_TheWW/A_TheOInput*100
    B_TheUEXLOS = A_TheUEXLOS/A_TheOInput*100
    B_TheFLOWOP = TheYIELD
    B_TheTOTAL = B_TheOLCT+B_TheSDGG+B_TheAO+B_TheOIC + \
        B_TheOIWFA+B_ThePMI+B_TheD+B_TheWW+B_TheUEXLOS+B_TheFLOWOP
    
    C_TheOLCT = A_TheOLCT*CTF/1000
    C_TheSDGG = A_TheSDGG*GSBC/1000
    C_TheAO = A_TheAO*AO/1000
    C_TheOIC = A_TheOIC*GSBC/1000
    C_TheOIWFA = A_TheOIWFA*WFA/1000
    C_ThePMI = A_ThePMI*0/1000
    C_TheD = A_TheD*PRD/1000
    C_TheWW = A_TheWW*0/1000
    C_TheUEXLOS = A_TheUEXLOS*0/1000
    C_TheFLOWOP = A_TheFLOWOP*RO/1000
    C_TheTOTAL = C_TheAO+C_TheOIC+C_TheOIWFA + \
        C_ThePMI+C_TheD+C_TheWW+C_TheUEXLOS+C_TheFLOWOP
    
    D_TheOLCT = (B_TheOLCT*CO/100)-(C_TheOLCT*1000/Flowrate)
    D_TheSDGG = (B_TheSDGG*CO/100)-(C_TheSDGG*1000/Flowrate)
    D_TheAO = (B_TheAO*CO/100)-(C_TheAO*1000/Flowrate)
    D_TheOIC = (B_TheOIC*CO/100)-(C_TheOIC*1000/Flowrate)
    D_TheOIWFA = (B_TheOIWFA*CO/100)-(C_TheOIWFA*1000/Flowrate)
    D_ThePMI = (B_ThePMI*CO/100)-(C_ThePMI*1000/Flowrate)
    D_TheD = (B_TheD*CO/100)-(C_TheD*1000/Flowrate)
    D_TheWW = (B_TheWW*CO/100)-(C_TheWW*1000/Flowrate)
    D_TheUEXLOS = (B_TheUEXLOS*CO/100)-(C_TheUEXLOS*1000/Flowrate)
    D_TheTOTAL = D_TheOLCT+D_TheSDGG+D_TheAO+D_TheOIC + \
        D_TheOIWFA+D_ThePMI+D_TheD+D_TheWW+D_TheUEXLOS
    
    TheFS = D_TheTOTAL
    

    #################################################################################################
    # Difference Summary
    Diff_OLCT = (D_OLCT-D_TheOLCT)*Flowrate/1000
    Diff_SDGG = (D_SDGG-D_TheSDGG)*Flowrate/1000
    Diff_AO = (D_AO-D_TheAO)*Flowrate/1000
    Diff_OIC = (D_OIC-D_TheOIC)*Flowrate/1000
    Diff_OIWFA = (D_OIWFA-D_TheOIWFA)*Flowrate/1000
    Diff_PMI = (D_PMI-D_ThePMI)*Flowrate/1000
    Diff_D = (D_D-D_TheD)*Flowrate/1000
    Diff_WW = (D_WW-D_TheWW)*Flowrate/1000
    Diff_UEXLOS = (D_UEXLOS-D_TheUEXLOS)*Flowrate/1000
    Diff_FLOWOP = (C_TheFLOWOP-C_FLOWOP)/(RO)*(RO-CO)
    Diff_TOTAL = Diff_OLCT+Diff_SDGG+Diff_AO+Diff_OIC + \
        Diff_OIWFA+Diff_PMI+Diff_D+Diff_WW+Diff_UEXLOS+Diff_FLOWOP

    de=values()
    de.CO=round(CO,2)
    de.PRD=round(PRD,2)
    de.CTF=round(CTF,2)
    de.WFA=round(WFA,2)
    de.GSBC=round(GSBC,2)
    de.RO=round(RO,2)
    de.AO=round(AO,2)
    de.Flowrate=round(Flowrate,2)
    de.Hours=round(Hours,2)
    de.CTS_Losses=round(CTS_Losses,2)
    de.TheCTS_Losses=round(TheCTS_Losses,2)
    de.WW=round(WW,2)
    de.TheWW=round(TheWW,2)
    de.UEXLOS=round(UEXLOS,2)
    de.TheUEXLOS=round(TheUEXLOS,2)
    de.P1_FlowPercent=round(P1_FlowPercent,2)
    de.P2_Var1=round(P2_Var1,2)
    de.P2_Var1=round(P2_Var1,2)
    de.P3_Var1=round(P3_Var1,2)
    de.P4_Var1=round(P4_Var1,2)
    de.P5_Var1=round(P5_Var1,2)
    de.P6_Var1=round(P6_Var1,2)
    de.P7_Var1=round(P7_Var1,2)
    de.P1_Var2=round(P1_Var2,2)
    de.P2_Var2=round(P2_Var2,2)
    de.P3_Var2=round(P3_Var2,2)
    de.P4_Var2=round(P4_Var2,2)
    de.P5_Var2=round(P5_Var2,2)
    de.P6_Var2=round(P6_Var2,2)
    de.P7_Var2=round(P7_Var2,2)
    de.P1_Var3=round(P1_Var3,2)
    de.P2_Var3=round(P2_Var3,2)
    de.P3_Var3=round(P3_Var3,2)
    de.P4_Var3=round(P4_Var3,2)
    de.P5_Var3=round(P5_Var3,2)
    de.P6_Var3=round(P6_Var3,2)
    de.P7_Var3=round(P7_Var3,2)
    de.P1_Impurities=round(P1_Impurities,2)
    de.P2_Impurities=round(P2_Impurities,2)
    de.P3_Impurities=round(P3_Impurities,2)
    de.P4_Impurities=round(P4_Impurities,2)
    de.P5_Impurities=round(P5_Impurities,2)
    de.P6_Impurities=round(P6_Impurities,2)
    de.P1_Impurities=round(P1_Impurities,2)
    de.P1_Mass=round(P1_Mass,2)
    de.P2_Mass=round(P2_Mass,2)
    de.P3_Mass=round(P3_Mass,2)
    de.P4_Mass=round(P4_Mass,2)
    de.P5_Mass=round(P5_Mass,2)
    de.P6_Mass=round(P6_Mass,2)
    de.P1_Wax1=round(P1_Wax1,2)
    de.P2_Wax1=round(P2_Wax1,2)
    de.P3_Wax1=round(P3_Wax1,2)
    de.P4_Wax1=round(P4_Wax1,2)
    de.P5_Wax1=round(P5_Wax1,2)
    de.P6_Wax1=round(P6_Wax1,2)
    de.P1_Ass1=round(P1_Ass1,2)
    de.P2_Ass1=round(P2_Ass1,2)
    de.P3_Ass1=round(P3_Ass1,2)
    de.P4_Ass1=round(P4_Ass1,2)
    de.P5_Ass1=round(P5_Ass1,2)
    de.P6_Ass1=round(P6_Ass1,2)
    de.P1_TheAss1=round(P1_TheAss1,2)
    de.P2_TheAss1=round(P2_TheAss1,2)
    de.P3_TheAss1=round(P3_TheAss1,2)
    de.P4_TheAss1=round(P4_TheAss1,2)
    de.P5_TheAss1=round(P5_TheAss1,2)
    de.P6_TheAss1=round(P6_TheAss1,2)
    de.P1_Ass2=round(P1_Ass2,2)
    de.P2_Ass2=round(P2_Ass2,2)
    de.P3_Ass2=round(P3_Ass2,2)
    de.P4_Ass2=round(P4_Ass2,2)
    de.P5_Ass2=round(P5_Ass2,2)
    de.P6_Ass2=round(P6_Ass2,2)
    de.P1_TheAss2=round(P1_TheAss2,2)
    de.P2_TheAss2=round(P2_TheAss2,2)
    de.P3_TheAss2=round(P3_TheAss2,2)
    de.P4_TheAss2=round(P4_TheAss2,2)
    de.P5_TheAss2=round(P5_TheAss2,2)
    de.P6_TheAss2=round(P6_TheAss2,2)
    de.P1_Ass3=round(P1_Ass3,2)
    de.P2_Ass3=round(P2_Ass3,2)
    de.P3_Ass3=round(P3_Ass3,2)
    de.P4_Ass3=round(P4_Ass3,2)
    de.P5_Ass3=round(P5_Ass3,2)
    de.P6_Ass3=round(P6_Ass3,2)
    de.P1_TheAss3=round(P1_TheAss3,2)
    de.P2_TheAss3=round(P2_TheAss3,2)
    de.P3_TheAss3=round(P3_TheAss3,2)
    de.P4_TheAss3=round(P4_TheAss3,2)
    de.P5_TheAss3=round(P5_TheAss3,2)
    de.P6_TheAss3=round(P6_TheAss3,2)
    de.P1_Ass4=round(P1_Ass4,2)
    de.P2_Ass4=round(P2_Ass4,2)
    de.P3_Ass4=round(P3_Ass4,2)
    de.P4_Ass4=round(P4_Ass4,2)
    de.P5_Ass4=round(P5_Ass4,2)
    de.P6_Ass4=round(P6_Ass4,2)
    de.P1_TheAss4=round(P1_TheAss4,2)
    de.P2_TheAss4=round(P2_TheAss4,2)
    de.P3_TheAss4=round(P3_TheAss4,2)
    de.P4_TheAss4=round(P4_TheAss4,2)
    de.P5_TheAss4=round(P5_TheAss4,2)
    de.P6_TheAss4=round(P6_TheAss4,2)
    de.P2_Iter=round(P2_Iter,2)
    de.P3_Iter=round(P3_Iter,2)
    de.P4_Iter=round(P4_Iter,2)
    de.P5_Iter=round(P5_Iter,2)
    de.P6_Iter=round(P6_Iter,2)
    de.P1_FlowPercent=round(P1_FlowPercent,2)
    de.P2_FlowPercent=round(P2_FlowPercent,2)
    de.P3_FlowPercent=round(P3_FlowPercent,2)
    de.P4_FlowPercent=round(P4_FlowPercent,2)
    de.P5_FlowPercent=round(P5_FlowPercent,2)
    de.P6_FlowPercent=round(P6_FlowPercent,2)
    de.P1_calc1=round(P1_calc1,2)
    de.P2_calc1=round(P2_calc1,2)
    de.P3_calc1=round(P3_calc1,2)
    de.P4_calc1=round(P4_calc1,2)
    de.P5_calc1=round(P5_calc1,2)
    de.P6_calc1=round(P6_calc1,2)
    de.P1_calc1withfactor=round(P1_calc1withfactor,2)
    de.P2_calc1withfactor=round(P2_calc1withfactor,2)
    de.P3_calc1withfactor=round(P3_calc1withfactor,2)
    de.P4_calc1withfactor=round(P4_calc1withfactor,2)
    de.P5_calc1withfactor=round(P5_calc1withfactor,2)
    de.P6_calc1withfactor=round(P6_calc1withfactor,2)
    de.P1_Loss1=round(P1_Loss1,2)
    de.P2_Loss1=round(P2_Loss1,2)
    de.P3_Loss1=round(P3_Loss1,2)
    de.P4_Loss1=round(P4_Loss1,2)
    de.P5_Loss1=round(P5_Loss1,2)
    de.P6_Loss1=round(P6_Loss1,2)
    de.P1_Loss1withfactor=round(P1_Loss1withfactor,2)
    de.P2_Loss1withfactor=round(P2_Loss1withfactor,2)
    de.P3_Loss1withfactor=round(P3_Loss1withfactor,2)
    de.P4_Loss1withfactor=round(P4_Loss1withfactor,2)
    de.P5_Loss1withfactor=round(P5_Loss1withfactor,2)
    de.P6_Loss1withfactor=round(P6_Loss1withfactor,2)
    de.P1_calc2=round(P1_calc2,2)
    de.P2_calc2=round(P2_calc2,2)
    de.P3_calc2=round(P3_calc2,2)
    de.P4_calc2=round(P4_calc2,2)
    de.P5_calc2=round(P5_calc2,2)
    de.P6_calc2=round(P6_calc2,2)
    de.P1_calc3=round(P1_calc3,2)
    de.P2_calc3=round(P2_calc3,2)
    #de.P3_calc3=round(P3_calc3,2)
    #de.P4_calc3=round(P4_calc3,2)
    #de.P5_calc3=round(P5_calc3,2)
    #de.P6_calc3=round(P6_calc3,2)
    de.P1_calc4=round(P1_calc4,2)
    de.P2_calc4=round(P2_calc4,2)
    #de.P3_calc4=round(P3_calc4,2)
    de.P4_calc4=round(P4_calc4,2)
    de.P5_calc4=round(P5_calc4,2)
    #de.P6_calc4=round(P6_calc4,2)
    de.P1_calc5=round(P1_calc5,2)
    de.P2_calc5=round(P2_calc5,2)
    de.P3_calc5=round(P3_calc5,2)
    de.P4_calc5=round(P4_calc5,2)
    de.P5_calc5=round(P5_calc5,2)
    de.P6_calc5=round(P6_calc5,2)
    de.TUCMASS=round(TUCMASS,2)
    de.FLOWLOSS=round(FLOWLOSS,2)
    de.YIELD=round(YIELD,2)
    de.TUCFACT=round(TUCFACT,2)
    de.FS=round(FS,2)
    de.P2_TheIter=round(P2_TheIter,2)
    de.P3_TheIter=round(P3_TheIter,2)
    de.P4_TheIter=round(P4_TheIter,2)
    de.P5_TheIter=round(P5_TheIter,2)
    de.P6_TheIter=round(P6_TheIter,2)
    de.P2_TheFlowPercent=round(P2_TheFlowPercent,2)
    de.P3_TheFlowPercent=round(P3_TheFlowPercent,2)
    de.P4_TheFlowPercent=round(P4_TheFlowPercent,2)
    de.P5_TheFlowPercent=round(P5_TheFlowPercent,2)
    de.P6_TheFlowPercent=round(P6_TheFlowPercent,2)
    de.P1_Thecalc1=round(P1_Thecalc1,2)
    de.P2_Thecalc1=round(P2_Thecalc1,2)
    de.P3_Thecalc1=round(P3_Thecalc1,2)
    de.P4_Thecalc1=round(P4_Thecalc1,2)
    de.P5_Thecalc1=round(P5_Thecalc1,2)
    de.P6_Thecalc1=round(P6_Thecalc1,2)
    de.P1_Thecalc1withfactor=round(P1_Thecalc1withfactor,2)
    de.P2_Thecalc1withfactor=round(P2_Thecalc1withfactor,2)
    de.P3_Thecalc1withfactor=round(P3_Thecalc1withfactor,2)
    de.P4_Thecalc1withfactor=round(P4_Thecalc1withfactor,2)
    de.P5_Thecalc1withfactor=round(P5_Thecalc1withfactor,2)
    de.P6_Thecalc1withfactor=round(P6_Thecalc1withfactor,2)
    de.P1_TheLoss1=round(P1_TheLoss1,2)
    de.P2_TheLoss1=round(P2_TheLoss1,2)
    de.P3_TheLoss1=round(P3_TheLoss1,2)
    de.P4_TheLoss1=round(P4_TheLoss1,2)
    de.P5_TheLoss1=round(P5_TheLoss1,2)
    de.P6_TheLoss1=round(P6_TheLoss1,2)
    de.P1_TheLoss1withfactor=round(P1_TheLoss1withfactor,2)
    de.P2_TheLoss1withfactor=round(P2_TheLoss1withfactor,2)
    de.P3_TheLoss1withfactor=round(P3_TheLoss1withfactor,2)
    de.P4_TheLoss1withfactor=round(P4_TheLoss1withfactor,2)
    de.P5_TheLoss1withfactor=round(P5_TheLoss1withfactor,2)
    de.P6_TheLoss1withfactor=round(P6_TheLoss1withfactor,2)
    de.P1_Thecalc2=round(P1_Thecalc2,2)
    de.P2_Thecalc2=round(P2_Thecalc2,2)
    de.P3_Thecalc2=round(P3_Thecalc2,2)
    de.P4_Thecalc2=round(P4_Thecalc2,2)
    de.P5_Thecalc2=round(P5_Thecalc2,2)
    de.P6_Thecalc2=round(P6_Thecalc2,2)
    de.P1_Thecalc3=round(P1_Thecalc3,2)
    de.P2_Thecalc3=round(P2_Thecalc3,2)
    #de.P3_Thecalc3=round(P3_Thecalc3,2)
    #de.P4_Thecalc3=round(P4_Thecalc3,2)
    #de.P5_Thecalc3=round(P5_Thecalc3,2)
    #de.P6_Thecalc3=round(P6_Thecalc3,2)
    de.P1_Thecalc4=round(P1_Thecalc4,2)
    de.P2_Thecalc4=round(P2_Thecalc4,2)
    #de.P3_Thecalc4=round(P3_Thecalc4,2)
    de.P4_Thecalc4=round(P4_Thecalc4,2)
    de.P5_Thecalc4=round(P5_Thecalc4,2)
    #de.P6_Thecalc4=round(P6_Thecalc4,2)
    de.P1_Thecalc5=round(P1_Thecalc5,2)
    de.P2_Thecalc5=round(P2_Thecalc5,2)
    de.P3_Thecalc5=round(P3_Thecalc5,2)
    de.P4_Thecalc5=round(P4_Thecalc5,2)
    de.P5_Thecalc5=round(P5_Thecalc5,2)
    de.P6_Thecalc5=round(P6_Thecalc5,2)
    de.TheTUCMASS=round(TheTUCMASS,2)
    de.TheFLOWLOSS=round(TheFLOWLOSS,2)
    de.TheYIELD=round(TheYIELD,2)
    de.TheTUCFACT=round(TheTUCFACT,2)
    de.TheFS=round(TheFS,2)
    de.A_OInput=round(A_OInput,2)
    de.A_OLCT=round(A_OLCT,2)
    de.B_OLCT=round(B_OLCT,2)
    de.C_OLCT=round(C_OLCT,2)
    de.D_OLCT=round(D_OLCT,2)
    de.A_SDGG=round(A_SDGG,2)
    de.B_SDGG=round(B_SDGG,2)
    de.C_SDGG=round(C_SDGG,2)
    de.D_SDGG=round(D_SDGG,2)
    de.A_AO=round(A_AO,2)
    de.B_AO=round(B_AO,2)
    de.C_AO=round(C_AO,2)
    de.D_AO=round(D_AO,2)
    de.A_OIC=round(A_OIC,2)
    de.B_OIC=round(B_OIC,2)
    de.C_OIC=round(C_OIC,2)
    de.D_OIC=round(D_OIC,2)
    de.A_OIWFA=round(A_OIWFA,2)
    de.B_OIWFA=round(B_OIWFA,2)
    de.C_OIWFA=round(C_OIWFA,2)
    de.D_OIWFA=round(D_OIWFA,2)
    de.A_PMI=round(A_PMI,2)
    de.B_PMI=round(B_PMI,2)
    de.C_PMI=round(C_PMI,2)
    de.D_PMI=round(D_PMI,2)
    de.A_D=round(A_D,2)
    de.B_D=round(B_D,2)
    de.C_D=round(C_D,2)
    de.D_D=round(D_D,2)
    de.A_WW=round(A_WW,2)
    de.B_WW=round(B_WW,2)
    de.C_WW=round(C_WW,2)
    de.D_WW=round(D_WW,2)
    de.A_UEXLOS=round(A_UEXLOS,2)
    de.B_UEXLOS=round(B_UEXLOS,2)
    de.C_UEXLOS=round(C_UEXLOS,2)
    de.D_UEXLOS=round(D_UEXLOS,2)
    de.A_FLOWOP=round(A_FLOWOP,2)
    de.B_FLOWOP=round(B_FLOWOP,2)
    de.C_FLOWOP=round(C_FLOWOP,2)
    #de.D_FLOWOP=round(D_FLOWOP,2)
    de.A_TOTAL=round(A_TOTAL,2)
    de.B_TOTAL=round(B_TOTAL,2)
    de.C_TOTAL=round(C_TOTAL,2)
    de.D_TOTAL=round(D_TOTAL,2)
    de.A_TheOInput=round(A_TheOInput,2)
    de.A_TheOLCT=round(A_TheOLCT,2)
    de.B_TheOLCT=round(B_TheOLCT,2)
    de.C_TheOLCT=round(C_TheOLCT,2)
    de.D_TheOLCT=round(D_TheOLCT,2)
    de.A_TheSDGG=round(A_TheSDGG,2)
    de.B_TheSDGG=round(B_TheSDGG,2)
    de.C_TheSDGG=round(C_TheSDGG,2)
    de.D_TheSDGG=round(D_TheSDGG,2)
    de.A_TheAO=round(A_TheAO,2)
    de.B_TheAO=round(B_TheAO,2)
    de.C_TheAO=round(C_TheAO,2)
    de.D_TheAO=round(D_TheAO,2)
    de.A_TheOIC=round(A_TheOIC,2)
    de.B_TheOIC=round(B_TheOIC,2)
    de.C_TheOIC=round(C_TheOIC,2)
    de.D_TheOIC=round(D_TheOIC,2)
    de.A_TheOIWFA=round(A_TheOIWFA,2)
    de.B_TheOIWFA=round(B_TheOIWFA,2)
    de.C_TheOIWFA=round(C_TheOIWFA,2)
    de.D_TheOIWFA=round(D_TheOIWFA,2)
    de.A_ThePMI=round(A_ThePMI,2)
    de.B_ThePMI=round(B_ThePMI,2)
    de.C_ThePMI=round(C_ThePMI,2)
    de.D_ThePMI=round(D_ThePMI,2)
    de.A_TheD=round(A_TheD,2)
    de.B_TheD=round(B_TheD,2)
    de.C_TheD=round(C_TheD,2)
    de.D_TheD=round(D_TheD,2)
    de.A_TheWW=round(A_TheWW,2)
    de.B_TheWW=round(B_TheWW,2)
    de.C_TheWW=round(C_TheWW,2)
    de.D_TheWW=round(D_TheWW,2)
    de.A_TheUEXLOS=round(A_TheUEXLOS,2)
    de.B_TheUEXLOS=round(B_TheUEXLOS,2)
    de.C_TheUEXLOS=round(C_TheUEXLOS,2)
    de.D_TheUEXLOS=round(D_TheUEXLOS,2)
    de.A_TheFLOWOP=round(A_TheFLOWOP,2)
    de.B_TheFLOWOP=round(B_TheFLOWOP,2)
    de.C_TheFLOWOP=round(C_TheFLOWOP,2)
    #de.D_TheFLOWOP=round(D_TheFLOWOP,2)
    de.A_TheTOTAL=round(A_TheTOTAL,2)
    de.B_TheTOTAL=round(B_TheTOTAL,2)
    de.C_TheTOTAL=round(C_TheTOTAL,2)
    de.D_TheTOTAL=round(D_TheTOTAL,2)
    de.Diff_OLCT=round(Diff_OLCT,2)
    de.Diff_SDGG=round(Diff_SDGG,2)
    de.Diff_AO=round(Diff_AO,2)
    de.Diff_OIC=round(Diff_OIC,2)
    de.Diff_OIWFA=round(Diff_OIWFA,2)
    de.Diff_PMI=round(Diff_PMI,2)
    de.Diff_D=round(Diff_D,2)
    de.Diff_WW=round(Diff_WW,2)
    de.Diff_UEXLOS=round(Diff_UEXLOS,2)
    de.Diff_FLOWOP=round(Diff_FLOWOP,2)
    de.Diff_TOTAL=round(Diff_TOTAL,2)




    return render(request, "home.html",{'de':de})
     