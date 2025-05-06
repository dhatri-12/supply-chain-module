import pandas as pd
from production_planner import ProductionPlanner
from wma_forecaster import WMAForecaster

# === Step 1: Load data ===
df = pd.read_csv("./data/red_tomato_demand.csv")

# Extract input vectors
demand = df["Demand"].tolist()
prod_cost = df["Prod_Cost"].tolist()
hold_cost = df["Hold_Cost"].tolist()
capacity = df["Max_Capacity"].tolist()

# === Step 2: Apply Weighted Moving Average ===
print("🔍 Weighted Moving Average Forecasting:")

weights = [0.5, 0.3, 0.2]  # Example: 3-period WMA
wma_model = WMAForecaster(weights=weights)
forecasted = wma_model.forecast(demand)

# Print results
print("Forecasted Demand:", forecasted)
actual = demand[len(demand) - len(forecasted):]
mae = wma_model.evaluate(actual, forecasted)
print("MAE (Mean Absolute Error):", mae)

# === Step 3: Production Planning Optimization ===
print("\n⚙️ Production & Inventory Planning:")

planner = ProductionPlanner(
    demand=demand,
    prod_cost=prod_cost,
    hold_cost=hold_cost,
    capacity=capacity,
    initial_inventory=0
)
planner.build_model()
result = planner.solve()

# Print results
print("Status:", result["Status"])
print("Total Cost:", result["Total Cost"])
print("Production Plan:", result["Production Plan"])
print("Inventory Plan:", result["Inventory Plan"])
