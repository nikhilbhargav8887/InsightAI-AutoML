import pandas as pd

from backend.ml.utils.problem_detector import detect_problem


df = pd.read_csv("backend/ml/classification_sample.csv")

problem = detect_problem(df, "Salary")

print(problem)