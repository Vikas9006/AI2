import itertools
from operator import truediv
from time import time
from tkinter import E
from typing import Tuple
from xml import dom
import copy
import pdb

# from csp import *


# initialising number of backtracks as 0
number_backtracks=0

def firstSum(n):
    return n * (n + 1) / 2

def lastSum(n):
    return n * (19 - n) / 2

# Function for getting lowest and highest values for given sum and number of cells
def minMax(Sum, numCells):
    high = Sum - firstSum(numCells - 1)
    high = min(9, high)

    low = Sum - lastSum(numCells - 1)
    low = max(0, low)
    return (low, high)

# Function to get dimension by taking a input from user
def getDimension():
    dimesionString = input()
    flag = 0
    n2 = ""
    for i in range(0, len(dimesionString), 1):
        if(flag == 1):
            n2 = n2 + dimesionString[i]
        if(dimesionString[i] == '='):
            flag = 1
    dimension = int(n2)
    return dimension

def getRowContent(row):
    comma = ','
    res = []
    element = ''
    for i in row:
        if i == comma:
            res.append(element)
            element = ''
        else:
            element = element + i
    res.append(element)
    return res

def parseRowContent(row):
    res = []
    for i in row:
        if i == '#':
            res.append(-1)
        else:
            element = int(i)
            res.append(element)
    return res

def crossProduct(possibleVals, listXij):
    newDomain = []
    for ele in listXij:
        newDomain.append(possibleVals[ele])
    res = list(itertools.product(*newDomain))
    return res

def isSatisfySum(tupleXij, Sum):
    # Sum is equal to given sum and all are distinct
    return (sum(list(tupleXij)) == Sum) and (len(set(tupleXij)) == len(tupleXij))

# def constraint(A, a, B, b):
#     if A in neighbours[B]:
#         # print("neighbours")
#         for i in range(0, len(neighbours[A])):
#             if (neighbours[A])[i] == B:
#                 return (a[i] == b)
#     # A and B are not neighbours
#     # print("not neighbours")
#     return True

def constraint(A, a, B, b):
    if isinstance(A[0], tuple) and isinstance(B[0], int):
        for i in range(0, len(neighbours[A])):
            if neighbours[A][i] == B:
                return a[i] == b

    elif isinstance(A[0], int) and isinstance(B[0], tuple):
        for i in range(0, len(neighbours[B])):
            if neighbours[B][i] == A:
                return b[i] == a

    return False
    """
    A = (x, y)
    a = 1-9
    B = ((x, y), bool)
        false => horizontal, true => vertical
    b = tuple (1-9)
    """

# Calculate ui
# mark constraints between xij and ui
def binarization(Sum, ulocation, listXij):
    ui = []
    domains[ulocation] = []
    tupleLen = len(listXij)
    minimax = minMax(Sum, tupleLen)
    for xij in listXij:
        tempDomain = copy.copy(domains[xij])
        deleted = 0
        for i, val in enumerate(tempDomain):
            # print(val, minimax, xij,domains[xij], tempDomain)
            if ((val < minimax[0]) or (val > minimax[1])):
                domains[xij].pop(i - deleted)
                deleted += 1
                # print(domains[xij])
        # print(domains)
    crsProduct = crossProduct(domains, listXij)
    # crsProduct = itertools.product()
    # print()
    for ele in crsProduct:
        if isSatisfySum(ele, Sum):
            domains[ulocation].append(ele)


allDigits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rows = getDimension()
columns = getDimension()
waste = input()
horizontal = []
vertical = []
constraintList = []
# domains:dict[tuple, list] = {}
variables = []
u_variables = []
neighbours = {}
domains = {}
u_variables_h = []
u_variables_v = []
board = []

for i in range(0, rows):
    row = input()
    res = getRowContent(row)
    content = parseRowContent(res)
    horizontal.append(content)

trash = input()

for i in range(0, rows):
    row = input()
    res = getRowContent(row)
    content = parseRowContent(res)
    vertical.append(content)

