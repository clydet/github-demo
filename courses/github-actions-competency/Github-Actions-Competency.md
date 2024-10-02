# GitHub Actions Competency

## Section 1: Your first GitHub Action workflow
- Create a simple container image CI build

###Questions:###
- How can you automate container image publish via a github action workflow?
    - How can you publish your image to a docker registry without exposing your login credentials in the source code?
        - Look into how you can configure [secrets in github](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions).
- Are there any existing premade github actions that can make docker image build and publish easier?
    - HINT: check out the [GHA action marketplace](https://github.com/marketplace)

- How might we support multiple architectures with our container image builds?
    - i.e. arm64 and amd64
    - Just think about this for now don't worry about solving this yet. We will cover this in Section 3


## Section 2: GHA resources
- [GHA Docs](https://docs.github.com/en/actions)
- [CHA workflow triggers](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)

## Section 3: Multi-architecture support
TBD
