# Third-party notices

The slides, the speaker notes and the PDFs in `presentation/build/` contain material by others, listed here with its licence.

## HCCI SEM micrographs

The micrographs and the mask in `presentation/assets/hcci/` come from B.-I. Bachmann, M. Stiefel, M. Müller and F. T. Mücklich, [A Systematically Designed Open-Access SEM Dataset and Robustness Benchmark for Machine Learning-Based Microstructure Segmentation: A High-Chromium Cast Iron Case Study](https://doi.org/10.5281/zenodo.21931379), dataset, Zenodo, version 1, 2026, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The micrographs are converted to grayscale JPEG and downscaled, and some are centre-cropped to the shape of their place on the slides; the mask is downscaled and its colours are softened 25 % toward white. `presentation/tools/prepare_hcci_images.py` makes these changes, and `presentation/assets/hcci/provenance.csv` lists the source of each file.

## Matt Pocock's skills

The speaker notes after slide 29 reproduce the section "Why These Skills Exist" of the README of [mattpocock/skills](https://github.com/mattpocock/skills), and slides 26 and 27 show a shortened `tdd/SKILL.md`, both from version 1.3.1 (commit 49dd158). They are used under this licence:

```text
MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Logos and screenshots

The Saarland University logo (`presentation/assets/uds-logo.pdf`) and the d3M logo (`presentation/assets/d3m.png`) belong to their owners. The screenshots in `presentation/assets/screens/` show VS Code, the Claude app, Claude Code and a GitHub page; these products and their names belong to their owners.
