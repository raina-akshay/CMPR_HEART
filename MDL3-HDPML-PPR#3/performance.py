from matplotlib import pyplot as plt
from train_n_test import pred_prob

true, pred, prob = pred_prob()

def roc_graph(y_test, pred, prob):
    from sklearn.metrics import roc_auc_score
    from sklearn.metrics import roc_curve
    logit_roc_auc = roc_auc_score(y_test, pred)
    fpr, tpr, thresholds = roc_curve(y_test, prob[:,1])
    plt.figure()
    plt.plot(fpr, tpr, label='(area = %0.2f)' % logit_roc_auc)
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")
    plt.show()

def cmat_graph(model, X_test, y_test):
    from sklearn.metrics import plot_confusion_matrix
    plot_confusion_matrix(model, X_test, y_test, cmap=plt.cm.Blues)  
    plt.show()

def score(model, y_test, pred):
    from sklearn.metrics import confusion_matrix
    tn, fp, fn, tp = confusion_matrix(y_test, pred).ravel()
    print("-----------------------------------------------------------------")
    print("Model:", model)
    accuracy = (tp + tn)/(tp + tn + fp + fn)
    print(f"accuracy: {accuracy:4.2f}")
    precision = (tp / (tp + fp))
    print(f"precision: {precision:4.2f}")
    recall = (tp / (tp + fn))
    print(f"recall: {recall:4.2f}")
    f1_score = 2 * precision * recall / (precision + recall)
    print(f"f1_score: {f1_score:4.2f}")
    
roc_graph(true, pred, prob)