for i in range(0, rows):
    board.append([])
    for j in range(0, columns):
        if vertical[i][j] == 0 and horizontal[i][j] == 0:
            board[i].append(0)
        elif vertical[i][j] == -1 and horizontal[i][j] == -1:
            board[i].append(-1)
        else:
            board[i].append((vertical[i][j], horizontal[i][j]))
# print(board)
# exit()

for i in range(0, rows):
    for j in range(0, columns):
        if vertical[i][j] == 0:
            variable = (i, j)
            variables.append(variable)
            domains[variable] = copy.copy(allDigits)
        
        elif vertical[i][j] != -1 or horizontal[i][j] != -1:
            if vertical[i][j] != -1:
                u_variable = ((i, j), True)
                variables.append(u_variable)
                # to be removed
                counter = 0
                for k in range(i+1, rows):
                    if vertical[k][j] != 0:
                        break
                        
                    neighbour_box = (k, j)
                    if u_variable not in neighbours:
                        neighbours[u_variable] = []
                    neighbours[u_variable].append(neighbour_box)

                    if neighbour_box not in neighbours:
                        neighbours[neighbour_box] = []
                    neighbours[neighbour_box].append(u_variable)
                counter += 1

            if horizontal[i][j] != -1:
                u_variable = ((i, j), False)
                variables.append(u_variable)
                # to be removed
                counter = 0
                for k in range(j+1, columns):
                    if vertical[i][k] != 0:
                        break
                        
                    neighbour_box = (i, k)
                    if u_variable not in neighbours:
                        neighbours[u_variable] = []
                    neighbours[u_variable].append(neighbour_box)

                    if neighbour_box not in neighbours:
                        neighbours[neighbour_box] = []
                    neighbours[neighbour_box].append(u_variable)
                counter += 1

# Calculating variables and u_variables
# for x, r in enumerate(horizontal):
#     for y, c in enumerate(r):
#         if c == 0 and (x, y) not in variables:
#             variables.append((x, y))
#             domains[(x, y)] = copy.copy(allDigits)
            # neighbours[(x, y)] = []

# for x, r in enumerate(vertical):
#     for y, c in enumerate(r):
#         if c > 0:
#             for i in range(x + 1, len(vertical)):
#                 if horizontal[i][y] == 0:
#                     neighbours[((x, y), True)].append((i, y))
#                     neighbours[(i, y)].append(((x, y), True))
#                 else:
#                     break

# for x, r in enumerate(vertical):
#     for y, c in enumerate(r):
#         if c > 0:
#             u_variables_v.append(((x, y), True))
#             neighbours[((x, y), True)] = []

# i = 0
# j = 0
# while i < len(u_variables_h) or j < len(u_variables_v):
#     if i < len(u_variables_h):
#         u_variables.append(u_variables_h[i])
#         i += 1
#     if j < len(u_variables_v):
#         u_variables.append(u_variables_v[j])
#         j += 1

# for x, r in enumerate(horizontal):
#     for y, c in enumerate(r):
#         if c > 0:
#             for i in range(y + 1, len(r)):
#                 if horizontal[x][i] == 0:
#                     neighbours[((x, y), False)].append((x, i))
#                     neighbours[(x, i)].append(((x, y), False))
#                 else:
#                     break

# for x, r in enumerate(vertical):
#     for y, c in enumerate(r):
#         if c > 0:
#             for i in range(x + 1, len(vertical)):
#                 if horizontal[i][y] == 0:
#                     neighbours[((x, y), True)].append((i, y))
#                     neighbours[(i, y)].append(((x, y), True))
#                 else:
#                     break

# Calculating variables (ui)
for x, r in enumerate(horizontal):
    for y, c in enumerate(r):
        if c > 0:
            binarization(horizontal[x][y] ,((x, y), False), neighbours[((x, y), False)])

for x, r in enumerate(vertical):
    for y, c in enumerate(r):
        if c > 0:
            binarization(vertical[x][y] ,((x, y), True), neighbours[((x, y), True)])
# print(domains)
# print(u_variables_h)
# print(u_variables_v)
# print(u_variables)
# **********************
# Debugging
# print("Variables")
# print(variables)
# print("Domains")
# print(domains)
# print("Neighbours")
# print(neighbours)

