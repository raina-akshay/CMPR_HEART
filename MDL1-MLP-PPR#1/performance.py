from sklearn.metrics import precision_recall_fscore_support as prfs, accuracy_score as a_s
from matplotlib import pyplot as plt
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve, auc
from train_n_test import traintest as tnt

print('''\t 'kf: if k-fold required (boolean, required)' \n \t 'n: proportion to split data if kf=0 (float(0-1), optional, default=0.2)' \n \t 'k: folds for partition if kf=1 (integer, optional, default=10)' ''')
def perfor():
    print('''\t 'kf: if k-fold required (boolean, required)' \n \t 'n: proportion to split data if kf=0 (float(0-1), optional, default=0.2)' \n \t 'k: folds for partition if kf=1 (integer, optional, default=10)' ''')
    a=input('\t ENTER A VALUE (REQUIRED) FOR kf: \t'); 
    b=input('\t ENTER A VALUE (OPTIONAL: HIT ENTER TO SKIP) FOR n: \t') or 0.2; 
    c=input('\t ENTER A VALUE (OPTIONAL: HIT ENTER TO SKIP) FOR k: \t') or 10;
    true,pred,prob=tnt(kf=a,n=b,k=c)
    return true, pred, prob

true,pred, prob=perfor()
# print('The true values are: ',true)
# print('The predicted values are: ', pred)
# print('The prediction probabilites are: ', prob)

print('The accuracy score is: ',a_s(true,pred))

x=prfs(true,pred)

fpr, tpr, thresh = roc_curve(true, prob[:,1], pos_label=1)
auc_score = roc_auc_score(true, prob[:,1])

# roc curve for tpr = fpr 
random_probs = [0 for i in range(len(true))]
p_fpr, p_tpr, _ = roc_curve(true, random_probs, pos_label=1)

plt.style.use('seaborn')
plt.plot(fpr, tpr, linestyle='--',color='orange', label='MLP')
plt.plot(p_fpr, p_tpr, linestyle='--', color='blue')
# title
plt.title('ROC curve')
# x label
plt.xlabel('False Positive Rate')
# y label
plt.ylabel('True Positive rate')

plt.legend(loc='best')
plt.savefig('ROC',dpi=300)
plt.show();