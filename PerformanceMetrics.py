import sklearn.metrics as metrics


def construct(initial, final):
    for i in range(len(initial)):
        if initial[i].lower() == 'pozitiv':
            final.append(0)
        else:
            final.append(1)


if __name__ == '__main__':
    x = []
    y = []
    v = [item for item in input("Enter actual list: ").split()]
    w = [item for item in input("Enter predicted list: ").split()]

    construct(v, x)
    construct(w, y)

    accuracy = metrics.accuracy_score(x, y)
    precision = metrics.precision_score(x, y)
    recall = metrics.recall_score(x, y)
    f1 = metrics.f1_score(x, y)
    cm = metrics.confusion_matrix(x, y, labels=[0, 1])

    print('Accuracy = ' + str('{0:.2f}'.format(accuracy * 100)) + '%')
    print('Precision = ' + str('{0:.2f}'.format(precision * 100)) + '%')
    print('Recall = ' + str('{0:.2f}'.format(recall * 100)) + '%')
    print('F1 = ' + str('{0:.2f}'.format(f1 * 100)) + '%')
    print('CM = [' + str(cm[0]) + '\n      ' + str(cm[1]) + ']')
    try:
        auc = metrics.roc_auc_score(x, y)
        print('AUC = ' + str('{0:.2f}'.format(auc * 100)) + '%')
    except ValueError:
        pass
