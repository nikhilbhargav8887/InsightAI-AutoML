class AutoMLEngine:

    def __init__(self):

        self.models = []

    def register_model(self, model):

        self.models.append(model)

    def get_models(self):

        return self.models