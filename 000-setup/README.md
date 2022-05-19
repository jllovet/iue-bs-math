## Setup for LaTex Workshop

So that I can manage my LaTeX documents across all of my devices without having to worry about dependency conflicts, and so that others will be able to build my documents successfully in the future, this is the base setup that I use.

I work in Visual Studio Code, where I also do my software engineering work. The setup I use makes use of the [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) plugin and Docker to make it easier to automatically recompile my documents locally.

This setup is modified from the first option described in the article [Three Ways to Create Dockernized LaTeX Environment](https://towardsdatascience.com/three-ways-to-create-dockernized-latex-environment-2534163ee0c4). Follow the steps there, with the modifications specified below.

**Nota bene,** the docker image listed in the article is no longer maintained. Instead of that the one listed there, I have modified blang/latex. The modifications I have made are to fix issues with fonts when using the container with the LaTeX Workshop plugin for VSCode, especially to address some issues with UTF8 support (i.e. to be able to support multiple languages and their writing systems).

```SHELL
docker image pull blang/latex
docker image pull blang/latex:ctanfull
docker image pull jllovet/latex
```

Add the following to VSCode's settings.json:
```JSON
    "latex-workshop.docker.enabled": true,
    "latex-workshop.latex.outDir": "./texout",
    "latex-workshop.synctex.afterBuild.enabled": true,
    "latex-workshop.view.pdf.viewer": "tab",
    "latex-workshop.docker.image.latex": "jllovet/latex",
    "latex-workshop.latex.tools": [{
        "name": "latexmk",
        "command": "latexmk",
        "args": [
            "-xelatex",
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "-output-directory=./texout",
            "--shell-escape", // added arg to default
            "%DOC%"
        ]
    }]
```
This can either be configured for the entire workspace or for individual projects. If it is configured on a per-directory basis, then `settings.json` should be inside a `.vscode` folder, as shown below

```SHELL
.
├── README.md
└── a-book-to-read
    ├── .vscode
    │   └── settings.json
    ├── bibliography.bib
    ├── texout
    │   ├── .keep
    │   ├── my_article.aux
    │   ├── my_article.bbl
    │   ├── my_article.bcf
    │   ├── my_article.blg
    │   ├── my_article.fdb_latexmk
    │   ├── my_article.fls
    │   ├── my_article.log
    │   ├── my_article.pdf
    │   ├── my_article.run.xml
    │   ├── my_article.synctex.gz
    │   └── my_article.xdv
    └── my_article.tex
```

## Setup for Diagrams

The package [diagrams](https://diagrams.mingrammer.com/) allows you to define elegant diagrams using python. As with LaTeX, I provide a docker image (jllovet/diagrams) in this repository to make it easier to use. You can retrieve this image from Docker Hub or build it yourself.

```SHELL
docker image pull jllovet/diagrams
```

There is a bash script to make it easier to run the python programs defined for creating diagrams. You can find it at [diagram](./diagrams/diagram). I recommend you add the path to the file to your PATH if you plan on using it frequently. It takes a single argument specifying the name of the python script that you want to run.

Assuming the script `diagram` is available on your PATH:

```SHELL
diagram example_flow.py
```

This will run the python script inside of a container defined by the image `jllovet/diagrams`, which has the python and `graphviz` dependencies required to run successfully. The docker container will mount a volume to the directory that you are currently in. Docker will use this volume to export the file that is created by the script using `diagrams` package.
