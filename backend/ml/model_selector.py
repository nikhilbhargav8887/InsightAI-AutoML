class ModelSelector:

    @staticmethod
    def get_best_model(results):

        best_model = max(
            results,
            key=lambda model: results[model]["accuracy"]
        )

        return best_model