def format_key(name, surname):
  """This is a function that takes a name and a surname and then return name+surname titled"""
  f_name = name
  l_name = surname
  return f"{f_name} {l_name}".title()
  

print(format_key("tamila", "kosdauletova"))