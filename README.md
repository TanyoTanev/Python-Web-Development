# Python-Web-Development
Project for the SoftUni course Python Web Development

This project is prepared for the projet defence of the SoftUni Python Web Development course. It represents a company that offers forecast-as-a-service for photovoltaic power plants.
The PV PP generation is very instable and not possible to schedulize. The PV PP have to present their expectations of what they will produce in the next days to the power grid 
operators. If the pridiction are not accurate, the grid operators should compensate the imbalance with fast-changing power plants, like water or gas PP. This is needed due to the
fact that the generation of electricity in the grid and the consumption should be in balance in every moment. The additional measures to balance this equation are additional investments.
At the moment, the available prediction methods required a lot of electrical related parameters, which takes a lot of resources, it is very difficult to make an accurate predictor
and is considerably slow in calculation terms.
The model, prepared in Machine Learning course of the Artificial Intelligence module of SoftUni, based on regression methods gives 0.973~0.993 accuracy with fast computation time.
This model was named as number 1 in the class. It is pickled, and added as a functionality in the project.
A user of the site can register himself, add a PV Plant, update, read, or delete it. Also, can use the forecast functionality represented by the forecast button.
In real project the real data of each power plant should be supplied to the model. In this case we are using the experimental data with which the model was trained, tuned for hyper
parameters, and finaly tested. In this case the user sees the results of the model supplied with the test data, which represents the real data from his power plant.
