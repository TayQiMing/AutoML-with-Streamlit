# AutoML-with-Streamlit

A fork github repo for learning purpose.

<br>

Since the libraries version and python version has some problem while directly running the fork repo, I have perform some modification on the python version including the libraires version.

<br>

**Some modification i made:**
- Python==3.7         &emsp;&emsp;&emsp;    *(for pycaret casting problem at "Modeling" part)*
- altair==4.0.0       &emsp;&emsp;&emsp;    *(for v4 problem while running app.py)*
- streamlit==1.23.0   &emsp;                *(for import dataset problem)*
- Change library pandas_profiling -> ydata_profiling  &emsp;&emsp;   *(pandas_profiling no longer been used)*

<br>

Basically,
1. Create virtual environment with Python 3.7, can use conda.
2. Install the correct version of libraries

<br>

**NOTE:** <br>
The "Modeling" part has the problem of return empty data while comparing the model, maybe due to incompatible of libraries version, left it for future modification. If you have the solution for it kindly please do leave a comment below. 🥰

