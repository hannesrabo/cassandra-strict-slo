# Git

This describes the workflow when working with git and the repo.

## Setup

- Fork the repo
- Download fork
- `git remote set-url upstream git@github.com:the_repo`
- run: `tools/install-dev.sh`
- verify that you are in the right environment (“which python” should be located in local repo)

## Adding a new feature in git

- `git fetch upstream && git reset --hard upstream/master`
- `git checkout -b my-feature-branch`
- work:  (may occur many times): 
  `git add . && git commit -m “my message”`
- adding: `git fetch upstream`
  - `git rebase upstream/master`
  - `git push (git push --set-upstream origin my-feature-branch)`
- Create PR
  - If there is an issue related to the PR, write: `fixes <copied link to issue>` in the description of the PR. This will make sure the issue is closed when the PR is merged. It does work to refer to PRs in comments but this does not close them.
- Review PR yourself
- Add comments to things that might be non-obvious
- Add fixes you discovered during self-review
- Share the PR with the rest of the group.
- After the PR is approved, use "squash and merge" this hides internal small commits and merges in the master branch.

## General guidelines for PRs

- Try to keep every PR strictly related to a single problem.
- Try to keep PRs under 500 lines.

## Review guidelines

- Never assume that a change is wrong. The goal is to make the author aware of things for them to correct them.

- Work comments as questions to the author. This looks nicer to the person getting the "critique".

  - Do not write: 

    > "This is probably wrong. You should have used this library", or
    >
    > "This variable should be called x"

  - Do write: 
  
    > "Have you seen this library as well?", or 
    >
    > "Do you think we could make this variable name a bit clearer?"