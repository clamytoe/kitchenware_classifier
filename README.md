# Kitchenware Classification (*kitchenware_classifier*)

> *Classifies kitchen stuff items into 6 categories: cups, glasses, plates, spoons, forks and knives*

![Python version][python-version]
![Latest version][latest-version]
[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]

NOTE: This project was generated with [Cookiecutter](https://github.com/audreyr/cookiecutter) along with [@clamytoe's](https://github.com/clamytoe) [toepack](https://github.com/clamytoe/toepack) project template.

This repo is the result of my capstone project for the Machine Learning Zoomcamp 2022 course. I used the model for a [Kitchenware Classification](https://www.kaggle.com/competitions/kitchenware-classification) competition that was hosted by the [DataTalks.Club](https://datatalks.club/) over at [Kaggle](https://www.kaggle.com).

The model will take an image of a kitchenware item and try to classify it into one of the following classes:

* cups
* forks
* glasses
* knives
* plates
* spoons

I was able to score a `0.97674` with it and am currently in the 13th place as a member of Team **Penumbra**!

My fellow team mebers were:

* Roman Zabolotin - Junior Data Scientist
* Tatiana Ankudo - Analyst

## The data

The dataset is pretty big so I did not include it here. You can download it from the competition page.

In order to get things to work right the first time, extract it's contents into the `kitchenware_classifier/data/` folder.

My tree structure looks like this:

```zsh
├── Dockerfile
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── api.py
├── environment.yml
├── evaluate_model.py
├── fastai-classifier.ipynb
├── fastai_model.pkl
├── favicon.ico
├── images
│   ├── coffe.jpg
│   ├── docs.png
│   ├── post.png
│   ├── result.png
│   ├── selected.png
│   └── upload.png
├── kitchenware_classifier
│   ├── data
│   │   ├── images
│   │   ├── sample_submission.csv
│   │   ├── test.csv
│   │   └── train.csv
│   └── kitchenware-classification.zip
├── kw_router.py
├── predictions
│   └── fastai-submission.csv
├── requirements.txt
├── sample.jpg
├── sample2.jpg
├── test_model.py
├── test_multiple_images.py
├── test_single_image.py
└── train.py
```

## Initial setup

First thing to do is to create or change directories into wherever you keep all of your projects.
For me, it's the `Projects` folder.
Once there clone this repo.

```zsh
(py310) ➜ cd Projects
(py310) ➜ git clone <https://github.com/clamytoe/kitchenware_classifier.git>
(py310) ➜ cd kitchenware_classifier
```

## Anaconda setup

If you are an Anaconda user, this command will get you up to speed with the base installation.

```zsh
(py310) ➜ conda env create
(py310) ➜ conda activate kwc
```

## Regular Python setup

If you are just using normal Python, this will get you ready.
First thing is to create a virtual environment. There are many ways to do this, but the simplest is using `venv`.

```zsh
(py310) ➜ python3 -m venv venv
(py310) ➜ source venv/bin/activate
(venv) ➜ pip install -r requirements.txt
```

## Start the server

Once your environment is setup, this one command will start the server:

```zsh
(kwc) ➜ uvicorn api:app --reload
```

## Usage

With the server up and running, you can now send it images to classify for you. I have included two sample images:

<img src="sample.jpg" alt="sample 1" width="200" />

and

<img src="sample2.jpg" alt="sample 2" width="200" />

I have provided two sample scripts:

* `test_simgle_image.py`
* `test_multiple_images.py`

With the server running, you can run either of the scripts to test out the server.

*test_simgle_image.py:*

```zsh
(kwc) ➜ python test_single_image.py
{'class': 'fork'}
```

*test_multiple_images.py:*

```zsh
(kwc) ➜ python test_multiple_images.py
[{'image': 'sample2.jpg', 'class': 'plate'}, {'image': 'sample.jpg', 'class': 'fork'}]
```

Now you can modify the scripts and use them for your own purpose.

## A much easier way

The benefit of using FasAPI is that it makes things much easier and faster. For instance, if you nagivate to: [http://localhost:8000/docs](http://localhost:8000/docs) you will be able to interact with the application.

![docs](images/docs.png)

### GET / Welcome

This entrypoint just returns some information about me and the project.

### POST /classify_image Classify Image

This is where you get to test out the model and see how well it works. Feed it an image of kitchenware item and see how well it does.

To use it, simply click on the **POST** button to expand it:

![post](images/post.png)

Then click on the **Try it out** button.

![upload](images/upload.png)

This will reveal a **Choose File** button that will allow you to navigate your filesystem and choose and image.

Here, I've randomly chosen a tricky one from the Internet to see what the model picks up:

<img src="images/coffe.jpg" alt="coffe" width="200" />

With the image loaded:

![selected](images/selected.png)

Simply click on the big **Execute** button to process the image.

If you scroll down a bit, you will see your results:

![results](images/result.png)

As you can see, it picked up on the cup!

## Docker image

If you would rather run this as a docker container you can simply download an already compiled version from Docker Hub: Kitchenware Classifier

```zsh
(kwc) ➜ docker pull clamytoe/kitchenware-clf
```

Once you have the image you can run it as so:

```zsh
(kwc) ➜ docker run -it --rm -p 8000:8000 clamytoe/kitchenware-clf
```

> **NOTE:** The image is just a little over 6GB.

### Build your own

If you would rather build the docker image yourself, I have included the Dockerfile just for that purpose. Just run the following command from the directory where you cloned this repo to:

```zsh
(kwc) ➜ docker build -t kitchenware-clf .
```

Once you have the image you can run it as so:

```zsh
(kwc) ➜ docker run -it --rm -p 8000:8000 kitchenware-clf
```

## Contributing

Contributions are welcomed.
Tests can be run with with `pytest -v`, please ensure that all tests are passing and that you've checked your code with the following packages before submitting a pull request:

* black
* flake8
* isort
* mypy
* pytest-cov

I am not adhering to them strictly, but try to clean up what's reasonable.

## License

Distributed under the terms of the [MIT](https://opensource.org/licenses/MIT) license, "kitchenware_classifier" is free and open source software.

## Issues

If you encounter any problems, please [file an issue](https://github.com/clamytoe/toepack/issues) along with a detailed description.

## Changelog

* **v0.1.0** Initial commit.

[python-version]:https://img.shields.io/badge/python-3.9.13-brightgreen.svg
[latest-version]:https://img.shields.io/badge/version-0.1.0-blue.svg
[issues-image]:https://img.shields.io/github/issues/clamytoe/kitchenware_classifier.svg
[issues-url]:https://github.com/clamytoe/kitchenware_classifier/issues
[fork-image]:https://img.shields.io/github/forks/clamytoe/kitchenware_classifier.svg
[fork-url]:https://github.com/clamytoe/kitchenware_classifier/network
[stars-image]:https://img.shields.io/github/stars/clamytoe/kitchenware_classifier.svg
[stars-url]:https://github.com/clamytoe/kitchenware_classifier/stargazers
[license-image]:https://img.shields.io/github/license/clamytoe/kitchenware_classifier.svg
[license-url]:https://github.com/clamytoe/kitchenware_classifier/blob/master/LICENSE
