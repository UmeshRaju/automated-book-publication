# automated_book_workflow/main.py

from scraping.scraper import fetch_chapter_text
from scraping.screenshot import capture_screenshot
from agents.writer_agent import ai_writer_spin
from agents.reviewer_agent import ai_reviewer
from agents.editor_agent import human_edit_loop
from versioning.chromadb_store import save_version, search_versions
from retrieval.rl_search import rl_ranked_search

# At the end

URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"


def main():
    print("\n[STEP 1] Fetching and saving chapter...")
    raw_text = fetch_chapter_text(URL)
    capture_screenshot(URL)

    print("\n[STEP 2] AI Writer is rewriting the chapter...")
    rewritten = ai_writer_spin(raw_text)

    print("\n[STEP 3] AI Reviewer is refining the text...")
    reviewed = ai_reviewer(rewritten)

    print("\n[STEP 4] Human-in-the-loop editing...")
    final_version = human_edit_loop(reviewed)

    print("\n[STEP 5] Saving final version to ChromaDB...")
    save_version(final_version)

    print("\n[STEP 6] Testing intelligent retrieval...")
    search_versions("Gates of Morning Chapter 1")
    
    print("\n[STEP 7] RL-based Ranked Retrieval:")
    rl_ranked_search("Gates of Morning Chapter 1")


if __name__ == "__main__":
    main()
