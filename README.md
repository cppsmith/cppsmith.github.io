# cppsmith's blog sources

This repository is used to create static pages of [cppsmith's blog] with [Sphinx] and deploy them to [GitHub Pages] using [GitHub Actions].

#### so what?

Curious how to publish static content to GitHub Pages in CI jobs? Would like to use Sphinx to generate your pages?

> This is the right place (*yet another*) to look at for an example

#### great! now what?

Just open [sources](src/) to see an origin of static pages, look at [deploy.yml] for actions, check out [tasks.json] for pages generation. 

#### but what about repo settings?

Well, there are many articles on the Internet where one can find information on how to set up a GitHub repository and GitHub Pages to serve static content - README does not cover this topic.

[cppsmith's blog]: https://cppsmith.dev
[Sphinx]: https://www.sphinx-doc.org
[GitHub Pages]: https://pages.github.com
[GitHub Actions]: https://github.com/features/actions

[deploy.yml]: .github/workflows/deploy.yml
[tasks.json]: .vscode/tasks.json
[src]: src/
