from pygit2 import Repository, Object

repo = Repository('.')
active_branch = repo.head.shorthand
print(active_branch)

changes = repo.diff()
changed = True if changes.stats.files_changed > 0 else False
print(changed)
print('________')

commit = repo.revparse_single('HEAD')
print(commit.commit_time)