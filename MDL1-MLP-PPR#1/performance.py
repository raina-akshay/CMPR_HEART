from matplotlib import pyplot as plt
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import confusion_matrix, f1_score, recall_score, precision_score, classification_report
import pandas as pd
from sklearn.model_selection import cross_val_score
from train_n_test import traintest


def perfor():
    tnt = traintest()
    true, pred, proba = tnt.run()
    return true, pred, proba

true, pred, prob=perfor()

fpr, tpr, thresh = roc_curve(true, prob[:,1], pos_label=1)
auc_score = roc_auc_score(true, prob[:,1])

# roc curve for tpr = fpr 
random_probs = [0 for i in range(len(true))]
p_fpr, p_tpr, _ = roc_curve(true, random_probs, pos_label=1)

plt.style.use('default')
plt.plot(fpr, tpr, linestyle='--',color='orange', label='MLP')
plt.plot(p_fpr, p_tpr, linestyle='-', color='blue')
# title
plt.title('ROC curve')
# x label
plt.xlabel('False Positive Rate')
# y label
plt.ylabel('True Positive rate')

plt.legend(loc='best')
plt.savefig('ROC',dpi=300)
plt.show();

#add 02/02/2021 (without 10 fold)

# cm = confusion_matrix(true,pred)
# print(cm)
# tn, fp, fn, tp = cm.ravel()
# print(tn,fp,fn,tp)

# rs_macro = recall_score(true, pred, average='macro')
# rs_micro = recall_score(true, pred, average='micro')
# rs_weighted = recall_score(true, pred, average='weighted')
# rs = recall_score(true, pred, average=None)
# print(rs_macro, rs_micro, rs_weighted, rs)

# fs_macro = f1_score(true, pred, average='macro')
# fs_micro = f1_score(true, pred, average='micro')
# fs_weighted = f1_score(true, pred, average='weighted')
# fs = f1_score(true, pred, average=None)
# print(fs_macro, fs_micro, fs_weighted, fs)

# ps_macro = precision_score(true, pred, average='macro')
# ps_micro = precision_score(true, pred, average='micro')
# ps_weighted = precision_score(true, pred, average='weighted')
# ps = precision_score(true, pred, average=None)
# print(ps_macro, ps_micro, ps_weighted, ps)

# report = pd.DataFrame(classification_report(true, pred, output_dict=True))
# print(report)

#add 03/02/2021 (with 10 fold - average)

# ac = 0
# for i in range(len(pred)):
#         ac = ac + a_s(true[i+1], pred[i+1])
# print("{} is the average accuracy." .format(ac*100/10))

# ps = 0
# for i in range(len(pred)):
#         ps = ps + precision_score(true[i+1], pred[i+1])
# print("{} is the average precision." .format(ps*100/10))

# rs = 0
# for i in range(len(pred)):
#         rs = rs + recall_score(true[i+1], pred[i+1])
# print("{} is the average recall." .format(rs*100/10))

# fs = 0
# for i in range(len(pred)):
#         fs = fs + f1_score(true[i+1], pred[i+1])
# print("{} is the average f1 score." .format(fs*100/10))

#not important

# for i in range(len(pred)):
#     report = pd.DataFrame(classification_report(true[i+1], pred[i+1], output_dict=True))
#     print(report)
    
# for i in range(len(pred)):    
#     cm = confusion_matrix(true[i+1],pred[i+1])
#     tn, fp, fn, tp = cm.ravel()
#     print(tn,fp,fn,tp)