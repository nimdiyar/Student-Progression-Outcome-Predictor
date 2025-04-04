# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: 20230199/w2051582
# Date: 14/12/2023
# References : “Python Graphics Programming (Graphics.py 1): The Basics.” Www.youtube.com, www.youtube.com/watch?v=R39vTAj1u_8. Accessed 14 Dec. 2023.

from graphics import*

def get_mark(prompt):
    while True:
         try:
             mark = int(input(prompt))
             if mark in valid_inputs:
                 return mark
             else:
                 print("Out of Range")
         except ValueError:
            print("Integer required")

def calculate_result(pass_mark, defer_mark, fail_mark):
    if pass_mark + defer_mark + fail_mark == 120:
        if pass_mark == 120:
            return "Progress"
        elif pass_mark == 100:
            return "Progress(module trailer)"
        elif fail_mark >= 80:
            return "Exclude"
        elif pass_mark >= 0:
            return "Module retriever"
    else:
        return "Total is incorrect"

def count_results():
    if result == "Progress":
        result_count["progress"] += 1
    elif result == "Progress(module trailer)":
        result_count["trailer"] += 1
    elif result == "Module retriever":
        result_count["retriever"] += 1
    elif result == "Exclude":
        result_count["exclude"] += 1
    total_number_of_results = (result_count.get("progress") + result_count.get("trailer") +
                               result_count.get("retriever") + result_count.get("exclude"))
    return total_number_of_results

def display_title():
    title = Text(Point(170, 30), "Histogram Results")
    title.setSize(20)
    title.setStyle("bold")
    title.draw(win)

def designing_histogram(starting_x_point):
    for (result_type, height_of_bar) in result_count.items():
        #drawing bars
        bar = Rectangle(
              Point(starting_x_point, starting_y_point),
              Point(starting_x_point + width_of_bar, starting_y_point - height_of_bar * 10))
        bar.setFill(bar_colors.get(result_type))
        bar.draw(win)
        #displaying amounts
        amount = Text(
                 Point(starting_x_point + half_of_width_of_bar,
                       starting_y_point - height_of_bar * 10 - distance_between_amount_and_bar), height_of_bar)
        amount.draw(win)
        #displaying result type
        result = Text(
                 Point(starting_x_point + half_of_width_of_bar, starting_y_point + distance_between_bar_and_result),
                 result_type)
        result.draw(win)

        starting_x_point += width_of_bar + distance_between_2_bars

def draw_line():
    Line(Point(60, starting_y_point + 1), Point(win.getWidth() - 90, starting_y_point + 1)).draw(win)

def display_total():
    total_results = Text(Point(130, starting_y_point + 40), f"{total_number_of_results} outcomes in total")
    total_results.setSize(14)
    total_results.draw(win)

def printing_list():
    for i in (outcome_list):
        print(i[0], '-', i[1], ',', i[2], ',', i[3])

def textfile():
    #Input data saving to text file
    with open('E:\IIT\SD1 [PRO]\coursework\\textfile.txt', 'w') as textfile:
        for i in (outcome_list):
            textfile.write(str(i[0]) + '-' + (str(i[1]) + ',' + (str(i[2]) + ',' + (str(i[3]) + '\n'))))

    #Output retrieving from text file
    textfile = open('E:\IIT\SD1 [PRO]\coursework\\textfile.txt', 'r')
    lines = textfile.readlines()
    for l in (lines):
        print(l,end="")

#declaring variables
valid_inputs = [0, 20, 40, 60, 80, 100, 120]
result_count = {"progress":0,"trailer":0,"retriever":0,"exclude":0}
outcome_list = []
total_number_of_results = 0

while True:
    #checking the user is a student or a staff member
    user = input('Please enter "s" for student, "f" for staff : ')

    if user == 's' or user == 'f':
        break

    else:
        print('\nInvalid Input, Please enter "s" or "f"\n')
        continue
while True:
    #Getting user inputs for credits
    pass_mark = get_mark("Enter your total PASS credits: ")
    defer_mark = get_mark("Enter your total DEFER credits: ")
    fail_mark = get_mark("Enter your total FAIL credits: ")

    #calculating the result
    result = calculate_result(pass_mark,defer_mark,fail_mark)
    print("")
    print(result)

    #if the user is a student program will stop here
    if user == 's':
        break

    #appending result and input values to a list
    if result != "Total is incorrect":
        outcome_list.append([result, pass_mark, defer_mark, fail_mark])

    #counting number of results in each type and counting total results
        total_number_of_results = count_results()

    letter = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view result: ")
    print("")
    if letter == "q":
        # creating histogram
        win = GraphWin("Histogram", 500, 500)

        # declaring variables to design histogram by a loop
        width_of_bar = 50
        starting_x_point = 60
        starting_y_point = win.getHeight() - 60
        distance_between_2_bars = 50
        half_of_width_of_bar = width_of_bar / 2
        distance_between_amount_and_bar = 10
        distance_between_bar_and_result = 10
        bar_colors = {"progress": "lightyellow", "trailer": "lightgreen", "retriever": "orange","exclude": "lightpink"}

        display_title()
        designing_histogram(starting_x_point)
        draw_line()
        display_total()

        # closing histogram
        win.getMouse()
        win.close()

        # part 2
        # printing outcome list
        printing_list()
        print()

        # part 3
        # print part 2 outcome and accessing it to part 3 file writing
        textfile()
        break
