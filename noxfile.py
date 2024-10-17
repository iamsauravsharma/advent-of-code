from nox_poetry import session
from nox_poetry.sessions import Session

python_versions = ["3.9", "3.10", "3.11", "3.12", "3.13"]


@session(python=python_versions)
def lint(session: Session):
    session.install("ruff", "safety", "pytest", ".")
    session.run("ruff", "check", ".")
    session.run("ruff", "format", ".", "--check")
    requirements_file = session.poetry.export_requirements()
    session.run("safety", "check", "-r", str(requirements_file))
    session.run("pytest")
