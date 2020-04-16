# Cassandra Strict SLO 

In this project we create a virtual network of cassandra instances to benchmark them. The goal is to perform smart request duplications to increase the chance of meeting strict latency guarantees.

The modified version of the cassandra driver was implemented in the benchmark tool YCSB. This code is available here: [https://github.com/hannesrabo/YCSB](https://github.com/hannesrabo/YCSB)

Starting the topology can be done by running the following command in the root folder of the repo:

```sh
> sudo ./pttopology
```

# Developing
> This has only been tested in ubuntu

To setup dev environment in run:

```sh
> ./tools/installdev.sh
```

This will install python, pip and virtual env. It will also create a `venv` for the use in the project called `env-slo`.

To activate the virtual environment run:

```sh
> source env-slo/bin/activate
```

This should change the prompt to include the word `env-slo` if you are using any kind of fancy terminal.

To deactivate the environment run:

```sh
> deactivate
```

# Running in vs code
If you are running in vs code you may add these lines to `.vscode/settings.json`

```json
{
    "python.pythonPath": "env-slo/bin/python",
    "python.linting.pep8Enabled": true,
    "python.linting.pylintEnabled": true,
    "editor.formatOnSave": true
}
```
