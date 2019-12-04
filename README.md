# Math-Series

**Author**: Stephen Koch
**Version**: 1.0.0

## Overview
Given a number "N", this code involves finding the Nth [Fibonacci Number](https://en.wikipedia.org/wiki/Fibonacci_number) and finding the Nth [Lucas Number](http://en.wikipedia.org/wiki/Lucas_number)

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
Make sure you have python3 installed:
```
$ python3 --version
```
If you do not:
```
$ brew install python
```
You need to have the files locally. Click on the green clone or download button and Download ZIP:
<!-- insert image here -->
In your command line, navigate to this directory:
```
$ cd ~  ##this is your root directory
$ cd Downloads  ##running MacOS: Downloads is a directory inside of your root; and where your file will be downloaded
```
This module is running tests on a given number. Install [pytest](https://docs.pytest.org/en/latest/getting-started.html) to get started:
Installing pytest:
```
$ pip install -U pytest
```
Running tests:
```
$ pytest
```
<!-- To change the input "N", you  -->

## Architecture
When the tests are run, the fibonacci, lucas, and sum_series functions are invoked.
Inputs default to a fibonacci number, starting the series at 0, 1.
If the optional inputs are given, the series will start at those given inputs.
Tests will pass if the expected result is returned from the function.

## Change Log
Tue Dec 03 2019 18:09:02 -

Setup
- [x] Create a repository with the exact name of math-series.
- [x] Start a branch in your repository called class-02
- [x] Create a new virtual environment where we can locally scope our project installations and dependencies
- [x] Add any standard configuration files such as .editorconfig, .gitignore, etc.
- [x] Write a README.mnd file describing the program and how to run it.
Features
- [x] Create a module series.py.
- [x] Add a file test_series.py to your repository. As you work on the tasks below, use TDD practices. Write tests first, then implement code. Make small changes with many cycles of Red-Green-Refactor

Create a function called fibonacci. The function should have one parameter n. The function should return the nth value in the fibonacci series. You may implement the function using recursion or iteration. If you are feeling particularly frisky, do both as separate functions.

Ensure that your function(s) has a well-formed docstring

In your series.py module, add a new function lucas that returns the nth value in the lucas numbers Again, you may use recursion or iteration, or both. Again, ensure that your function has a well-formed docstring.

Both the fibonacci series and the lucas numbers are based on an identical formula. Add a third function called sum_series with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.

Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will produce other series. Again, you may use recursion or iteration, or both. Again, ensure that your function has a well-formed docstring.

Add your series.py and test_series.py modules to your repository and commit frequently while working on your implementation. Include good commit messages that explain concisely both what you are doing and why.
