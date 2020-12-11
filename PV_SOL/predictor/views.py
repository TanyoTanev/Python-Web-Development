from django.shortcuts import render

# Create your views here.
from predictor.apps import PredictorConfig
import matplotlib.pyplot as plt
from io import StringIO

from pv_plants_app.forms import ForecastForm


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
    return render(request, 'forecast.html', context={'result': result,})



def get_n_days(request):
    prediction_form = ForecastForm()
    context = {}
    if request.method == 'POST':
        prediction_form = ForecastForm(request.POST)
        #if prediction_form.is_valid():
        beggining = int(prediction_form.data['number_of_days'])
        #beggining = int(beggining)
        if beggining is None:
                beggining = 2

        graph = forecast_graph(request, beggining)

        context = {
                  'graph': graph,
                  'prediction_form': prediction_form
                    }
        return render(request, 'forecast.html', context)
 #       return render(request, 'forecast_graph.html', context)
    else: # request.method == 'GET':
        prediction_form = ForecastForm(request.GET)
        return render(request, 'forecast.html', context)



def forecast_graph(request, beggining):


    Y = PredictorConfig.data['PV_y_test']
    Y_predicted = get_predictions()
    end = len(Y)
    #beggining = 11
    plt_period_begginig = end - beggining*288

    plt.figure()
    #plt.figure(figsize=(20,10))
    plt.rcParams.update({'font.size': 8}) # must set in top

    plt.title(f"Power generation comparison between measured and predicted values")
    plt.plot(Y[plt_period_begginig:end].index, Y_predicted[plt_period_begginig:end], label = f"Predicted generation")
    plt.plot(Y[plt_period_begginig:end].index, Y[plt_period_begginig:end], label = "Real generation")
    plt.legend(loc="upper left")
    plt.xlabel("Measurements, 5 min")
    plt.ylabel("Generated power, W")

    fig = plt.gcf()
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    graph = imgdata.getvalue()
    return graph

    #context = {
    #    'graph': graph
    #        }
    #return render(request, 'forecast_graph.html', context)
