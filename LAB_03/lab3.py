import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from scipy.spatial.distance import minkowski
import data


def dot_product(x, y):
    s = 0
    for i in range(len(x)):
        s += x[i] * y[i]
    return s


def euclidean_norm(x):
    s = 0
    for v in x:
        s += v * v
    return s ** 0.5


def calculate_mean(arr):
    s = 0
    for v in arr:
        s += v
    return s / len(arr)


def calculate_variance(arr, mean_val):
    s = 0
    for v in arr:
        s += (v - mean_val) ** 2
    return s / len(arr)


def minkowski_distance(v1, v2, p):
    s = 0
    for i in range(len(v1)):
        s += abs(v1[i] - v2[i]) ** p
    return s ** (1 / p)


def normalize_data(X):
    Xn = X.copy()
    for j in range(X.shape[1]):
        mn = np.min(X[:, j])
        mx = np.max(X[:, j])
        for i in range(X.shape[0]):
            Xn[i][j] = (X[i][j] - mn) / (mx - mn)
    return Xn


def custom_knn_predict(train_X, train_y, test_vec, k):
    dist_list = []
    for i in range(len(train_X)):
        d = minkowski_distance(train_X[i], test_vec, 3)
        dist_list.append((d, train_y[i]))

    dist_list.sort(key=lambda x: x[0])

    votes = {}
    for i in range(k):
        lbl = dist_list[i][1]
        votes[lbl] = votes.get(lbl, 0) + 1

    return max(votes, key=votes.get)


def calculate_confusion_metrics(actual, predicted):
    tp = tn = fp = fn = 0

    for i in range(len(actual)):
        if actual[i] == 1 and predicted[i] == 1:
            tp += 1
        elif actual[i] == 0 and predicted[i] == 0:
            tn += 1
        elif actual[i] == 0 and predicted[i] == 1:
            fp += 1
        elif actual[i] == 1 and predicted[i] == 0:
            fn += 1

    acc = (tp + tn) / (tp + tn + fp + fn)
    prec = tp / (tp + fp) if (tp + fp) != 0 else 0
    rec = tp / (tp + fn) if (tp + fn) != 0 else 0
    f1 = (2 * prec * rec) / (prec + rec) if (prec + rec) != 0 else 0

    return tp, tn, fp, fn, acc, prec, rec, f1


def main():
    df = data.data
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    X = normalize_data(X)

    v1 = X[2]
    v2 = X[6]

    manual_dp = dot_product(v1, v2)
    numpy_dp = np.dot(v1, v2)

    manual_norm = euclidean_norm(v1)
    numpy_norm = np.linalg.norm(v1)

    X0 = X[y == 0]
    X1 = X[y == 1]

    mean0 = np.mean(X0, axis=0)
    mean1 = np.mean(X1, axis=0)

    std0 = np.std(X0, axis=0)
    std1 = np.std(X1, axis=0)

    inter_dist = np.linalg.norm(mean0 - mean1)

    feat = X[:, 1]
    feat_mean = calculate_mean(feat)
    feat_var = calculate_variance(feat, feat_mean)

    plt.hist(feat, bins=6)
    plt.show()

    mink_vals = []
    for p in range(2, 9):
        mink_vals.append(minkowski_distance(v1, v2, p))

    plt.plot(range(2, 9), mink_vals)
    plt.show()

    scipy_mink = minkowski(v1, v2, 4)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=7
    )

    knn = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=3)
    knn.fit(X_train, y_train)

    knn_acc = knn.score(X_test, y_test)
    sklearn_preds = knn.predict(X_test)

    custom_preds = []
    for vec in X_test:
        custom_preds.append(custom_knn_predict(X_train, y_train, vec, 5))

    k_vals = []
    acc_vals = []
    for k in range(1, 8):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, y_train)
        k_vals.append(k)
        acc_vals.append(model.score(X_test, y_test))

    tp, tn, fp, fn, acc, prec, rec, f1 = calculate_confusion_metrics(
        y_test, sklearn_preds
    )

    print("A1:", manual_dp, numpy_dp, manual_norm, numpy_norm)
    print("A2:", mean0, mean1, std0, std1, inter_dist)
    print("A3:", feat_mean, feat_var)
    print("A4 Minkowski values:", mink_vals)
    print("A5 SciPy Minkowski:", scipy_mink)
    print("A6 Train:", len(X_train), "Test:", len(X_test))
    print("A7 kNN with k=5")
    print("A8 Accuracy:", knn_acc)
    print("A9 sklearn predictions:", sklearn_preds)
    print("A10 custom predictions:", custom_preds)
    print("A11 k values:", k_vals)
    print("A11 accuracies:", acc_vals)
    print("A12/A13:", tp, tn, fp, fn, acc, prec, rec, f1)
    print("A14 Comparison: Distance based vs linear assumption")


main()
