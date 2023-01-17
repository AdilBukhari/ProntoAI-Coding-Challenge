from pygit2 import Repository, Object
import time
import sys

repo_name = sys.argv[1]

repo = Repository('.')
active_branch = repo.head.shorthand
print('active branch: ' + active_branch)

changes = repo.diff()
changed = True if changes.stats.files_changed > 0 else False
print('local changes: ' + str(changed))

commit = repo.revparse_single('HEAD')
time_diff = (time.time() - commit.commit_time) / 604800
if time_diff <= 1.0:
    print('recent commit: True')
else:
    print('recent commit: False')


author = str(commit.author).split()[0]
if author == 'Rufus':
    print('blame Rufus: True')
else:
    print('blame Rufus: False')