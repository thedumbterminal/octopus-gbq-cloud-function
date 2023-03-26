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


@task(lint)
def ci(c):
    pass
