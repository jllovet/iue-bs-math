## Setup for LaTex Workshop

So that I can manage my LaTeX documents across all of my devices without having to worry about dependency conflicts, and so that others will be able to build my documents successfully in the future, this is the base setup that I use.

I work in Visual Studio Code, where I also do my software engineering work. The setup I use makes use of the [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) plugin and Docker to make it easier to automatically recompile my documents locally.

This setup is modified from the first option described in the article [Three Ways to Create Dockernized LaTeX Environment](https://towardsdatascience.com/three-ways-to-create-dockernized-latex-environment-2534163ee0c4). Follow the steps there, with the modifications specified below.

**Nota bene,** the docker image listed in the article is no longer maintained. Instead of that the one listed there, I use the following:

```SHELL
docker image pull blang/latex
```

Add the following to VSCode's settings.json:
```JSON
    "latex-workshop.docker.enabled": true,
    "latex-workshop.latex.outDir": "./out",
    "latex-workshop.synctex.afterBuild.enabled": true,
    "latex-workshop.view.pdf.viewer": "tab",
    "latex-workshop.docker.image.latex": "blang/latex",
```
