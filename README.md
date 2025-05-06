# Supply Chain Extra Credit Module

This project was created for Engineering the Supply Chain course (Spring 2025) at the USF. 

Core Techniques used:

- **📈 Weighted Moving Average (WMA) Forecasting** – implemented from scratch using NumPy  
- **🔧 Production & Inventory Planning** – formulated using Linear Programming via PuLP

---

## Module Features

- Two custom Python classes:
  - `WMAForecaster`: Calculates forecasts using Weighted Moving Average
  - `ProductionPlanner`: Minimizes total cost while meeting demand and capacity constraints
- Scalable: Works with any number of time periods
- Data-driven: Reads input from a CSV file (`data/red_tomato_demand.csv`)
- Output includes forecast values, error metrics, optimal production and inventory plans

---

## 🗂️ File Structure

```
supply-chain-planning-module/
├── production_planner.py        # Linear Programming model
├── wma_forecaster.py            # WMA forecasting logic
├── main.py                      # Runs the full module
├── data/
│   └── red_tomato_demand.csv    # Monthly input data (12 months)
├── requirements.txt             # Python dependencies
└── README.md                    # Project description
```

---

## ▶️ How to Run the Module

### 1. Install required libraries
```bash
pip install -r requirements.txt
```

### 2. Run the script
```bash
python main.py
```

The script will:
- Forecast demand using WMA
- Solve a production planning LP model
- Print total cost, production plan, inventory plan, and forecasting error

---

## 📚 Data Source

The first 6 months of demand and cost data are adapted from:

> Chopra, S., & Meindl, P. (2021). *Supply Chain Management: Strategy, Planning, and Operation* (7th ed.) – Example 8-1, Red Tomato Tools.

The rest of the data was extended for scalability, as required by the assignment.

## Scalability

This module is fully scalable — it dynamically adjusts to any input size (e.g., 6 months, 12 months, 24+ months). All parameters like demand, production cost, holding cost, and capacity are read from external CSV files, ensuring the module is generic and adaptable to real-world variations in planning horizons.
