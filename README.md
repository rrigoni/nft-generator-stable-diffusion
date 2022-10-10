Using Stable Diffusion DreamStudio API in a Python Script
If you prefer calling the API in a Python script on your local machine or on a cloud VM server, here are the steps:

Make sure you have Python 3 or above installed on your machine and you can run it from the command line.

```
python -v
```


Install Stable Diffusion Python SDK/module

```
pip install stability-sdk
```

Install *libmagic1*

On Ubuntu
```
apt-get install libmagic1
```
On Windows

```
pip install python-libmagic
```

Install dot env
```
pip install dotenv python-dotenv
```

In .env, change `STABLE_DIFFUSION_API_KEY=your-stable-diffusion-api-key` 

Tweak your input parameters in `src/resources`. Parameters that can be tweaked are:
```
-actions
-background
-details
-objects
-styles
```

You can also change how many parameters can be used in each prompt
```
NUMBER_OF_OBJECTS = 2
NUMBER_OF_STYLES = 2
NUMBER_OF_BACKGROUNDS = 1
NUMBER_OF_ACTIONS = 2
NUMBER_OF_DETAILS = 3
```

Run the application with 
```python3 run.py```

