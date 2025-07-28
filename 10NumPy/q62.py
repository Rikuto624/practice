import numpy as np

A = np.array([[1, 5, -2],
              [4, 0, -3],
              [-8, 2, 6]])

# --- 統計値の計算 ---
total_sum = np.sum(A)
max_value = np.max(A)
min_value = np.min(A)
mean_value = np.mean(A)
median_value = np.median(A)
variance = np.var(A)
std_dev = np.std(A)

# --- 結果の出力 ---
print("\n--- 統計計算結果 ---")
print(f"合計値:     {total_sum}")
print(f"最大値:     {max_value}")
print(f"最小値:     {min_value}")
print(f"平均値:     {mean_value}")
print(f"中央値:     {median_value}")
print(f"分散:       {variance:.4f}") # 小数点以下4桁で表示
print(f"標準偏差:   {std_dev:.4f}") # 小数点以下4桁で表示
print(A.sum())