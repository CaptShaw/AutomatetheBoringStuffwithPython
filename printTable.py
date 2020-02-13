#! /usr/bin/venv
# -*- coding:utf-8 -*-


def printTable(tableData):
    '''function for print table while taking list for argv
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

        apples Alice dogs
       oranges Bob   cats
      cherries Carol moose
        banana David goose
     '''
    colWidths = [[]] * len(tableData)
    output = [[]] * len(tableData[0])
    for i in range(len(tableData)):
        for j in tableData[i]:
            colWidths[i] = colWidths[i] + [len(j)]
        colWidths[i] = max(colWidths[i])
    print(colWidths)

    for i in range(len(tableData)):
        for j in range(len(tableData[0])):
            if i == 0:
                output[j] = output[j] + [tableData[i][j].rjust(colWidths[i])]
            else:
                output[j] = output[j] + [tableData[i][j].ljust(colWidths[i])]

    for j in range(len(tableData[0])):
        print(' '.join(output[j]))
        # print(output[j])

    return output


def enhenced(list):
    '''fixed up
    a more straight way to make a new list
    [[[] for _ in range(col)] for _ in range(row)]'''
    col = len(list)
    row = len(list[0])
    new_list = [[[] for _ in range(col)] for _ in range(row)]
    for i in range(col):
        for j in range(row):
            new_list[j][i] = list[i][j]

    print(new_list)


def main():

    tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

    printTable(tableData)
    enhenced(tableData)


if __name__ == '__main__':
    main()