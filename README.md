# Add, Commit, Push
This repository is for my acp project. I included the .bashrc needed to use the aliases for the project. Do note that the directories are specific to my machine so you'll have to edit them to make the aliases work properly.
## Usage

```bash
python add-commit-push.py
python add-commit-push.py -m "commit message"
python add-commit-push.py -f
python add-commit-push.py -m "commit message" -f
```
### Flags

| Flag | Description |
|------|-------------|
| `-m MESSAGE` | Set the commit message. Defaults to `"Updated files"` if not provided. |
| `-f` | Force mode. Skips the confirmation prompt and executes immediately. |

## Sprint 5 directory shortcut
```
alias g5='cd /home/john/Desktop/school/intro-to-cs/sprint-5/'
```
## Add, commit, push shortcut
```
alias acp='python /home/john/Desktop/school/intro-to-cs/sprint-5/add-commit-push.py'
```
