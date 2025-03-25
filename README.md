# 📚 UsefulPythonLib

**UsefulPythonLib** is a collection of handy, reusable Python scripts designed to simplify various tasks.

---

## 📁 File Structure
```yaml
UsefulPythonLib/
├── README.md # This README file
├── progress_bar.py # A simple progress bar utility
├── ebook.py # Create EPUB from chapters
├── another_useful_script.py # More useful scripts to come!
```

## 📦 Installation
Simply clone the repository to your local machine:
```bash
git clone https://github.com/nektarinne/UsefulPythonLib.git
```

## 📌 Available Scripts
1. progress_bar.py (Progress Bar Utility)

This script provides a simple, customizable progress bar for tracking progress in the terminal.

### 📖 progress() Function

```python
progress(numberOfCalls: int, message: str = "Progress")
```

Parameters:

- numberOfCalls (int): Total number of expected calls to progress(). Defines the completion percentage.

- message (str): Custom message to display. Truncated to 25 characters if longer.

### 📖 progressReset() Function
```python
progressReset()
```

Resets the progress tracking system. Always call this function before starting a new progress tracking sequence.

### 📌 Example Usage
Save the following code in your script or the Python console:
```python
from progress_bar import progress, progressReset
from time import sleep

# Reset progress tracking (recommended before starting a new process)
progressReset()

# Short process (10 steps)
for i in range(10):
    progress(10, message="Short Process")
    sleep(0.1)
print()  # Move to the next line after progress bar completion

# Reset progress tracking for the next process
progressReset()

# Long process (100 steps)
for i in range(100):
    progress(100, message="A longer process with a detailed message")
    sleep(0.1)
print()  # Move to the next line after progress bar completion

```
### 📊 Output Example
```
Short Process           | 100% | ██████████████████████████████████████████████████ | N/A
A longer process wit... | 54%  | ██████████████████████████████████████████████████ | 4s
```

2. ebook.py (Epub creator)

## 📦 Dependencies
Before using this script, ensure you have the ebooklib package installed. You can install it using pip:

```bash
pip install ebooklib
```

### create_epub() Function
```python
create_epub(title: str, author: str, filename: str, chapters: list[tuple[str, str]]) -> None
```

Parameters:
- title (str): The title of the book.
- author (str): The author's name.
- filename (str): The output filename for the EPUB file.
- chapters (list[tuple[str, str]]): A list of tuples where each tuple contains:
    - Chapter title (str)
    - Chapter content (str)

### 📌 Example Usage:
```python
from ebook import create_epub

title = "My First eBook"
author = "Jane Doe"
filename = "my_ebook.epub"
chapters = [
    ("Introduction", "Welcome to this book."),
    ("Chapter 1", "This is the first chapter."),
    ("Chapter 2", "This is the second chapter."),
]

create_epub(title, author, filename, chapters)
```

### 📊 Output:
```nginx
EPUB file "my_ebook.epub" has been created successfully!
```
This script allows you to generate EPUB files easily by providing a book title, author, and a structured list of chapters.



