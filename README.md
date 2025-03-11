# datascipsych-template
Final project for Data Science for Psychology course

## Data

The data are included in the project under `src/project/Polyn_2011_score.csv`. After the project is installed, you can use `project.task.get_data_file()` to get the filepath to the data file.

### Data dictionary

subject
: subject identifier code

list
: list number

item
: item that was presented or recalled

input
: position the item was presented in the list (also known as serial position)

output
: position that the item was recalled during the free-recall period (also known as output position)

study
: "true" if this item was presented and "false" if it was not (this only happens when the participant accidentally recalls an item that was not on the list, or if they accidentally repeat the same item multiple times during recall). To exclude all repeats and intrusions, filter for trials where the study field is "true"

recall
: "true" if this item was recalled and "false" if it was not recalled

repeat
: the number of times this item was repeated during recall

intrusion
: "true" if this item was recalled but was not actually presented on the list

task
: 1: uncategorized list, followed by free recall; 2: categorized list, followed by free recall; 3: categorized list, followed by recall-by-category

category
: category this item belongs to ("n/a" for intrusions)

period
: if this was a recall-by-category list (task code=3), indicates the recall period that the category was cued
