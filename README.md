# celeref-lang

A versatile interpreter in python to execute programs written in JSON.

## Writing new program

You need a code-editor that supports intellisense for JSON schema. My preference is Visual Studio Code.

Create a JSON file in Visual Studio Code. And add the schema path located in `src/schema` folder.
See examples in `examples` folder for help.

With schema defined, editor will catch schema errors and auto-suggest available expressions.

Here is a sample program written in it:

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

## Executing a script

You need Python 3 to execute this script.

- First create a new virtual environment
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
- Below are list of public function available to use with `call`.
  All these method are ported directly from [python built-ins](https://docs.python.org/3/library/functions.html).
  See the docs there for documentation.

```txt
    abs         all         any         ascii       bin         breakpoint      chr
    dir         divmod      enumerate   filter      float       format          hash
    hex         input       int         iter        len         license         list
    map         max         min         next        oct         ord             pow
    print       quit        range       repr        reversed    round           set
    sorted      str         sum         tuple       type        zip
```
