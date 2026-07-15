"""
PolitiPulse NLP Workshop — Week 3 Assignment
Sentiment Analysis with VADER
"""

import string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# The five raw public comments from Layer 1 (Data Acquisition)
comments = [
    "The New Roads Policy is AMAZING!!!",
    "i dont think the new tax rule helps anyone.",
    "The committee met on Tuesday to review the budget.",
    "Honestly, this healthcare reform is a disaster.",
    "Farmers finally got the support they deserve, great move!!",
]

# ---------------------------------------------------------------
# Question 1(a) — Preprocessing function
# Steps taught in the workshop: lowercasing, punctuation removal,
# tokenization
# ---------------------------------------------------------------
def preprocess(text):
    # Step 1: lowercasing
    text = text.lower()
    # Step 2: punctuation removal
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Step 3: tokenization (split on whitespace)
    tokens = text.split()
    return tokens


print("=" * 60)
print("Question 1(a): Preprocessed tokens")
print("=" * 60)
for c in comments:
    print(f"Original : {c}")
    print(f"Tokens   : {preprocess(c)}\n")

# ---------------------------------------------------------------
# Question 1(b) — VADER compound scores on ORIGINAL comments
# (VADER uses capitalization/punctuation as cues, so we do NOT
# preprocess before scoring)
# ---------------------------------------------------------------
print("=" * 60)
print("Question 1(b): VADER compound scores (original comments)")
print("=" * 60)
for c in comments:
    scores = analyzer.polarity_scores(c)
    print(f"Comment  : {c}")
    print(f"Compound : {scores['compound']}\n")

# ---------------------------------------------------------------
# Question 2 — Mini Approval-Rating Pipeline
# Public Comment -> VADER -> Sentiment Score -> Average Score
# -> Approval Rating -> Dashboard
# ---------------------------------------------------------------

# 2(a): list of comments -> list of compound scores
def get_compound_scores(comments):
    return [analyzer.polarity_scores(c)["compound"] for c in comments]


# 2(b): mean of a list of compound scores
def average_score(scores):
    return sum(scores) / len(scores)


# 2(c): map average compound score to an approval-rating label
def approval_rating(avg_score):
    if avg_score >= 0.5:
        return "Strongly Approve"
    elif avg_score >= 0.05:          # 0.05 <= avg < 0.5
        return "Approve"
    elif avg_score > -0.05:          # -0.05 < avg < 0.05
        return "Neutral"
    elif avg_score > -0.5:           # -0.5 < avg <= -0.05
        return "Disapprove"
    else:                            # avg <= -0.5
        return "Strongly Disapprove"


# 2(d): run the full pipeline on the five comments
print("=" * 60)
print("Question 2(d): Full pipeline run")
print("=" * 60)
scores = get_compound_scores(comments)
avg = average_score(scores)
label = approval_rating(avg)
print(f"Compound scores : {scores}")
print(f"Average score   : {avg:.4f}")
print(f"Approval rating : {label}\n")

# ---------------------------------------------------------------
# Question 3 — Per-Comment Sentiment Classifier
# ---------------------------------------------------------------
def classify_sentiment(text):
    compound = analyzer.polarity_scores(text)["compound"]
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"


print("=" * 60)
print("Question 3: Per-comment sentiment labels")
print("=" * 60)
for c in comments:
    print(f"{c}  ->  {classify_sentiment(c)}")
