# How world reacted to Coronavirus Case Study

URL of case study is https://coronacase-study.herokuapp.com/

# This case-study answers following questions:

- Is hate speech or offensive language or both are involved?
- To whom hate speech were directed to?
- Can we identify the main abusers on twitter?
- Temporal Analysis?
- Variation in Emotions?
- Any other finding evident from large volume of twitter data?

# This case study studies the impact of:

1. Hate speech: abusive or threatening speech or writing that expresses prejudice against a particular group, especially on the basis of race, religion, or sexual orientation. 
2. Offensive tweets: insulting, unpleasant, disgusting, abusive language, as to the senses causing anger or annoyance. 
3. Sentiment scores: It determines whether a piece of text is positive, negative or neutral. 
4. Mean sentiment scores: It is the average/mean of sentiment scores of the tweets posted over the period of one month to determine overall positivity or negativity in tweets of the respective month.

# Methodology

After collection of tweets these were labelled offensive, hate speech and sentiment scores were annotated.
For creating word cloud the offensive, hate speech tweets were pre-processed using regular expressions in python, then for stop words removal tweets were passed into 'en_core_web_sm' module of Spacy library for removal and filtering out stop words.

# Dataset Details

Hashtags | Tweets collected | Corresponding hashtags | Start Date | End Date | Coronavirus 
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----



