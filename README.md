![books](https://github.com/danielburdeno/Kindle-Recommendations/blob/main/Images/ebooks.jpg)

# Kindle eBook Recommendations: A Collaborative and Content Based Approach
Authors: Daniel Burdeno


## Overview
This project aims to build a two system approach to recommending Kindle eBook's to both existing reviewers and new users looking to find similar books. For existing reviewers a collaborative approach is taken by comparing similar reviewer profiles based on exisitng ratings. A content-based approach is taken in order to recommend books based on similar review text data and can be used by anyone.

## Business Problem
Currently eBooks are outsold by print books at about a 4 to 1 ratio. In 2020 there was 191 million eBooks sold. While Amazon holds over 70% of the market in eBooks via their kindle platform there is a large untapped potential for increasing eBook sales and promoting the use of eReaders compared to print. By utilzing quality recommendation systems Amazon can boost the interest and useablity of eBooks thus improving upon this market. The kindle platform and eBooks in general are incredidly accesibile for anyone with a tablet, smartphone, computer, or eReader. These eBooks can be immediatley purchased from a multitude of platforms and are able to read within minutes of purchase, which is far superior to obtaining a print book. This notion of real time purchase and useablily plays greater into Amazon's one click purchase philsophy. 

The kindle store is also full of cheap reads, with some eBooks even being free with certain subsripctions like prime and unlimited. A broad span of genres are available ranging from things like self-help books, cookbooks, and photography books to more traditional literature genres like Science Fiction & Fantasy and Romance novels. A final huge plus for the advocacy of eBooks is the ease in which readers can rate and reviews books they have either just read or already read. This can all be done via the same platform used to access and read the eBook (aka kindle). Ultimately this plays into the collection of more review and rating data wich in turn can attribute to better performing recommendations for each indiviudal user. A quality recommendation system can thus create a positive feedback loop that not only enhances itself but promotoes the increase in eBook sales across the board.

Sources: [1](https://www.tonerbuzz.com/blog/paper-books-vs-ebooks-statistics/) [2](https://www.statista.com/topics/1474/e-books/#:~:text=E%2Dbook%20sales%20in%20the,consistent%20annual%20increases%20since%202018.)

## Data Understanding
Data for this project was pulled from a compiled dataset of Amazon kindle store reviews and meta data in two seperate JSON files. The datasets can be found [here](https://nijianmo.github.io/amazon/index.html). I utlized the smaller dataset known as 5-core which contained data for products and reviewers with at least 5 entries. Data from the Kindle Store sets were used, both the 5-core review data and the full metadata file. Due to the large size of these datasets I downloaded them locally and saved to an external repository outside of github.

![rev](https://github.com/danielburdeno/Kindle-Recommendations/blob/main/Images/Revimg.png) ![meta](https://github.com/danielburdeno/Kindle-Recommendations/blob/main/Images/Metaimg.png)

Once the data was loaded in, cleaned, and processed I saved seperate csv files locally as well, again due to size constraints. Several data sets including a reduced user dataframe and two meta data files were saved and pushed to github as seen in the repository structure. These files are needed for heroku to run the app that was developed. 

Citation: 

Justifying recommendations using distantly-labeled reviews and fined-grained aspects

Jianmo Ni, Jiacheng Li, Julian McAuley

Empirical Methods in Natural Language Processing (EMNLP), 2019 [pdf](https://cseweb.ucsd.edu//~jmcauley/pdfs/emnlp19a.pdf)


## Data Preparation





## Methods and Models

### Collaborative Filtering
![Surprise](https://github.com/danielburdeno/Kindle-Recommendations/blob/main/Images/Model_bar.png)

### Content-Based

## Conclusions



## Repository Structure
```
├── [Data]
│    ├── df_dtm.parquet
│    ├── df_user.csv
│    ├── meta5.csv
│    ├── meta_all.csv
├── [Images]
├── [Model]
├── .gitignore
├── CollaborativeFiltering.ipynb
├── ContentBased.ipynb
├── DataPrepFinal.ipynb
├── final_presentation.pdf
├── LICENSE
├── Procfile
├── README.md
├── app.py
├── requirements.txt
└── setup.sh
```
