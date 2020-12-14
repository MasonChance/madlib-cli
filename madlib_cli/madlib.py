

# define main program function

def main():
  path = 'assets/make_a_video_game.txt'
  welcome()
  parse_template(path)


def welcome():
  """ Begins program welcoming user
      Describes the program
      
      Input: N/A
      Output: str

      O(1)

  """
  print(
  '''Welcome to Madlibs! The game where we tell you a story based on words you give us! We will ask you for words based on their part of speach, for example, a noun; and will fill in, pre-determined blanks in the story, then print it for you and your friends to laugh about!
  ''')

# TODO: FIXME: For testing purposes the paths in this function are to a smaller sample file Be SURE to replace the path with the correct path on deployment. 

def read_template(path):
  """ gets template opens and reads
      returns a string

      Input: <-- path to file
      Output: --> str

      O(N)
  """
  with open(path, 'r') as t3mpl8:
    story_with_blanks = t3mpl8.read()
  return (story_with_blanks)

def parse_template(initial_str):
  """ Invokes: read_template(path)
      pulls the relevant template parts 
      return str with empty template braces && tuple of the words extracted
      
      Input <-- callback??
      Output --> str && tuple

      O(N)
  """
  return [get_stripped_template(initial_str),  get_parts(initial_str)]


def get_stripped_template(initial_string):
  t3mpl8_stripped = []
  for word in initial_string.split():
    if not word.startswith('{'):
      t3mpl8_stripped.append(word)
    else:
      t3mpl8_stripped.append('{}')

  
  return ' '.join(t3mpl8_stripped) + '.'
 
def get_parts(initial_str):
 
  parts_list = []
  
  for word in initial_str.split():
    print(word)
    if word.startswith('{'):
      word = word.strip('{')
      word = word.strip('.')
      word = word.strip('}')
      parts_list.append(word)

  return tuple(parts_list)


def get_user_words(initial_str):
  list_prompts = parse_template(initial_str)[1]
  answers = []
  for term in list_prompts:
    usr_input = input(term)
    answers.append(usr_input)

  return tuple(answers)



def merge(t3mpl8_story, results):
  a, b, c = results
  return t3mpl8_story.format(a, b, c)
  
