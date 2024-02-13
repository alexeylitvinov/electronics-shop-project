class InstantiateCSVError:
    def __init__(self, message='InstantiateCSVError: Файл item.csv поврежден'):
        self.message = message
        raise Exception(self.message)
