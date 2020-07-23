from scipy.optimize import minimize

###When using multivariate constrained optimization routine, variable
###must be typed in terms of args and you scatter them inside the 
###objective and constraint functions.  DO NOT TYPE EACH VARIABLE.

def U(args, alpha = 1/3):  # Reminder: Don't type A, B instead of args
    A, B = args
    return -(B**alpha * A**(1-alpha)) #Note the negative sign

def V(args):
    P, C = args
    return (P-20)**2 + 2*(C-1)**2 #Note all positive signs here

###All constraints must be in the form of greater than or equal to 0

def constraint1(args, W1=20, pa=2, pb=1):
    A, B = args
    return  W1 - pa*A - pb*B

def constraint2(args, W2=10, pp=1, pc=2): #not binding. 
    P, C = args
    return W2 - pp*P - pc*C

def constraint3(args, W2=50, pp=1, pc=2): #not binding. 
    P, C = args
    return W2 - pp*P - pc*C

def constraint4(args, W2=150, pp=1, pc=2): #not binding. 
    P, C = args
    return W2 - pp*P - pc*C

W1, pa, pb = 20, 2, 1
W2, pp, pc = [10, 50, 150], 1, 2 

###Constraints must be defined in terms of dictionary with the
###exact string syntax below if SLSQP is used.

con1 = {'type':'eq'  , 'fun':constraint1}  
con2 = {'type':'ineq', 'fun':constraint2}
con3 = {'type':'ineq', 'fun':constraint3}
con4 = {'type':'ineq', 'fun':constraint4}

result1 = minimize(U, x0 = [1, 1], method='SLSQP', bounds=[(1, W1/pa), (1, W1/pb)], constraints=con1)
print(f'Optimal_A is {result1.x[0]:.2f} and optimal_B is {result1.x[1]:.2f}')
for w, con in zip(W2, [con2, con3, con4]):
    result2 = minimize(V, x0 = [5, 2], bounds=[(0, w/pp),(0,w/pc)], method='SLSQP',  constraints=con)
    print(f'When W = {w}, optimal_P is {result2.x[0]} and optimal_C is {result2.x[1]}.')
