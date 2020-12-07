from django.shortcuts import render

# Create your views here.
from predictor.apps import PredictorConfig


def get_predictions():
    pv_reg = PredictorConfig.data['pv_reg']
    PV_features_train = PredictorConfig.data['PV_features_train']
    PV_y_train = PredictorConfig.data['PV_y_train']
    PV_features_test = PredictorConfig.data['PV_features_test']
    PV_y_test = PredictorConfig.data['PV_y_test']

    prediction = pv_reg.predict(PV_features_test)

    return prediction

def forecast_result(request):

    result = get_predictions()
    return render(request, 'forecast.html', context={'result': result})
