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
