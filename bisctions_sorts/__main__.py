from bisect import bisect

grades = 'FDCBA'
scores = [60, 70, 80, 90]
score_grade = lambda s: bisect(scores, s)
grade = lambda s: grades[score_grade(s)]

# def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#     i = bisect(breakpoints, score)
#     return grades[i]
# [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
