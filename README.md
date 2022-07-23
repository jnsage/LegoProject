# [Untitled Lego Project](https://github.com/jnsage/LegoProject) 

As a collector of LEGO sets, I am interested in examining data pulled from 2 LEGO Collection websites: Brickset and Rebrickable. I wanted to explore these questions:

1) Does a higher number of pieces in a LEGO set guarantee a higher user rating on Brickset?
2) For Star Wars-themed LEGO sets, does the popularity of a specific Star Wars property correlate to the customer rating of sets for that movie/TV Show?
3) Could I find the Star Wars set that has the most pieces, and then find the top 10 most common parts in that set.

This project reads in data, cleans up and merges data where necessary, then saves the resulting data to a .csv files. The resulting files are then used to create a Tableau dashboard.

# Data used in Untitled Lego Project
Sources: 
1) [Star Wars IP Google Sheet](https://docs.google.com/spreadsheets/d/1xw7y9yawF6i35BTfP9M1uUawJvwpacz01Xq4MEZszBs/edit#gid=0)
- IP Title, Is_Movie, Is_TV, Release Year, Rotten Tomato rating
2) [Brickset](https://brickset.com/) via  API
- Set Number, Set Name, Release Year, Theme, Theme Group, Subtheme, Number of Pieces, and Brickset Rating
3) [Rebrickable](https://rebrickable.com) via .csv download 
- Set Number, Inventory ID, Part Number, Quantity of parts. 


# Requirements
- Python v3.10.1
- pandas v1.4.2
- requests 2.271.1
- notebook 6.4.12
- Pillow 9.2.0
- Bricket and  Rebrickable API keys
- Active internet connection

  
   
# Instructions 
## API Keys

### Rebrickable
1. Make an account at [Rebrickable](https://rebrickable.com) 
2. Follow the steps on the [Rebrickable API page](https://rebrickable.com/api/) to generate a personal key
### Brickset
1. Make an account at [Brickset](https://brickset.com/)
2. Follow the steps on the [Brickset API page](https://brickset.com/tools/webservices/requestkey) to generate a personal key

### 
## Installation and Setup

From the command line:
1) Clone the [Untitled Lego Project](https://github.com/jnsage/LegoProject) repo from GitHub:
```
git clone git@github.com:jnsage/LegoProject.git
```
2) Navigate to the Untitled Lego Project directory.
3) Create and a virtual environment 
```
python -m venv venv
```
4) Activate your environment 

- Windows:
```
 . venv/Scripts/activate
```
-  Mac/Linux:
```
source venv/bin/activate
```
5) Use pip to install system requirements:
```
pip install -r requirements.txt
```
6) From File Explorer/Finder, navigate to the LegoProject directory and open the 'Keys' folder
7) Open 'rebrickable.txt' and replace 'REBRICKABLEAPIKEY' with your Rebrickable API key. Save and close 'rebrickable.txt'
8) Open 'brickset.txt' and replace 'BRICKSETAPIKEY' with your Brickset API key. Save and close 'brickset.txt'

## Run notebooks
9) From the command line, launch Jupyter Notebook:
```
jupyter notebook
``` 

10) Run the following notebooks to see the steps for importing, manipulating, and saving the data to be user later
```
NumPiecesRating.ipynb
IPRatings.ipynb
TopTenParts.ipynb
```

## Open Visualizations
11) View the visualzations based on the clean data on [My Tableau Public page](https://public.tableau.com/app/profile/jnsage/viz/)


# Code Louisville Project Requirements
- Category 1 - Loading Data
    - Read two datasets with an API
    - Read two data files 
- Category 2 - Clean Data
    - Clean data and perform a pandas merge on two datasets. Then calculate a new value based on the new data set
- Category 3 - Present Data
    - Make a Tableau Dashboard to display data
- Category 4 - Best Practices
    - Utilize a virtual environment and include instructions in the README on how to set one up.
    - Lists dependencies in a requirement.txt file.

# Changes from Proposal
- Original question of examining possible relationship between Brickset rating and the age ratings for LEGO sets was eliminated. There were too many missing values for the minimum and maximum age ranges of LEGO sets.
 


