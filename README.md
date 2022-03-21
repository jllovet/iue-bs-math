# Indiana University East - Bachelors of Science in Mathematics 🧮
---

Here you will find my notebooks, papers, code and other work towards the IUE B.S. in Mathematics. Sprinkled among these attempts at clear thinking are resources and reflections you may find helpful about mathematics, software, and philosophy.

   >**Note:** Some of the projects in this repo will require some software dependencies. See [here](#Environment-Setup).

If you'd like to help support my studies and projects like this repo, I'd be delighted if you bought me a coffee.

<a href="https://www.buymeacoffee.com/jllovet"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=jllovet&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" /></a>

## About

[IUE - Bachelors of Science in Mathematics](https://www.iue.edu/online/degrees-certificates/bachelor-of-science-mathematics.html)

### Core Courses

The following are required courses for the program
- MATH-M 215 Calculus I (5 Credits)
- MATH-M 216 Calculus II (5 Credits)
- MATH-M 303 Linear Algebra (3 Credits)
- MATH-M 311 Calculus III (3 Credits)
- MATH-M 393 Bridge to Abstract Mathematics (3 Credits)
- MATH-M 403 Modern Algebra (3 Credits)
- MATH-M 413 Real Analysis (3 Credits)
- MATH-M 447 Mathematical Models (3 Credits)
- MATH-M 499 Senior Seminar (3 Credits)

### Electives

The following are courses from which I will choose, pending discussions with academic advisors

- MATH-M 312 Calculus IV (3 Credits)
- MATH-M 313 Differential Equations (3 Credits)
- MATH-M 366 Elements of Statistical Techniques (3 Credits)
- MATH-M 371 Elementary Computational Methods (3 Credits)
- MATH-M 380 History of Mathematics (3 Credits)
- MATH-M 404 Modern Algebra II (3 Credits)
- MATH-M 405 Number Theory (3 Credits)
- MATH-M 421 Introduction to Topology I (3 Credits)
- MATH-M 448 Mathematical Models II (3 Credits)
- MATH-M 451 Mathematics of Finance (3 Credits)
- MATH-M 463 Intro to Probability Theory I (3 Credits)
- MATH-T 321 Intuitive Topology (3 Credits)
- MATH-T 336 Topics in Euclidean Geometry (3 Credits)

# Tools and Resources
---

Articles and resources about sundry topics you may need for interacting with my repository, but that you may not be familiar with yet, depending on your background.

## Environment Setup
Where possible, I will provide a containerized environment for any work that uses software, to abstract away the setup. To do this, I will primarily use Docker. Docker is a tool used frequently in software engineering for creating containers, which are similar to lightweight virtual machines, but make more efficient use of the resources of the underlying host machine. 
- [Docker Overview](https://docs.docker.com/get-started/overview/)

## MarkDown

This document is in Markdown!

   > Markdown is a text-to-HTML conversion tool for web writers. Markdown allows you to write using an easy-to-read, easy-to-write plain text format, then convert it to structurally valid XHTML (or HTML).
   Source: [https://daringfireball.net/projects/markdown/](https://daringfireball.net/projects/markdown/)

- [Markdown (Github's flavor)](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Dillinger (An Online Markdown Previewer)](https://dillinger.io/)

## LaTeX

   > LaTeX is a high-quality typesetting system; it includes features designed for the production of technical and scientific documentation. LaTeX is the de facto standard for the communication and publication of scientific documents. LaTeX is available as free software.
   Source: [https://www.latex-project.org/](https://www.latex-project.org/)

### Books on LaTeX

- [Books on LaTeX](https://www.latex-project.org/help/books/)
- [LaTeX in 157 Minutes](https://www.amazon.com/Latex-157-minutes-Short-Introduction/dp/9881443628)

### Examples

- [Overleaf LaTeX Book Gallery](https://www.overleaf.com/gallery/tagged/book)

### Discussions and Tutorials

- [Dr. Trefor Bazett - Intro to LaTeX Part I](https://www.youtube.com/watch?v=Jp0lPj2-DQA)
- [Dr. Trefor Bazett - Intro to LaTeX Part II](https://www.youtube.com/watch?v=-HvRvBjBAvg)
- [dspinellis/latex-advice](https://github.com/dspinellis/latex-advice)
- [Compiling LaTeX Locally on macOS with VS Code and Git](https://jrwang.ca/2020/01/13/latex-vscode-git/)

You can find a summary of my LaTeX setup here:
- [jllovet LaTeX Setup](https://github.com/jllovet/iue-bs-math/000-setup/README.md)

## Citations and Bibliographies

### Discussions

- [Bibliographies - Stylistic conventions for bibliographies in mathematical writing](https://faculty.math.illinois.edu/~hildebr/tex/tips-bibliographies.html)
- [Wikibooks - LaTeX Bibliography Management](https://en.wikibooks.org/wiki/LaTeX/Bibliography_Management)

### Tools and Packages

#### Zotero
   > Zotero is a free, easy-to-use tool to help you collect, organize, cite, and share research.
   Source: [https://www.zotero.org/](https://www.zotero.org/)

- I use Zotero to generate .bib files for myself to use in my LaTeX documents. See below on Biblatex.
#### biblatex and biber
   > The biblatex package is becoming the definitive citation management tool for LaTeX users. Biblatex provides a powerful and flexible macro interface for authors of citation styles.
   Biblatex's own data backend processor, biber, allows biblatex to offer [a lot of] features.
   Source: [http://biblatex-biber.sourceforge.net/](http://biblatex-biber.sourceforge.net/)

- If you're interested, you should read [this article on CICD for LaTeX](https://ljvmiranda921.github.io/notebook/2018/04/23/postmortem-shift-to-docker/), which deals with these packages.
#### amsrefs
amsrefs is a LATEX package for preparing bibliography or reference lists.
- [User’s Guide to the amsrefs Package](http://www.bakoma-tex.com/doc/latex/amsrefs/amsrdoc.pdf)
- [American Mathematical Society - TeX Resources](http://www.ams.org/publications/authors/tex/tex)

#### MathSciNet
MathSciNet is a database of known mathematics and science journals provided by the American Mathematical 
Society. It is available by subscription only.

- [mathscinet](https://mathscinet.ams.org/mathscinet)

## Knowledge Management System ፨ 👨🏻‍💻 📄
I'm trying out [Obsidian](https://obsidian.md/) to manage a knowledge graph for myself with Markdown and will be storing in this repository. Running notes will be in Markdown with mathematical sketches in inline LaTeX and embedded diagrams generated from other tools. Since Markdown is plain-text, this knowledge graph will be maintainable through git, like the rest of the project. It will be consumable through Obsidian or [Foam](https://foambubble.github.io/foam/) (one of its VSCode-plugin competitors).

- [Citations](https://www.marianamontes.me/post/obsidian-and-zotero/) plugin for Obsidian To Use .bib files from [Zotero](https://www.zotero.org/) to import bibliographies

## Visualizations

### Python Packages
- [diagrams](https://diagrams.mingrammer.com/)
- [matplotlib](https://matplotlib.org/)
- [plotly](https://plotly.com/)
- [manim](https://www.manim.community/)

### Standalone Tools
- [Graphviz](https://www.graphviz.org/)

## Software Engineering
- [Git](https://git-scm.com/)
- [Docker](https://docs.docker.com/get-started/overview/)
- [Visual Studio Code](https://code.visualstudio.com/)