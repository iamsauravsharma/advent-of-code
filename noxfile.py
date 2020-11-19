import nox
import nox_poetry

python_versions = ["3.7", "3.8", "3.9"]


@nox.session(python=python_versions)
def lint(session):
    nox_poetry.install(session, nox_poetry.WHEEL)
    nox_poetry.install(session, "flake8", "black", "isort")
    session.run("flake8")
    session.run("black", ".", "--check")
    session.run("isort", ".", "--check-only")
