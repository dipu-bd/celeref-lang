# celeref-lang

A versatile interpreter in python to execute programs written in JSON.

## Installation

First you need to install python 3. Now you can install the package via pip:

```sh
$ python -m pip install --user -U celeref-lang
# In linux, you might have to use `python3` instead.
# Make sure to check `python --version` first.
```

Test if it is installed successfully:

```sh
$ celeref
# It should print a help message

$ celeref --version
# It should print the installed version
```

If it says `celeref` is not found, follow this help:

- [Windows](https://stackoverflow.com/a/44437176/1583052)
- [Linux](https://stackoverflow.com/a/51799221/1583052)
- [MacOS](https://itsevans.com/install-pip-osx/)

## Writing your first program

You need a code-editor that supports intellisense for JSON schema. My preference is Visual Studio Code.

- Create a JSON file in Visual Studio Code
- Add the schema path located in `src/schema` folder.
  See examples in `examples` folder for help.

With schema defined, editor will catch schema errors and auto-suggest available expressions.

Here is a sample program written in celeref-lang:

```json
{
  "$schema": "https://raw.githubusercontent.com/dipu-bd/celeref-lang/master/src/schema/schema.json",
  "name": "Hello World",
  "program": [
    {
      "state": "Hello World"
    },
    {
      "print": "state"
    }
  ]
}
```

Save the program to `hello-world.json` file, and run it using:

```sh
$ celeref hello-world.json
----------
Hello World

------ 0.000 seconds ------
```

## Building from source

You need Python 3 to execute this script.

- Clone the repository first
- Create a new virtual environment
  - `python -m venv venv`
- Activate it;
  - In Windows: `venv\Scripts\activate`
  - In Linux: `venv/bin/activate`
  - In MacOS: `venv/bin/activate`
- Now install dependencies:
  - `pip install -U wheel pip`
  - `pip install -r requirements.txt`
- Now to run the script:
  - `python src <path/to/your-source.json>`

E.g. To run the `hello-world.json` example:

```sh
$ python src examples/hello-world.json
Hello World
```

## Documentation

This project in under development. APIs are subjected to change in future.
Documentation is further away. Follow schema descriptions for basic documentation for now.

To note a few basic things:

- `state` is a very important variable in this program. After executing a statement,
  the result is always stored in state first.

- After program has finished running the final value of `state` will be the result.

- To pass and array or objects as arguments to `call` method,
  you can use `{ "state": <your array or object> }`.

- To display a list of all available functions:

```sh
$ celeref -s
```

- To search for specific functions, pass a query after `-s`:

```sh
$ celeref -s mod
----- [divmod] -----
Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.

----- [math.fmod] -----
Return fmod(x, y), according to platform C.

x % y may differ.

----- [math.modf] -----
Return the fractional and integer parts of x.

Both results carry the sign of x and are floats.

----- [op.mod] -----
mod(a, b) -> number
Same as `a % b`

Find the modulus of two numbers

```
