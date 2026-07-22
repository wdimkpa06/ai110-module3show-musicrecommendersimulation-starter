# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

CipherMatch 1.0

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This system recommends songs from a small, fixed catalog based on how closely a song's genre, mood, and energy match a single stated listener preference. It's built for classroom exploration of how content-based recommendation works, not for real-world deployment — it has no user accounts, no listening history, and no way to learn or adapt over time.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The system compares each song in the catalog to a listener's stated preferences on three things: whether the genre matches exactly, whether the mood matches exactly, and how close the song's energy level is to the listener's target energy. A genre match is worth the most points, a mood match is worth half as much, and energy gets partial credit based on how close it is — an exact match earns full points, and the score shrinks the further apart they are. All songs get scored this way, then the highest-scoring songs are shown first.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog has 16 songs across 9 genres (pop, lofi, rock, ambient, jazz, synthwave, indie pop, hip-hop, r&b), each with 8 attributes (genre, mood, energy, tempo, valence, danceability, acousticness). Several genres — ambient and jazz — have only 1 song each, which limits how well the system can differentiate within those genres.
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system performs well when a listener's genre, mood, and energy preferences co-occur somewhere in the catalog — for the "Confident Hip-Hop," "High-Energy Hip-Hop," and "Chill R&B" profiles, the top-ranked song matched all three criteria and scored close to the maximum (3.9–4.0 out of a possible ~4.0), which matched intuition well. The energy-closeness formula also behaves correctly at the margins: songs with very close but non-identical energy still rank sensibly below exact or near-exact matches.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The catalog has 16 songs across 9 genres, but the distribution is uneven: lofi, hip-hop, and r&b each have 3 songs (19% of the catalog each, 56% combined), while rock, ambient, jazz, synthwave, and indie pop have only 1 song each. This means the system has much more room to differentiate between songs for a listener who prefers lofi, hip-hop, or r&b, since there are multiple songs to rank against each other within those genres. For a listener who prefers rock, ambient, jazz, synthwave, or indie pop, there's only one matching song available no matter how well or poorly it fits their mood and energy preferences — the system can't offer alternatives within that genre.

A second, more behavioral limitation showed up during evaluation (see Section 7): because genre match (+2.0) is weighted twice as heavily as mood match (+1.0), a listener's mood preference gets effectively overridden whenever it doesn't naturally co-occur with their genre preference in the catalog. In the adversarial test, a listener asking for "intense" r&b was shown r&b songs that weren't intense at all, ranked above songs that genuinely were intense but belonged to a different genre. This means the system can silently ignore part of what a listener explicitly asked for, without any indication to the listener that their mood preference wasn't actually satisfiable within their chosen genre.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

Tested four profiles: "Confident Hip-Hop," "High-Energy Hip-Hop," "Chill R&B," and an adversarial profile combining r&b genre with an "intense" mood and high target energy — a combination that doesn't actually exist in the catalog.

```
=== Confident Hip-Hop ===
City Lights Anthem — Score: 4.00 — genre match (+2.0), mood match (+1.0), energy closeness (+1.00)
Late Night Cipher — Score: 2.93 — genre match (+2.0), energy closeness (+0.93)
Corner Store Chronicles — Score: 2.77 — genre match (+2.0), energy closeness (+0.77)
Rooftop Lights — Score: 0.98 — energy closeness (+0.98)
Night Drive Loop — Score: 0.97 — energy closeness (+0.97)

=== High-Energy Hip-Hop ===
Late Night Cipher — Score: 3.95 — genre match (+2.0), mood match (+1.0), energy closeness (+0.95)
City Lights Anthem — Score: 2.88 — genre match (+2.0), energy closeness (+0.88)
Corner Store Chronicles — Score: 2.65 — genre match (+2.0), energy closeness (+0.65)
Storm Runner — Score: 1.99 — mood match (+1.0), energy closeness (+0.99)
Gym Hero — Score: 1.97 — mood match (+1.0), energy closeness (+0.97)

=== Chill R&B ===
Slow Burn — Score: 3.97 — genre match (+2.0), mood match (+1.0), energy closeness (+0.97)
Honest Conversations — Score: 2.95 — genre match (+2.0), energy closeness (+0.95)
Velvet Hours — Score: 2.90 — genre match (+2.0), energy closeness (+0.90)
Library Rain — Score: 1.00 — energy closeness (+1.00)
Coffee Shop Stories — Score: 0.98 — energy closeness (+0.98)

=== Adversarial (conflicting) ===
Velvet Hours — Score: 2.55 — genre match (+2.0), energy closeness (+0.55)
Slow Burn — Score: 2.48 — genre match (+2.0), energy closeness (+0.48)
Honest Conversations — Score: 2.40 — genre match (+2.0), energy closeness (+0.40)
Storm Runner — Score: 1.99 — mood match (+1.0), energy closeness (+0.99)
Gym Hero — Score: 1.97 — mood match (+1.0), energy closeness (+0.97)
```

The first three profiles all surfaced the expected song as the top result, with clean drop-offs in score as fewer criteria matched. The adversarial profile revealed a real limitation: because no r&b song in the catalog is tagged "intense," the top 3 results were r&b songs ranked only by energy closeness, while genuinely intense-mood songs (Storm Runner, Gym Hero) were pushed to 4th and 5th place despite matching the mood the listener asked for. This shows genre match dominates mood match strongly enough that a listener's stated mood preference can be effectively ignored when it doesn't co-occur with their genre preference anywhere in the data.

**Weight sensitivity experiment:** Halved genre's weight (2.0 → 1.0) and doubled energy's weight (1.0 → 2.0), keeping mood at 1.0, so genre and mood became equal. Re-running the adversarial profile ("intense" r&b) flipped the top 2 results: Storm Runner and Gym Hero — genuinely intense-mood songs from other genres — moved from 4th/5th place up to 1st/2nd, ahead of every off-mood r&b song. This confirms the bias described above was specifically caused by genre outweighing mood 2-to-1, not an inherent limitation of content-based scoring. After observing this, the original weights (genre 2.0, mood 1.0, energy 1.0) were kept for the shipped version, since equal-weighting genre and mood is a design choice with its own tradeoffs, not a strict improvement.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

- Add more songs per genre, especially ambient and jazz, so genre-based comparisons are more meaningful
- Let mood matching account for "close" moods (e.g., "confident" and "intense" might be considered partial matches) rather than exact-string-match only
- Add a diversity penalty so the top 5 don't skew toward one artist or genre

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

The biggest learning moment for me wasn't really the algorithm, it was how much time went into just getting the environment working. I ran into a broken import, a duplicate project folder that made pytest run the same test twice. None of that was about recommendation logic, but I couldn't write a single real line of code until it was sorted out.

I used AI for a few specific things, like the CSV loading function and getting the scoring formula right, but I double-checked everything before trusting it, because one answer it did give would have messed with my logic and crated a problem when trying a different mood. What surprised me most was how "smart" a simple weighted formula can feel. My genre/mood/energy scoring is just arithmetic, but in one test it ended up basically ignoring what a listener asked for mood-wise just because genre was weighted higher, which made me realize how much these small weighting choices shape what a system recommends, without anything technically being "wrong."