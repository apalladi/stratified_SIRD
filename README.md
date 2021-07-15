# Models derived from SIR
In this repository you can run epidemiological simulations using three different models, namely:
- SIR model
- SIRD model
- age stratified SIRD model

In order to install the repository on your local machine, please run:
`git clone https://github.com/apalladi/stratified_SIRD.git`

Then you can create create a Conde environment running:
`conda env create -f environment.yml`

# Examples
Now you are ready to run the examples contained in the Notebook. 
In SIR-example.ipynb there is a simple example that uses the basic SIR model. 
You just need to import the SIR model typing 
```from src.simple_models import SIR``` 
Then you can specify the model parameters, that for the basic SIR are the population (N), beta and gamma, as described in the Notebook. 

The Notebook ```stratified_SIR-validations.ipynb``` uses the stratified SIR to model the 2nd wave of Covid19, that occured in Italy between the end of 2020 and the beginning of 2021. 

The Notebook ```stratified_SIR-validations.ipynb``` uses the stratified SIR to make predictions on the mortality that could happen in case of a new wave at the end of 2021. In order to do that, we use the optimal parameters found in the validation Notebook and we add vaccinations. In the example, the vaccinations do not stop the transmission but they prevent the sever form of the illness, reducing the fatality rate.  


