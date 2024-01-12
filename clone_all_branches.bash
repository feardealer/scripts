#!/usr/bin/env bash

init_branch=$(git branch --list \
            | grep '*' \
            | cut -d' ' -f2 \
            | sed 's|.*/||')

branches=$(git branch -a \
         | grep -v -e '*' -v -e "HEAD" \
         | sed 's|.*/||')

for branch in $branches; do
  git checkout $branch
  mkdir -p .github/workflows/
  cat <<'END' > .github/workflows/mirroring.yml
name: GitlabSync

on:
  - push
  - delete

jobs:
  sync:
    runs-on: ubuntu-latest
    name: Git Repo Sync
    steps:
    - uses: actions/checkout@v2
      with:
        fetch-depth: 0
    - uses: wangchucheng/git-repo-sync@v0.1.0
      with:
        target-url: ${{ secrets.GITLAB_URL }}
        target-username: ${{ secrets.GITLAB_USERNAME }}
        target-token: ${{ secrets.GITLAB_TOKEN }}
END
  git add .github/workflows/mirroring.yml
  git commit -m 'add mirroring ci'
done

git checkout $init_branch
