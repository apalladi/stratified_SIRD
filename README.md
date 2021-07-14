# SIR derived models
In this repository you can run epidemiological simulations using three different models, namely:
- SIR model
- SIRD model
- age stratified SIRD model

In order to install the repository on your local machine, please run:
`git clone https://github.com/apalladi/stratified_SIRD.git`

Then you can create create a Conde environment running:
`conda env create -f environment.yml`

Now you are ready to run the examples contained in the Notebook. 
In SIR-example.ipynb there is a simple example that uses the basic SIR model. 
You just need to import the SIR model typing 
```from src.simple_models import SIR``` 
Then you can specify the model parameters, that for the basic SIR are the population (N), beta and gamma, as described in the Notebook. 
