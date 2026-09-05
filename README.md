# Statistical AI-Agent

## Description

This is an AI-Agent built with [OpenAI SDK](https://developers.openai.com/api/docs/libraries) using the router of [Openrouter](https://openrouter.ai/). It can perform basic statistical operations on the datasets saved locally in the form of `.csv` files. The agent API is written in Python3, as well as the tools the agent can use. Those tools rely on a shared library implemented in C and exposed to Python via [ctypes](https://docs.python.org/3/library/ctypes.html).

## How to install and run the project - Linux

1. Download the content of this project inside an empty directory, we will refer to this directory with the name *root*. Every command you see will be run from the root directory.
2. Build the shared library with the commands
```bash
cmake -B build
cmake --build build
```
Of course you need [cmake](https://cmake.org/). You could find helpful this [guide](https://linuxvox.com/blog/how-to-install-cmake-on-linux/) to install it. Check the **Requirements** section too.

3. Get a key on [Openrouter](https://openrouter.ai/)
    - Create the file `.env` in the root with the command
    ```bash
    touch .env
    ```
    - Edit `.env` and write on it `OPENROUTER_API_KEY="*"`
    - Make an account on [Openrouter](https://openrouter.ai/).
    - Go to Profile/API Keys.
    - Click "+ New Key".
    - Set the parameters as you like. I've always run the program with credit limit = 0.
    - Copy the key and paste it into the file `.env` in place of the `*`.
Say that your key is `1234`, your `.env` file should now contain
```
OPENROUTER_API_KEY="1234"
```
4. Run the command
```bash
python3 main.py "Give me an overview of the dataset house:prices.csv"
```

It should print on screen an answer
