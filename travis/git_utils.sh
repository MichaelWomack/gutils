#!/usr/bin/env bash

function configure() {
    echo "Entering configure()"
    git config credential.helper "store --file=.git/credentials"
    echo "https://${GH_TOKEN}:@github.com" > .git/credentials

    git config --global user.email 'travis@travis-ci.org'
    git config --global user.name 'Travis CI'
    git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"
    echo "exiting git configuration"
}


function merge_successful_pull_request() {
    if [[ $TRAVIS_PULL_REQUEST != "false" ]]; then
        configure
        git fetch
        git reset --hard

        STAGE_BRANCH=$TRAVIS_BRANCH-stage
        echo "### Just ran 'git reset --hard'. About to checkout '$STAGE_BRANCH"
        git checkout -b $STAGE_BRANCH
        echo "### Current branch: '$(git branch | head -n 1)'"
        git merge --ff-only "$TRAVIS_COMMIT"

        echo "### Just attempted to merge $TRAVIS_COMMIT"

        git checkout $TRAVIS_BRANCH -f && git merge $STAGE_BRANCH || exit 1

        if [[ $TRAVIS_BRANCH == "master" ]]; then
           echo "### Preparing to bumpversion. Current tag: $(git tag)"
           bumpversion minor
           echo "### New Tag: $(git tag)"
        fi

        git push --tags origin $TRAVIS_BRANCH
    else
        echo "No pull request."
    fi
}