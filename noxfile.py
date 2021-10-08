import nox_poetry
from nox_poetry.sessions import Session

python_versions = ["3.7", "3.8", "3.9", "3.10"]


@nox_poetry.session(python=python_versions)
def lint(session: Session):
    session.install("flake8", "black", "isort", "safety", "pytest", ".")
    session.run("flake8")
    session.run("black", ".", "--check")
    session.run("isort", ".", "--check-only")
    requirements_file = session.poetry.export_requirements()
    session.run("safety", "check", "-r", str(requirements_file))
    session.run("pytest")
