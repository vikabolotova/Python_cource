import numpy as np
import re

class AnalysDataFile:
  def __init__(self, path):
    self.path = path
    self.data = []


  def read_file(self):
    self.data = np.genfromtxt(self.path,dtype=str, delimiter='\n')
    print(self.data)

  def search_text(self, pattern):
    if self.data is None:
      print("Данные из файла не были прочитаны.")
      return []

    str_data = ''.join(self.data)
    matches = []
    l = re.search(pattern, str_data)
    matches.append(l.group())

    return matches

res = AnalysDataFile('file.txt')
res.read_file()
search_pattern = r'\d{6}'
result = res.search_text(search_pattern)

print(result)