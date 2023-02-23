# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_positions():
    h_p = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    v_p = ['8', '7', '6', '5', '4', '3', '2', '1']
    row = []
    rows = []
    for i in v_p:
        for j in h_p:
            row.append(i + j)
        rows.append(row)
        row = []

    print(rows)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_positions()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
