from invoke import task


@task
def start(c):
    """
    Start the dev server
    """
    c.run("functions-framework --source ./main.py --target entry_http --debug")


@task
def format(c):
    """
    Format source files
    """
    c.run("black .")


@task
def lint(c):
    """
    Lint source files
    """
    c.run("flake8 --statistics .")


@task
def test(c):
    c.run(
        "OCTOPUS_API_KEY=x"
        " OCTOPUS_ELECTRICITY_SERIAL=x"
        " OCTOPUS_ELECTRICITY_MPAN=x"
        " OCTOPUS_GAS_SERIAL=x"
        " OCTOPUS_GAS_MPRN=x"
        " pytest . --cov"
    )


@task(lint, test)
def ci(c):
    pass
