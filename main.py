import sys

from stats import GetWordCount
from stats import GetCharCounts;
from stats import SortDictionary;

def GetBookText(filepath):
  contents = "";
  with open(filepath) as f:
    contents = f.read();
    
  return contents;

def Main():
  if (len(sys.argv) == 1):
    print("Usage: python3 main.py <path_to_book>");
    sys.exit(1);
  
  filepath = sys.argv[1]; #"books/frankenstein.txt";
  fileText = GetBookText(filepath);
  wordCount = GetWordCount(fileText);
  charsCount = SortDictionary(GetCharCounts(fileText));
  
  print("============ BOOKBOT ============");
  print(f"Analyzing book found at {filepath}...");
  print("----------- Word Count ----------");
  print(f"Found {wordCount} total words")
  print("--------- Character Count -------");
  
  for c in charsCount:
    char = c["char"];
    count = c["count"];
    print(f"{char}: {count}");
  
  print("============= END ===============");
  
Main();