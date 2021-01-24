#!/usr/bin/env bash
git push --tags
bazel build //caper/bazel_compose:bazel_compose.par
ghrelease gravypod/bazel_compose $(git describe --abbrev=0 --tags) -- bazel-bin/caper/bazel_compose/bazel_compose.par
