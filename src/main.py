"""
Command line runner for the Music Recommender Simulation.
This file helps you quickly run and test your recommender.
"""
from src.recommender import load_songs, UserProfile, Recommender


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Default profile: confident hip-hop listener
    user_prefs = UserProfile(
        favorite_genre="hip-hop",
        favorite_mood="confident",
        target_energy=0.78,
        likes_acoustic=False,
    )

    rec = Recommender(songs)
    recommendations = rec.recommend(user_prefs, k=5)

    print("\nTop recommendations:\n")
    for song in recommendations:
        explanation = rec.explain_recommendation(user_prefs, song)
        print(f"{song.title} — {explanation}")
        print()


if __name__ == "__main__":
    main()