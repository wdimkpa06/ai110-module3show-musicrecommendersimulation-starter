# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Real-world music recommenders like Spotify combine two approaches: collaborative filtering, which suggests songs based on what similar users have liked, and content-based filtering, which suggests songs based on the song's own attributes compared to a listener's known taste. Collaborative filtering is powerful once a platform has lots of user behavior data, but it struggles with brand-new songs that have no listening history yet ("cold start"). Content-based filtering solves this by working directly from a song's own features, so it can recommend something the moment it's added to a catalog. This project builds a purely content-based recommender: it has no user community or listening history to draw on, so it scores every song in the catalog against a single user's stated taste profile, based on how closely the song's attributes match what that user prefers.

Features:

Song objects use: title, artist, genre, mood, energy, tempo_bpm, valence, danceability, acousticness

UserProfile objects use: favorite_genre, favorite_mood, target_energy, likes_acoustic

Algorithm Recipe:

+2.0 points for a genre match
+1.0 point for a mood match
Up to +1.0 points for energy closeness, using max(0, 1 - abs(song.energy - user.target_energy)) scaled by weight

Potential Bias: This scoring system weights genre highest (+2.0), meaning it may over-prioritize genre matches even when a song's mood or energy is a much better fit for the listener. For example, a "confident hip-hop" profile could rank an intense hip-hop track above a genuinely confident-sounding song from another genre, simply because genre is worth more points than mood. The system may also underrepresent genres with fewer songs in the catalog (e.g., ambient or jazz, which currently have only one track each), since there's less variety for the scoring to differentiate between.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

Top recommendations:

City Lights Anthem — Score: 4.00 — genre match (+2.0), mood match (+1.0), energy closeness (+1.00)
Late Night Cipher — Score: 2.93 — genre match (+2.0), energy closeness (+0.93)
Corner Store Chronicles — Score: 2.77 — genre match (+2.0), energy closeness (+0.77)
Rooftop Lights — Score: 0.98 — energy closeness (+0.98)
Night Drive Loop — Score: 0.97 — energy closeness (+0.97)
```
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



