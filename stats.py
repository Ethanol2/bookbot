def GetWordCount(text):
  words = text.split();
  return len(words);
  
def GetCharCounts(text):
  charsDict = {};
  
  for c in text:
    if (charsDict.get(c.lower()) is None):
      charsDict[c.lower()] = 1;
    else:
      charsDict[c.lower()] += 1;  
    
  return charsDict;

def SortParam(e):
  return e["count"];

def SortDictionary(originalDict):
  prettyList = [];
  for c in originalDict:
    prettyEntry = {"char":c,"count":originalDict[c]}
    prettyList.append(prettyEntry);
    
  prettyList.sort(reverse=True, key=SortParam);
  return prettyList;