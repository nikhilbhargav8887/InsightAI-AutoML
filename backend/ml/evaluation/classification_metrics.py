from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_auc_score
)


class ClassificationMetrics:

    @staticmethod
    def evaluate(y_test, predictions):

        metrics = {

            "accuracy": accuracy_score(
                y_test,
                predictions
            ),

            "precision": precision_score(
                y_test,
                predictions
            ),

            "recall": recall_score(
                y_test,
                predictions
            ),

            "f1_score": f1_score(
                y_test,
                predictions
            ),

            "confusion_matrix": confusion_matrix(
                y_test,
                predictions
            ).tolist(),

            "classification_report": classification_report(
                y_test,
                predictions
            )
        }

        return metrics