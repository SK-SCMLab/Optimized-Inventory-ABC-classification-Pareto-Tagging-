# 🥍 Optimized-Inventory-ABC-classification-Pareto-Tagging-
This repository represents an intelligent inventory segmentation using Python + CPLEX optimizer

--- 

## 🏓 Overview
This project implements a **Mixed-Integer Linear Programming (MILP) optimizer** in Python to automate the ABC classification of inventory items (SKUs) using the Pareto principle, business targets, and cost efficiency criteria.

**Objective**: Assign each SKU to A, B, or C classes so that:
- Class A covers ≥ 70% of value
- Class B covers ≥ 20% of value
- Each item is tagged to only one class
- Total expected holding cost (or other business metric) is minimized

**Use cases**
- Supply Chain analytics
- Inventory Management
- Portfolio demonstration for OR/Optimization skills

---

## ⛳️ Data & Model
- **Inputs**
   - SKU IDs
   - Value or Annual usage for each
   - (Optional) Class-specific holding cost multipliers
- **Variables**
   - 'x[i][k]': Binary assignment - 1 iff SKU 'i' assigned class 'k' ('A=0, B=1, C=2')
- **Constraints**
   - Each SKU assigned to one class only
   - Class coverage targets (A≥70%, B≥20% of total value)
- **Objective**
   - Minimize: Weighted sum of inventory values * class risk multiplier

---

## 🎣 Technologies used
- Python 13 > PuLP library > DOcplex
- Visual Code Studio
- ChatGPT & Perplexity

## 🛹Requirements
- Inventory Management
- Knowledge of Prompt Engineering
- Basics of Coding
- Linear Programming



