import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

def purchase_analysis(data):
    candies = data["Candies (#)"].values
    mangoes = data["Mangoes (Kg)"].values
    milk = data["Milk Packets (#)"].values
    payment = data["Payment (Rs)"].values
    X = []
    for i in range(len(candies)):
        X.append([candies[i], mangoes[i], milk[i]])

    X = np.array(X)
    y = payment.reshape(-1, 1)
    rank = np.linalg.matrix_rank(X)
    cost = np.linalg.pinv(X).dot(y)
    return X, rank, cost


def classify_customers(payment):
    status = []
    for amt in payment:
        if amt > 200:
            status.append("RICH")
        else:
            status.append("POOR")
    return status


def stock_statistics(stock):
    prices = stock["Price"]
    change = stock["Chg%"]
    days = stock["Day"]
    months = stock["Month"]

    start = time.time()
    total = 0
    for p in prices:
        total += p
    mean_manual = total / len(prices)

    var_sum = 0
    for p in prices:
        var_sum += (p - mean_manual) ** 2
    var_manual = var_sum / len(prices)
    exec_time = time.time() - start

    loss_count = 0
    for c in change:
        if c < 0:
            loss_count += 1
    loss_prob = loss_count / len(change)

    wed_prices = []
    for i in range(len(days)):
        if days[i] == "Wed":
            wed_prices.append(prices[i])

    apr_prices = []
    for i in range(len(months)):
        if months[i] == "Apr":
            apr_prices.append(prices[i])

    wed_profit = 0
    wed_total = 0
    for i in range(len(days)):
        if days[i] == "Wed":
            wed_total += 1
            if change[i] > 0:
                wed_profit += 1

    cond_prob = wed_profit / wed_total if wed_total != 0 else 0
    return mean_manual, var_manual, exec_time, loss_prob, wed_prices, apr_prices, cond_prob


def dataset_analysis(data):
    return data.dtypes, data.isnull().sum(), data.describe()


def jaccard_smc(data):
    binary = data.select_dtypes(include="int64").iloc[:2]
    v1 = binary.iloc[0].values
    v2 = binary.iloc[1].values

    f11 = f00 = f10 = f01 = 0
    for i in range(len(v1)):
        if v1[i] == 1 and v2[i] == 1:
            f11 += 1
        elif v1[i] == 0 and v2[i] == 0:
            f00 += 1
        elif v1[i] == 1 and v2[i] == 0:
            f10 += 1
        elif v1[i] == 0 and v2[i] == 1:
            f01 += 1

    jc = f11 / (f11 + f10 + f01) if (f11 + f10 + f01) != 0 else 0
    smc = (f11 + f00) / (f11 + f10 + f01 + f00) if (f11 + f10 + f01 + f00) != 0 else 0
    return jc, smc


def cosine_similarity(data):
    num = data.select_dtypes(include=["int64", "float64"]).iloc[:2].values
    dot = np.dot(num[0], num[1])
    norm = np.linalg.norm(num[0]) * np.linalg.norm(num[1])
    return dot / norm if norm != 0 else 0


def impute_and_normalize(data):
    for col in data.columns:
        if data[col].dtype in ["int64", "float64"]:
            data[col] = data[col].fillna(data[col].median())
        else:
            data[col] = data[col].fillna(data[col].mode()[0])

    normalized = data.copy()
    for col in data.select_dtypes(include=["int64", "float64"]).columns:
        min_val = data[col].min()
        max_val = data[col].max()
        if max_val != min_val:
            normalized[col] = (data[col] - min_val) / (max_val - min_val)
        else:
            normalized[col] = 0

    return data.isnull().sum(), normalized


def main():

    file_name = r"D:\Sem4\KBDVM\MOULI\ML\Lab Session Data.xlsx"

    purchase = pd.read_excel(file_name, sheet_name="Purchase data")
    X, rank, cost = purchase_analysis(purchase)
    purchase["Status"] = classify_customers(purchase["Payment (Rs)"])

    stock = pd.read_excel(file_name, sheet_name="IRCTC Stock Price")
    mean_m, var_m, t, loss_p, wed_p, apr_p, cond_p = stock_statistics(stock)

    thyroid = pd.read_excel(file_name, sheet_name="thyroid0387_UCI")
    dtypes, missing, stats = dataset_analysis(thyroid)
    jc, smc = jaccard_smc(thyroid)
    cos = cosine_similarity(thyroid)
    missing_after, normalized = impute_and_normalize(thyroid)

    print("\nPurchase Data")
    print("Features:", X.shape[1])
    print("Records:", X.shape[0])
    print("Rank:", rank)
    print("Cost of Candies:", cost[0][0])
    print("Cost of Mangoes:", cost[1][0])
    print("Cost of Milk Packets:", cost[2][0])

    print("\nCustomer Classification")
    print(purchase[["Payment (Rs)", "Status"]])

    print("\nStock Analysis")
    print("Manual Mean:", mean_m)
    print("Manual Variance:", var_m)
    print("Execution Time:", t)
    print("Loss Probability:", loss_p)
    print("Wednesday Mean:", sum(wed_p) / len(wed_p) if len(wed_p) != 0 else 0)
    print("April Mean:", sum(apr_p) / len(apr_p) if len(apr_p) != 0 else 0)
    print("Conditional Profit:", cond_p)

    print("\nThyroid Dataset")
    print("Datatypes:\n", dtypes)
    print("\nMissing Values:\n", missing)
    print("\nStatistics:\n", stats)

    print("\nSimilarity Measures")
    print("Jaccard Coefficient:", jc)
    print("Simple Matching Coefficient:", smc)
    print("Cosine Similarity:", cos)

    print("\nAfter Imputation")
    print(missing_after)

    print("\nNormalization")
    print(normalized.head())


main()
