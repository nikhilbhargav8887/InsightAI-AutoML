from backend.ml.preprocessing.preprocessor import DataPreprocessor
from backend.ml.preprocessing.feature_splitter import FeatureSplitter
from backend.ml.preprocessing.splitter import TrainTestSplitter
from backend.ml.classification.random_forest import RandomForestModel
from backend.ml.evaluation.classification_metrics import ClassificationMetrics
from backend.ml.utils.model_saver import ModelSaver
from backend.ml.utils.model_loader import ModelLoader


# Step 1: Load and preprocess data
preprocessor = DataPreprocessor(
    "datasets/raw/customer_churn.csv"
)

preprocessor.load_data()
preprocessor.remove_duplicates()
preprocessor.fill_missing_values()
preprocessor.encode_categorical_columns()

df = preprocessor.get_dataframe()


# Step 2: Split features and target
feature_splitter = FeatureSplitter(
    dataframe=df,
    target_column="Churn"
)

X, y = feature_splitter.split()


# Step 3: Train/Test split
splitter = TrainTestSplitter(X, y)

X_train, X_test, y_train, y_test = splitter.split()


# Step 4: Train Random Forest
model = RandomForestModel()

model.train(X_train, y_train)


# Step 5: Predict
predictions = model.predict(X_test)

metrics = ClassificationMetrics.evaluate(
    y_test,
    predictions
)

print("\n===== Random Forest Evaluation =====\n")

print(f"Accuracy      : {metrics['accuracy']:.4f}")
print(f"Precision     : {metrics['precision']:.4f}")
print(f"Recall        : {metrics['recall']:.4f}")
print(f"F1 Score      : {metrics['f1_score']:.4f}")

print("\nConfusion Matrix:")
print(metrics["confusion_matrix"])

print("\nClassification Report:")
print(metrics["classification_report"])




print("\nSaving model...")

ModelSaver.save(
    model.get_model(),
    "random_forest.pkl"
)

print("Model saved successfully!")

loaded_model = ModelLoader.load(
    "random_forest.pkl"
)

print("Model loaded successfully!")

predictions = loaded_model.predict(X_test)

print("\nLoaded model predictions:")
print(predictions[:10])