# Intialization
"""
variable    === cell in grid which is to be filled (we will make a list out of them)
                arr[i][j][0] == 'W'
domains     === range of values that can be filled in a particular cell 
                (dictionary of the form {variable: list of values})
                arr[i][j][1]
constraints === 
neighbours  === cells that are in same row or column having an constraint with given cell
                (dictionary of the form {variable: list of neighbours})
"""

# *****************************************************************************
class csp():

    def __init__(self, variables, u_variables, domains, neighbours, constraints) -> None:
        self.variables = variables
        self.u_variables = u_variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints
        self.assign_count = 0
        self.total_assigns = 0
        self.curr_domains = None

    def assign(self, var, val, assignment):
        assignment[var] = val
        self.assign_count += 1
        self.total_assigns += 1

    def unassign(self, var, assignment):
        if var in assignment:
            assignment.pop(var)

    def isConflict(self, var1, val1, var2, assignment):
        # print("var1, val1, var2, assignment = ", var1, val1, var2, assignment)
        if var2 in assignment and not self.constraints(var1, val1, var2, assignment[var2]):
            return True
        return False

    def count_conflicts(self, var, val, assignment):
        count = 0
        # print(self.neighbours[var])
        for neighbour in (self.neighbours)[var]:
            if self.isConflict(var, val, neighbour, assignment):
                count += 1
        # if count == 0:
            # for neighbour in (self.neighbours)[var]:
                # self.assign(neighbour, )
        return count

    def suppose(self, var, value):
        """Start accumulating inferences from assuming var=value."""
        self.support_pruning()
        removals = [(var, a) for a in self.curr_domains[var] if a != value]
        self.curr_domains[var] = [value]
        return removals

    def support_pruning(self):
        """Make sure we can prune values from domains. (We want to pay
        for this only if we use it.)"""
        if self.curr_domains is None:
            self.curr_domains = {v: list(self.domains[v]) for v in self.variables}

    def restore(self, removals):
        """Undo a supposition and all inferences from it."""
        for B, b in removals:
            self.curr_domains[B].append(b)

    def prune(self, var, value, removals):
        """Rule out var=value."""
        self.curr_domains[var].remove(value)
        if removals is not None:
            removals.append((var, value))

    def getDomainValue(self, var):
        return self.domains[var]
    
    def getNeighbours(self, var):
        return self.neighbours[var]
"""
constraints 
    
"""
# *******************************************************************************

def forward_checking(csp, var, value, assignment, removals):
    """Prune neighbor values inconsistent with var=value."""
    csp.support_pruning()
    for B in csp.neighbours[var]:
        if B not in assignment:
            for b in csp.curr_domains[B][:]:
                if not csp.constraints(var, value, B, b):
                    csp.prune(B, b, removals)
            if not csp.curr_domains[B]:
                return False
    return True

def revise(csp, Xi, Xj, removals, checks=0):
    """Return true if we remove a value."""
    revised = False
    for x in csp.curr_domains[Xi][:]:
        # If Xi=x conflicts with Xj=y for every possible y, eliminate Xi=x
        # if all(not csp.constraints(Xi, x, Xj, y) for y in csp.curr_domains[Xj]):
        conflict = True
        for y in csp.curr_domains[Xj]:
            if csp.constraints(Xi, x, Xj, y):
                conflict = False
            checks += 1
            if not conflict:
                break
        if conflict:
            csp.prune(Xi, x, removals)
            revised = True
    return revised, checks

def AC3(csp, queue=None, removals=None):
    """[Figure 6.3]"""
    if queue is None:
        queue = {(Xi, Xk) for Xi in csp.variables for Xk in csp.neighbours[Xi]}
    csp.support_pruning()
    checks = 0
    while queue:
        (Xi, Xj) = queue.pop()
        revised, checks = revise(csp, Xi, Xj, removals, checks)
        if revised:
            if not csp.curr_domains[Xi]:
                return False, checks  # CSP is inconsistent
            for Xk in csp.neighbours[Xi]:
                if Xk != Xj:
                    queue.add((Xk, Xi))
    return True, checks  # CSP is satisfiable

