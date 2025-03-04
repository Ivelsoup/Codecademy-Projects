last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [["Physics", 98], ["Calculus", 97], ["Peotry", 85], ["history", 88]]

gradebook.append(["Computer Science", 100])
gradebook.append(["Visual arts", 93])

gradebook[-1][-1] = gradebook[-1][-1] + 5 

# Switch Peotry to a pass/fail system, rather than a grade:
gradebook[2].remove(85)

gradebook[2].append("Pass")

full_gradebook = last_semester_gradebook + gradebook 

print(full_gradebook)
