from train_n_test import traintest as tnt
print('''\t 'kf: if k-fold required (boolean, required)' \n \t 'n: proportion to split data if kf=0 (float(0-1), optional, default=0.2)' \n \t 'k: folds for partition if kf=1 (integer, optional, default=10)' ''')
def perfor():
    print('''\t 'kf: if k-fold required (boolean, required)' \n \t 'n: proportion to split data if kf=0 (float(0-1), optional, default=0.2)' \n \t 'k: folds for partition if kf=1 (integer, optional, default=10)' ''')
    a=input('\t ENTER A VALUE (REQUIRED) FOR kf: \t'); 
    b=input('\t ENTER A VALUE (OPTIONAL: HIT ENTER TO SKIP) FOR n: \t') or 0.2; 
    c=input('\t ENTER A VALUE (OPTIONAL: HIT ENTER TO SKIP) FOR k: \t') or 10;
    true,pred=tnt(kf=a,n=b,k=c)
    return true, pred

true,pred=perfor()
print('The true values are: ',true)
print('The predicted values are: ', pred)