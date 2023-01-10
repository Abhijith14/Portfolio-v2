from algo import *

f_read = open("./index.html", "r")
html_str = f_read.read()
html_str_orig = html_str


# html_str = update_badges(html_str, "", "Helklol", "Descaa", "Dates", 1)      
html_str = update_achievements(html_str, "", "Helklol", "Descaa", "Dates")     

# print(html_str)

save(html_str)
