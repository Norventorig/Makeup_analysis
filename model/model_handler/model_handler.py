import numpy as np
from PIL.JpegImagePlugin import JpegImageFile


class ModelHandler:
    def __init__(self, labels, model):
        self.model = model
        self.labels = labels

    def prepare_data(self, x):
        x = x.resize((228, 228))
        x = np.array(x)
        x = x.reshape((1, 228, 228, 3))

        return x

    def predict(self, x: JpegImageFile):
        res = 'error'

        try:
            x = self.prepare_data(x=x)

        except Exception as e:
            print("\nВОЗНИКЛА ОШИБКА НА ЭТАПЕ ОБРАБОТКИ ИЗОБРАЖЕНИЯ", e)

        else:
            pred = self.model.predict(x)
            pred = int(pred[0, 0])
            res = self.labels[pred]

        finally:
            return res
