from git import Repo


def commit_changes(message="AI update"):
    repo = Repo("repo/")
    repo.git.add(A=True)
    repo.index.commit(message)