class ModelComparison:

    def __init__(self):
        self.results = []

    def add_result(
        self,
        model_name,
        accuracy,
        precision,
        recall,
        f1_score
    ):

        self.results.append({

            "Model": model_name,

            "Accuracy": accuracy,

            "Precision": precision,

            "Recall": recall,

            "F1 Score": f1_score
        })

    def get_results(self):

        return sorted(
            self.results,
            key=lambda x: x["Accuracy"],
            reverse=True
        )

    def get_best_model(self):

        return self.get_results()[0]