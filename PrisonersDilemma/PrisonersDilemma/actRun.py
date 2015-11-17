''' this file actually runs the tournement '''
import prisoners_dilemma
def main():
    prisoners_dilemma.play_tournament(int(raw_input("Players: ")))

if __name__ == '__main__':
    main()