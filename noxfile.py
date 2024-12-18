from nox import Session, session

python_versions = ["3.9", "3.10", "3.11", "3.12", "3.13"]


@session(python=python_versions)
def lint(session: Session):
    session.install("ruff", "pytest", ".")
    session.run("ruff", "check", ".")
    session.run("ruff", "format", ".", "--check")
    session.run("pytest")
