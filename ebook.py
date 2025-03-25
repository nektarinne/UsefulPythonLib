
from ebooklib import epub

BOOK_LANGUAGE = 'en'

def create_epub(title: str, author: str, filename: str, chapters: list[tuple[str, str]]) -> None:
    """
    Creates an EPUB file with the given title, author, and chapters.

    Parameters:
        title (str): The title of the book.
        author (str): The author's name.
        filename (str): The output filename for the EPUB file.
        chapters (list[tuple[str, str]]): A list of tuples where each tuple contains a chapter title and its content.
    
    Returns:
        None
    """
    book = epub.EpubBook()
    
    # Set metadata
    book.set_title(title)
    book.set_language(BOOK_LANGUAGE)
    book.add_author(author)
    
    # Create chapters
    epub_chapters = []
    for i, (chapter_title, chapter_content) in enumerate(chapters, start=1):
        chapter = epub.EpubHtml(title=chapter_title, file_name=f'chap_{i}.xhtml', lang=BOOK_LANGUAGE)
        chapter.content = f'<h1>{chapter_title}</h1>\n{chapter_content}'
        book.add_item(chapter)
        epub_chapters.append(chapter)
    
    # Define table of contents and spine
    book.toc = (epub_chapters)
    book.spine = ['nav'] + epub_chapters
    
    # Add navigation files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    
    # Write to file
    epub.write_epub(filename, book, {})
    print(f'EPUB file "{filename}" has been created successfully!')


if __name__ == "__main__":
    # Example usage
    title = "Sample Book"
    author = "John Doe"
    filename = "sample_book.epub"
    chapters = [
        ("Introduction", "This is the introduction content."),
        ("Chapter 1", "This is the content of the first chapter."),
        ("Chapter 2", "This is the content of the second chapter."),
    ]

    create_epub(title, author, filename, chapters)