import pulp

# ----- Example Data ------
sku_list = [f"SKU{i+1}" for i in range(10)]
item_value = [430, 220, 180, 150, 120, 90, 60, 40, 30, 20]

class_weights = [1, 2, 4]  # A:1, B:2, C:4
class_names = ['A', 'B', 'C']

n = len(sku_list)
K = 3  # Number of classes

# ----- Model ------
model = pulp.LpProblem("Optimized_ABC_Classification", pulp.LpMinimize)

# ----- Decision Variables -------
x = pulp.LpVariable.dicts("x", (range(n), range(K)), cat="Binary")

# ----- Constratints -----
# 1. Each SKU assigned to exactly one class
for i in range(n):
    model += pulp.lpSum(x[i][k] for k in range(K)) == 1

# 2. Class Value coverage
total_val = sum(item_value)
model += pulp.lpSum(x[i][0] * item_value[i] for i in range(n)) >= 0.7 * total_val  # A
model += pulp.lpSum(x[i][1] * item_value[i] for i in range(n)) >= 0.2 * total_val  # B

# ----- Objective -----
model += pulp.lpSum(x[i][k] * class_weights[k] * item_value[i]
                for i in range(n) for k in range(K))

# ------ Solve -------
status = model.solve(pulp.PULP_CBC_CMD(msg=False))

# ----- Output ------
print("Status:", pulp.LpStatus[status])
print("SKU  |  Value  | Assigned Class")
print("-" * 30)
for i in range(n):
        assigned_k = [k for k in range(K) if pulp.value(x[i][k]) > 0.5][0]
        print(f"{sku_list[i]:<5}  | {item_value[i]:5}  |  {class_names[assigned_k]}")

# Totals per class
for k in range(K):
        c_val = sum(item_value[i] for i in range(n) if pulp.value(x[i][k]) > 0.5)
        print(f"Total value for class {class_names[k]}: {c_val}")