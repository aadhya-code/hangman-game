import os
from playsound import playsound

def play_win_sound():
    path = os.path.join("static", "sounds", "win.mp3")
    if os.path.exists(path):
        playsound(path)
    else:
        print("[Missing win.mp3]")

def play_lose_sound():
    path = os.path.join("static", "sounds", "lose.wav")
    if os.path.exists(path):
        playsound(path)
    else:
        print("[Missing lose.wav]")

# Example usage:
if __name__ == "__main__":
    play_win_sound()
    play_lose_sound()