def ORDER_DOMAIN_VALUES(var, assignment, csp):
    return csp.domains[var]

# Function iterates over variables and which one is not assigned, return that element
def SELECT_UNASSIGNED_VARIABLE(assignment, csp):
    for var in csp.variables:
        if var not in assignment:
            return var
    # All element are assigned, return None
    return None

# def RECURSIVE_BACKTRACKING(assignment, csp):
#     # pdb.set_trace()
#     print("Assignment")
#     if csp.assign_count == len(csp.u_variables):
#         return assignment
#     print(assignment)
#     print()
#     var = SELECT_UNASSIGNED_VARIABLE(assignment,csp)
#     # print(var)
#     # print(var, csp.getDomainValue(var), csp.getNeighbours(var))
#     # print(assignment)
#     # for value in ORDER_DOMAIN_VALUES(var, assignment, csp):
#     # print("Domain =", csp.domains[var])
#     # if var == ((0, 1), True):
#         # pdb.set_trace()
#     for value in csp.domains[var]:
#         if var in assignment:
#             assignment.pop(var)
#             for neighbour in csp.neighbours[var]:
#                 if neighbour in assignment:
#                     for neighbourOfNeighbour in csp.neighbours[neighbour]:
#                         if (neighbourOfNeighbour != var) and (neighbourOfNeighbour not in assignment):
#                             assignment.pop(neighbour)
#         # print("Value taken =", value)
#         if csp.count_conflicts(var, value, assignment) == 0:
#             csp.assign(var, value, assignment)
#             # print(var, value)
#             # Assign each neighbour also
#             for i, neighbour in enumerate(csp.neighbours[var]):
#                 # if neighbour not in assignment:
#                 assignment[neighbour] = value[i]

#             result = RECURSIVE_BACKTRACKING(assignment, csp)
#             # print(var, "recursive function is called", result)
#             if result is not None:
#                 return assignment
#     # print("Removed", var, None)
#     csp.unAssign(var, assignment)
#     for neighbour in csp.neighbours[var]:
#         present = False
#         for neighbourOfNeighbour in csp.neighbours[neighbour]:
#             if neighbourOfNeighbour in assignment:
#                 present = True
#         if not present:
#             if neighbour in assignment:
#                 assignment.pop(neighbour)
#             # print("Removed", neighbour)
#     csp.assign_count -= 1
#     # print(csp.assign_count)
#     return None

def NO_INFERENCE(csp, var, value, assignment, removals):
    return truediv

def RECURSIVE_BACKTRACKING(csp, assignment, select_unassigned_variable, order_domain_values, inference):

    if len(assignment) == len(csp.variables):
        return assignment
    # print(assignment)
    var = select_unassigned_variable(assignment, csp)
    for value in order_domain_values(var, assignment, csp):
        if 0 == csp.count_conflicts(var, value, assignment):
            csp.assign(var, value, assignment)
            removals = csp.suppose(var, value)
            if inference(csp, var, value, assignment, removals):
                result = RECURSIVE_BACKTRACKING(csp, assignment, select_unassigned_variable, order_domain_values, inference)
                if result is not None:
                    return result
            csp.restore(removals)
    csp.unassign(var, assignment)
    return None

def BACKTRACKING_SEARCH(csp, select_unassigned_variable=SELECT_UNASSIGNED_VARIABLE,
                        order_domain_values=ORDER_DOMAIN_VALUES, inference=forward_checking):
    return RECURSIVE_BACKTRACKING(csp, {}, select_unassigned_variable, order_domain_values, inference)

def mac(csp, var, value, assignment, removals, constraint_propagation=AC3):
    """Maintain arc consistency."""
    return constraint_propagation(csp, {(X, var) for X in csp.neighbours[var]}, removals)
# *****************************************************************************

# print(domains)

CSP = csp(variables, u_variables, domains, neighbours, constraint)

intial_time = time()
sol = BACKTRACKING_SEARCH(CSP, inference=mac)
time_taken = time() - intial_time

print("Solution")
print(sol)
print("Time taken", time_taken)
print("Total assignments did", CSP.total_assigns)
print("Total number of assignments did", number_backtracks)