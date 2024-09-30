import sys
import time


class LoveCalculator:
    def __init__(self, lover1, lover2):
        self.lover1 = lover1
        self.lover2 = lover2
        self.love_score = 0

    def calculate_love_score(self):
        """Generate a love score based on lovers."""
        # Combine lovers into a single string
        combined_lovers = f"{self.lover1} loves {self.lover2}".lower()

        # Count occurrences of 'l', 'o', 'v', 'e', and 's'
        letter_counts = {char: combined_lovers.count(char) for char in "loves"}

        # Create a list of counts
        counts = list(letter_counts.values())

        # Reduce counts until we get to a two-digit score
        while len(counts) > 2:
            new_counts = []

            # Sum adjacent numbers
            for i in range(len(counts) - 1):
                new_counts.append(counts[i] + counts[i + 1])

            counts = new_counts     # Update counts to the new combined counts

        # Convert the final two counts into a percentage score
        if len(counts) == 2:
            love_score = (counts[0] * 10 + counts[1]) % 100     # Ensure it's a two-digit number
        else:
            love_score = counts[0]      # If there's only one number, use it directly

        self.love_score = love_score
        return int(self.love_score)

    def display_love_score(self):
        """Display the love score in a formatted message."""
        return f'Your love score for {self.lover1} and {self.lover2} is {self.love_score}%'

    def progress_bar(self, total, prefix='', length=30):
        """Display a progress bar."""
        for i in range(total + 1):
            # Calculate the progress
            percent = (i / total) * 100
            # Create the progress bar
            filled_length = int(length * i // total)
            bar = '█' * filled_length + '-' * (length - filled_length)
            # Print the progress bar
            sys.stdout.write(f'\r{prefix} |{bar}| {percent:.2f}% Complete')
            sys.stdout.flush()
            time.sleep(0.02)    # Simulate work being done
        print()     # Move to the next line after completion


def main():
    print('Welcome to...')
    print("""
      ,ad8PPPP88b,     ,d88PPPP8ba,
     d8P"      "Y8b, ,d8P"      "Y8b
    dP'           "8a8"           `Yd
    8(              "              )8
    I8                             8I
     Yb,                         ,dP
      "8a,                     ,a8"
        "8a,                 ,a8"
          "Yba             adP"
            `Y8a         a8P'
              `88,     ,88'
                "8b   d8"  THE LOVE
                 "8b d8"   CALCULATOR!
                  `888'
    """)
    # Get user input for lovers
    lover1 = input('Enter your name: ')
    lover2 = input('Enter your lover\'s name: ')

    # Create an instance of the LoveCalculator class
    calculator = LoveCalculator(lover1, lover2)

    # Calculate love score and show fake progress bar
    calculator.progress_bar(total=100, prefix='Calculating love...')
    calculator.calculate_love_score()

    # Display the love score result
    result = calculator.display_love_score()
    print(result)


if __name__ == '__main__':
    main()
