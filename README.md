# Emerging Technologies
#### John Shields - G00348436 

A repo for the main assignment in Emerging Technologies...

# Run the Project
## How to run the Jupyter Notebook:
### From Github
View the Jupyter Notebook [here](https://github.com/johnshields/EMT_PROJECT/blob/main/project_files/train-model/train-model.ipynb). All the cells should run automatically.
***
### From Jupyter Notebook
##### Run the Jupyter Notebook:
Open the repository directory in Command-Line and enter:
```cmd
$ cd project_files\train_model
$ jupyter notebook
```
***

## How to run the Web Service:
##### Run the Web Service:
Open the repository directory in Command-Line and enter:
```cmd
$ cd project_files\web_service
$ set FLASK_APP=web_service.py && python -m flask run
```
* Running on http://127.0.0.1:5000/

##### Docker Image
```cmd
$ cd project_files\web_service
$ docker run -d -p 5000:5000 model_playground
```
***
View the wiki [here](https://github.com/johnshields/EMT_PROJECT/wiki) for more detail.
