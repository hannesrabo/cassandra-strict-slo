# Cassandra Strict SLO 

In this project we create a virtual network of cassandra instances to benchmark them. The goals is to perform smart request duplications to increase chanses of meeting strict latency guarantees.

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