# LocalLLM
Implementing a Python AI chatbot. 

## Languages:
Python

## Features:
Because this chatbot will run locally we do not have to pay for the subscription or connect to "Open AIs"

### Steps
* 1st: Download [ollama](https://ollama.com/)</br>
This is what we use to run our LLM locally on our machine.</br>
It is a software that allows us to download & run open source LLMs.</br>
The larger the model, the more difficult it is to run it on our machine in terms of the type of hardware we need.</br>
after installation to check if it is installed correctly open the command prompt and type "ollama" If it is installed, it should show the details.</br></br>

* 2nd: Install the model(Llama 3.1) that you need from [ollama](https://github.com/ollama/ollama) with 8B Parameters, on our computer with this command:</br>
~~~
ollama pull llama3.1
~~~

* 3rd: Run the model with this command</br>
~~~
ollama run llama3
~~~

* 4th: Create a virtual environment, here we will install a few dependencies that we need for this project. means some isolated dependencies inside.</br>
for this reason, I opened this folder in "Visual Studio Code", and then typed this command.</br>
~~~
python -m venv chatbot
~~~
</br> Because I am on Windows I wrote Python if it was Mac or Linux I would write python3</br>
according to "img1" you can see that the "Chatbot" directory has been created.</br></br>

* 5th: Activate the Virtual environment then install our packages.</br>
#this command activates it on my Windows machine
~~~
.\chatbot\Scripts\Activate.ps1
~~~         
  + On some other Windows machine maybe this command works:
~~~
.\chatbot\Scripts\activate.bat or .\venv\Scripts\activate.bat
~~~
  + on Mac or Linux:
~~~
source chatbot/bin/activate
~~~

* 6th: Install the packages that we need:</br>
~~~
pip install langchain langchain-ollama ollama </br>
~~~
* 7th: create a python file: main.py</br>

* 8th: inside it write this codes:
~~~
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3")

result = model.invoke(input="hello world")
print(result)
~~~

you will see if you execute it you will see the result.
* 
* 



