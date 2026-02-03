#!/usr/bin/env bash

if [ -z "$1" ]; then
	echo "Please provide a tag."
	echo "Usage: ./release.sh v[X.Y.Z]"
	exit
fi

echo "Preparing $1..."
# update the version
msg="# managed by release.sh"
# update the changelog
git add -A && git commit -m "chore(release): prepare for $1"
git show
# generate a changelog for the tag message
git tag -a "$1" -m "Release $1"
echo "Done!"
echo "Now push the commit (git push) and the tag (git push --tags)."
