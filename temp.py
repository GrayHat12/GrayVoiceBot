import pafy

dat=pafy.new("https://www.youtube.com/watch?v=74yb9E3WY1I")

print(dat)

dat.getbest().download()