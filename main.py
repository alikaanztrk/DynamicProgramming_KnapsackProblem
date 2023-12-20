import numpy as np

def knapsack_dynamic_programming(values, weights, capacity):
    n = len(values)
    # Tablo oluştur
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    selected_items_table = [[[] for _ in range(capacity + 1)] for _ in range(n + 1)]
    optimal_values = []  # Tüm optimal değerleri saklamak için liste

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Eğer mevcut ağırlık kapasitesinden küçükse, öğeyi ekleyip eklememeyi kontrol et
            if weights[i - 1] <= w:
                if values[i - 1] + dp[i - 1][w - weights[i - 1]] > dp[i - 1][w]:
                    dp[i][w] = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                    selected_items_table[i][w] = selected_items_table[i - 1][w - weights[i - 1]] + [i - 1]
                else:
                    dp[i][w] = dp[i - 1][w]
                    selected_items_table[i][w] = selected_items_table[i - 1][w]
            else:
                dp[i][w] = dp[i - 1][w]
                selected_items_table[i][w] = selected_items_table[i - 1][w]

            optimal_values.append(dp[i][w])  # Tüm optimal değerleri listeye ekleyin

    for i in range(n + 1): # Tüm çözümleri ve seçilen öğeleri yazdır
        for w in range(capacity + 1):
            print(f"DP[{i}][{w}] - Optimal Value: {dp[i][w]}, Selected Items: {selected_items_table[i][w]}")

    # Optimal çözüm değerini ve seçilen öğeleri bul
    final_optimal_value = dp[n][capacity]
    final_selected_items = selected_items_table[n][capacity]
    total_optimal_value = sum([dp[i][capacity] for i in range(n + 1)])  # Tüm optimal değerlerin standart sapmasını hesapla ve yazdır
    std_deviation = np.std(optimal_values)
    print("--------------------------------------------------------------------")
    print("\nTotal Optimal Value:", total_optimal_value)
    print("Standard Deviation of Optimal Values:", std_deviation)

    return final_optimal_value, final_selected_items

# Test
values = [8, 7, 10, 11, 8, 9, 5]
weights = [3, 2, 7, 6, 4, 10, 3]
capacity = 15

optimal_value, selected_items = knapsack_dynamic_programming(values, weights, capacity)
print("\nFinal Optimal Value:", optimal_value)
print("Final Selected Items:", selected_items)
