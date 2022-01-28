class FileManager:
    """A class to manage the best score file."""

    def __init__(self):
        """Initialize FileManager content."""

        self.filename = 'best_score.txt'
        self.filename_path = 'data/' + self.filename

        self.best_score = 0

    def save_data(self, score):
        """Saving the best score into the file."""

        # Checking if a new record has been set.
        if score > int(self.best_score):
            self.best_score = score

            # Preparation of data for saving.
            self.best_score = str(score)

            # Save the best score.
            with open(self.filename_path, 'w') as file_object:
                file_object.write(self.best_score)

    def load_data(self):
        """Loading the best score from the file."""

        try:
            with open(self.filename_path, 'r') as file_object:
                best_score = file_object.read()
                self.best_score = int(best_score)
        # If ensue FileNotFoundError or ValueError return best score as 0.
        except FileNotFoundError:
            return 0
        except ValueError:
            return 0

        return self.best_score
