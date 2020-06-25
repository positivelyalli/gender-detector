# Gender Detector
## Predict the gender of a character based on word distribution in dialogue
A Multinomial Naive Bayes machine learning NLP model to predict the gender of a character based on their lines of text displayed in an interactive website.

## Process
1. Get Raw Text Dataset - https://www.kaggle.com/Cornell-University/movie-dialog-corpus
2. Make a task list with deadlines
3. Data Cleaning
    Change 6000 non-gender characters into 
4. Join with gender for character id
5. Tokenization - make sure that gender is tokened
6. Stem or lemmatize
7. Filter stopwords
8. TF-IDF
9. Machine Learning
10. Responsive webpage
11. Plotly plots
    - Looking at word frequency  
        - Bubble chart - skewed words plotly.js with animation on male vs female
            - Load csv through d3.js
            - Need gender and words with count
        - Histogram of male vs female characters with animation on male vs female
            - Load csv through d3.js
            - Need character count and gender
12. Word cloud for each gender 
    Create dataframe for each gender
    Filter stopwords and lemmatize
    Create word cloud and save to display on website
13. FlaskApp for running model   
    Predict input in webpage
14. JS file 

###Tuning the model:
    - Stemming/lemmatization first - Lowered slightly - word clouds better
    - No stemming/lemmatization - No difference
    - Take out non-gendered lines - YES improved to .69
    - Randomly select from buckets to make it even - Accuracy went down
    - Take out apostrophe's

## Team
- [Alli Kruger](https://github.com/positivelyalli)
- [Sowmya Srinivasan](https://github.com/sowmyasrinivasan)
