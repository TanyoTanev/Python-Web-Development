from django.apps import AppConfig
from django.conf import settings
import os
import pickle
class PredictorConfig(AppConfig):
    # create path to models
    path = os.path.join(settings.MODELS, 'models.p')
    name = 'predictor'

    # load models into separate variables
    # these will be accessible via this class
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    pv_reg = data['pv_reg']
    PV_features_train = data['PV_features_train']
    PV_y_train = data['PV_y_train']
    PV_features_test = data['PV_features_test']
    PV_y_test = data['PV_y_test']

