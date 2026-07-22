"""
Command line runner for the Music Recommender Simulation.
This file helps you quickly run and test your recommender.
"""
from src.recommender import load_songs, UserProfile, Recommender

HIGH_ENERGY_HIPHOP = UserProfile(favorite_genre="hip-hop", favorite_mood="intense", target_energy=0.9, likes_acoustic=False)
CHILL_RNB = UserProfile(favorite_genre="r&b", favorite_mood="sultry", target_energy=0.35, likes_acoustic=True)
ADVERSARIAL_CONFLICTING = UserProfile(favorite_genre="r&b", favorite_mood="intense", target_energy=0.9, likes_acoustic=True)

def main() -> None:
    songs = load_songs("data/songs.csv")
    rec = Recommender(songs)

    profiles = {
        "Confident Hip-Hop": UserProfile(favorite_genre="hip-hop", favorite_mood="confident", target_energy=0.78, likes_acoustic=False),
        "High-Energy Hip-Hop": HIGH_ENERGY_HIPHOP,
        "Chill R&B": CHILL_RNB,
        "Adversarial (conflicting)": ADVERSARIAL_CONFLICTING,
    }

    for label, user_prefs in profiles.items():
        print(f"\n=== {label} ===\n")
        recommendations = rec.recommend(user_prefs, k=5)
        for song in recommendations:
            explanation = rec.explain_recommendation(user_prefs, song)
            print(f"{song.title} — {explanation}")


if __name__ == "__main__":
    main()