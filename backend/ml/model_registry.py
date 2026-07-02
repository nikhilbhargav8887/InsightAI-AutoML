class ModelRegistry:

    def __init__(self):

        self.models = []

    def register(self, model):

        self.models.append(model)

    def get_models(self):

        return self.models