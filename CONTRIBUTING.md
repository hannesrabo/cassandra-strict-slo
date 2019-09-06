# Git

This describes the workflow when working with git and the repo. This may be up to debate if there are any suggestions. It is nice with continuous improvements.

## Setup

- Fork the repo
- Download fork
- `git remote set-url upstream git@github.com:the_repo`
- run: `tools/install-dev.sh`
- verify that you are in the right environment (“which python” should be located in local repo)

## Adding a new feature in git

- `git fetch upstream && git reset --hard upstream/master`.
- `git checkout -b my-feature-branch`.
- work:  (may occur many times): 
  `git add . && git commit -m “my message”`.
- adding: `git fetch upstream`.
  - `git rebase upstream/master`.
  - `git push (git push --set-upstream origin my-feature-branch)`.
- Create PR.
  - If there is an issue related to the PR, write: `fixes <copied link to issue>` in the description of the PR. This will make sure the issue is closed when the PR is merged. It does work to refer to PRs in comments but this does not close them.
  - Name the PR in a way that makes sense. Start with the general area and then a sentence that describes what it adds: `docs: Adds new documentation for installing python`. The name of the PR will propagate to the commit message when it is merged.
- Review PR yourself. There are usually some error that you can discover when reading a diff log.
- Add comments to things that might be non-obvious.
- Add fixes you discovered during self-review.
- Share the PR with the rest of the group.
- After the PR is approved, use "squash and merge". This hides internal small commits and merges in the master branch.
- Delete the branch on github, then delete the branch locally: `git branch -d my-feature-branch`.

## General guidelines for PRs

- Try to keep every PR strictly related to a single problem.
- Try to keep PRs under 500 lines.
- Naming scheme is `area of affect` : `Active form sentence of what is added`. Example: `build: Adds new build script for mac os.`.

## Review guidelines

- Never assume that a change is wrong. The goal is to make the author aware of things for them to correct them.
- The experience should be "wholesome".
- Work comments as questions to the author. This looks nicer to the person getting the "critique".

  - Do not write: 

    > "This is probably wrong. You should have used this library", or
    >
    > "This variable should be called x"

  - Do write: 
  
    > "Have you seen this library as well?", or 
    >
    > "Do you think we could make this variable name a bit clearer?"