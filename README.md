# Statistical AI-Agent

## Description

This is an AI-Agent built with [OpenAI SDK](https://developers.openai.com/api/docs/libraries) using the router of [Openrouter](https://openrouter.ai/). It can perform basic statistical operations on the datasets saved locally in the form of `.csv` files. The agent API is written in Python3, as well as the tools the agent can use. Those tools rely on a shared library implemented in C and exposed to Python via [ctypes](https://docs.python.org/3/library/ctypes.html).

## How to install and run the project - Linux, Mac, Windows

1. Download the content of this project inside an empty directory, we will refer to this directory with the name *root*. Every command you see will be run from the root directory.
2. Build the shared library with the commands
```bash
cmake -B build
cmake --build build
```
Of course you need [cmake](https://cmake.org/). You could find helpful this [guide](https://linuxvox.com/blog/how-to-install-cmake-on-linux/) to install it. Check the **Requirements** section too.

3. Get a key on [Openrouter](https://openrouter.ai/)
    - Create the file `.env` in the root. If you have Linux or Mac you can use the command
    ```bash
    touch .env
    ```
    If you are on Windows use 
    ```powershell
    New-Item .env
    ```
    - Edit `.env` and write on it `OPENROUTER_API_KEY="*"`
    - Make an account on [Openrouter](https://openrouter.ai/).
    - Go to Personal/Profile/API Keys.
    - Click "+ New Key".
    - Set the parameters as you like. I've always run the program with credit limit = 0.
    - Copy the key and paste it into the file `.env` in place of the `*`.
Say that your key is `1234`, your `.env` file should now contain
```
OPENROUTER_API_KEY="1234"
```
4. Install python requirements. You can do this in 2 ways:
    - You can install manually every dependancy.
        - On Linux or Mac run
        ```bash
        pip3 install openai
        pip3 install python-dotenv
        ```
        - On Windows run
        ```powershell
        python3 -m pip install openai
        python3 -m pip install python-dotenv
        ```
    - You can use [uv](https://docs.astral.sh/uv/) (follow the instruction on the website to install it) and run the command
    ```bash
    uv sync
    ```
5. If you are running all of this from Mac or Windows there is still an issue to fix: open the file `python_API/C_lib_API.py` and edit line 5. Replace it with the following
    - Mac:
    ```python
    shared_lib_path: str = os.path.join(root_file_path, "build/libStatFuncs.dylib")
    ```
    - Windows: 
    ```python
    shared_lib_path: str = os.path.join(root_file_path, "build/libStatFuncs.dll")
    ```
6. Run the command
```bash
python3 main.py "Perform an analisys of the dataset house_prices.csv"
```
Or, if you used [uv](https://docs.astral.sh/uv/), use
```bash
uv run main.py "Perform an analisys of the dataset house_prices.csv"
```

It should print on screen a list of tool calling and then an answer

### How to use

run the command
```bash
python3 main.py <prompt>
```
and replace \<prompt> with your actual prompt between quotes. Fantasy is the limit.
You may add the flag `--verbose` to have more information about the tool calling, parameters used and answers given to the AI-Agent.
The agent can access any CSV file in `data/small_data` and `data/big_data`. At the moment of download there is only `data/small_data/house_prices.csv`, but you can add as many tables as you want. Make sure to name them with the final `.csv` extension.
You can find a lot of CSV tables on [kaggle](https://www.kaggle.com/)

## Requirements

Those are the version I used. The project could work with lower versions, but I don't guarantee
- cmake: 3.23
- gcc: 13.3.0
- python: 3.13.13
- openai: 2.44.0
- python-dotenv: 1.1.0

## What (and where) I learned

This project was a ton of fun. I used everything I learned in the last 3 months and I built something that no one thaught me. The creative process started with this thought: I want to write something in C and make Python use it. That was my goal.
Here's a list of websites I found very useful during development

- [Boot.dev](https://www.boot.dev/) code learning platform.
- [Cmake Tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/index.html) this tutorial is extremely helpful and easy to follow. This project could not be done without it.
- [csv](https://docs.python.org/3/library/csv.html) python library to read CSV tables.
- [ctypes](https://docs.python.org/it/3.14/library/ctypes.html#module-ctypes) python library to use shared library.
- [json schema](https://json-schema.org/) where I learned about complex json schema for tool calling.
- [json validator](https://www.jsonschemavalidator.net/) helpful json schema / data  validator
- [kaggle](https://www.kaggle.com) among many other things, this website has tons of tables
