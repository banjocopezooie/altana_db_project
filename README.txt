# Altana Project

This repository contains the Altana coding assessment.
The project was built using Python 3.9.0.

## Running the project
```commandline
python main.py /path/to/input_csv_file

example:
    python main.py input_data/cnpj-qsa.zip

```


# About the Project:

## Concerns about the project:
* One of the Biggest concerns I had was over-complicating the problem,
and trying to perform either too many, or unnecessary conversions.
I settled with just reading in the csv file into pandas in order to chunk the data.
Then I used the to_sql function pandas has to store the data into a .db file.

## Things I attempted:
* I tried normalizing the data by breaking it up into python classes and different tables in order to
use sqlalchemy. However I was having trouble getting that to work.
I went with the simpler method of just using sqlite in order to get a working solution.
I thought I would have enough time to add on, or improve the project, however I was unable
to do so. In the future though, I want to revist the idea as this could help improve
the performance and organization of the data.

## Notes:
* For the method, associated_companies_for_operator, the current version gets all
of the business partners for the given operator.
Inorder to get just the company business partners, this needs to be added to the execute command:
" and in_cpf_cnpj='1'".
I removed it from my method due to time constraints. When I had it in the execute method,
the results were empty due to no matching data for the given input.

