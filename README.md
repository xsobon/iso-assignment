# iso-assignment
Iso-assignment for kiwi.com
assignement: https://github.com/rlapar/iso-assignment/tree/master

## Overview

Application for country search based on iso code. Python 3.10 and Pycharm IDE were used for the project.
The main.py file contains the application. Ten tests were created in the unti_test.py file to verify the function of the application.
File requirements2.txt contains the required packages.

## Dependencies
To install packages: 

```
pip3 install -r requirements2.txt

```

## Exapmles

Request: 
```
{}
```
Response:
```
{
  'message': {'iso': 'Add iso value.'}
}
```

Request:
```
{"iso": "svk"}
```
Response:
```
{
  'message': {'countries': 'Without countries list there can't be any match.'}
}
```

Request:
```
{
  "iso": "pol",
  "countries": [
              "iran",
              "Polonia",
              "Slowakei",
              "Ajdnfkruu"
               ]
}
```
Response:
```
{
  "iso": "pol",
  "match_count": 1,
  "matches": [
            "Polonia"
             ]
}
```
More tests in a file unti_test.py.

##### Autor: Tomáš Soboňa 









