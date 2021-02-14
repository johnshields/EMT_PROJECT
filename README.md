<h1 align="center">Emerging Technologies</h1>

<a href="https://www.gmit.ie/" >
<p align="center"><img src="https://i.ibb.co/f1ZQSkt/logo-gmit.png"
alt="GMIT Logo" width="500" height="200"/>
</p></a>

## Project Details
| **Project Title** | Machine Learning Web Service |
| :------------- |:-------------|
| **Course**              | BSc (Hons) in Software Development |
| **Module**              | Emerging Technologies |
| **Institute**           | [Galway-Mayo Institute of Technology](https://www.gmit.ie/) |
| **Student**            | [John Shields](https://github.com/johnshields) |
| **Module Lecturer**     | Ian McLoughlin |

***
# Project Description 
A Flask Web Service that uses Machine Learning to make predictions based of a Power Production of a Wind Turbine Data Set.

# Run the Project
## How to run the Jupyter Notebook:
### From Github
View the Jupyter Notebook [HERE](https://github.com/johnshields/ML-Web-Service/blob/main/project_files/train_model/train_model.ipynb). All the cells should run automatically.
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
Open the repository directory in Command-Line and enter:
```cmd
$ cd project_files\web_service
$ docker build . -t model_playground
$ docker run -d -p 5000:5000 model_playground
```
***
View the Wiki [HERE](https://github.com/johnshields/ML-Web-Service/wiki) for more detail.
