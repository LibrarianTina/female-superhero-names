#female superhero name possibilities using a nested for loop
first_names = ["Scary", "Super", "Kaleidescope"]
last_names = ["Black", "Trouble", "Vixon"]
full_names = []
for a_first_name in first_names:
  for a_last_name in last_names:
    full_names.append(a_first_name + " " + a_last_name)
    print(full_names)