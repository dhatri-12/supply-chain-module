import pandas as pd
import pulp

class ProductionPlanner:
    def __init__(self, demand, prod_cost, hold_cost, capacity, initial_inventory=0):
        self.periods = list(range(len(demand)))
        self.demand = demand
        self.prod_cost = prod_cost
        self.hold_cost = hold_cost
        self.capacity = capacity
        self.initial_inventory = initial_inventory
        self.model = pulp.LpProblem("Production_Planning", pulp.LpMinimize)
        self.prod_vars = {}
        self.inv_vars = {}

    def build_model(self):
        # Decision variables
        for t in self.periods:
            self.prod_vars[t] = pulp.LpVariable(f'Production_{t+1}', lowBound=0, cat='Continuous')
            self.inv_vars[t] = pulp.LpVariable(f'Inventory_{t+1}', lowBound=0, cat='Continuous')

        # Objective: minimize production + inventory cost
        self.model += pulp.lpSum(
            [self.prod_cost[t] * self.prod_vars[t] + self.hold_cost[t] * self.inv_vars[t] for t in self.periods]
        )

        # Constraints
        for t in self.periods:
            # Production capacity
            self.model += self.prod_vars[t] <= self.capacity[t], f"Capacity_Constraint_{t+1}"

            # Inventory balance
            if t == 0:
                self.model += self.prod_vars[t] + self.initial_inventory - self.demand[t] == self.inv_vars[t]
            else:
                self.model += self.prod_vars[t] + self.inv_vars[t - 1] - self.demand[t] == self.inv_vars[t]

    def solve(self):
        self.model.solve()
        status = pulp.LpStatus[self.model.status]
        result = {
            'Status': status,
            'Total Cost': pulp.value(self.model.objective),
            'Production Plan': [pulp.value(self.prod_vars[t]) for t in self.periods],
            'Inventory Plan': [pulp.value(self.inv_vars[t]) for t in self.periods]
        }
        return result
