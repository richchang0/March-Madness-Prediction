## March Madness Prediction

#### Purpose
- To utilize machine learning techniques to predict the NCAA March Madness Tournament
- All data used in our predictions are scraped from Statsheet

#### Documentation
Overview of the files contained in this repo

##### Scripts
- statsheet_scrape.py
 - used to get team info (name, url, stats, schedule)
- espn_scrape.py
  - no longer used
- clean_data.py
 - cleans the data scraped from statsheet into our custom format
- build_examples.py
 - generates instances using game data + stats for the teams
- compare_prediction.py
 - elminates last column of march instances to create testing data
 - calculates accuracy of Weka's predicted output using our training model
- util.py
 - no longer used

##### Textfiles
- games
 - D1 conference games for the 2012-2013 season
   - homeTeam, awayTeam, outcomeForHomeTeam
 - Tourny games for 2013 March Madness
   - firstTeam, secondTeam, outcomeForFirstTeam  
- stats
 - team statistics for various seasons, we are only using the 2012-2013 stats
- teams
 - information for D1 teams arranged in the following format
   - team name, statsheet url, division, home court 
  - also contains various team files that were used in cleaning up our dataset
- model_data
 - contains the csv + arff (open and save csv files in Weka to generate these)
 - remember to set the outcome field as {W,L} when handling the arff for march games, otherwise Weka won't let you supply this as a testing set
- model_results
 - predicted results from weka
 - will be saved as arff, remember to remove the @stuff and eliminate last column from each row ",?"
