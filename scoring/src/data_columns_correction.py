import pandas as pd
from scoring import constants as c

# NOTES
less_notes = pd.read_csv("data/less_notes.csv", sep="\t")
cn_notes = less_notes[c.noteTSVColumns]  # select + correct order
cn_notes.to_csv(
    "data/notes-00000.tsv",
    sep="\t",
    index=False,
    header=True  # <-- write header row
)

# RATINGS

ratings = pd.read_csv("data/ratings_subset.csv", sep="\t")

cn_ratings = ratings[c.ratingTSVColumns].copy()

# Add correlatedRater if the scorer expects it
cn_ratings["correlatedRater"] = 0

cn_ratings.to_csv("data/ratings-00000.tsv", sep="\t", index=False, header=True)