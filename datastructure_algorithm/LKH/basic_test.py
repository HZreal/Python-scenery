import lkh

# doc: http://akira.ruc.dk/~keld/research/LKH-3/



# problem_str = requests.get('http://vrp.atd-lab.inf.puc-rio.br/media/com_vrp/instances/A/A-n32-k5.vrp').text
#

# path = '../A-n32-k5.vrp'
path = r'C:\Users\sizhong\file\project\SEV\LKH\CVRP\CVRP\INSTANCES\Belgium\A1.vrp'  # from CVRP.tgz
with open(path, 'r', encoding='utf8') as f:
    problem_str = f.read()

problem = lkh.LKHProblem.parse(problem_str)

solver_path = '../LKH/LKH-3.exe'

res = lkh.solve(solver_path, problem=problem, max_trials=10000, runs=1)
# res = lkh.solve(solver_path, problem=None, max_trials=10000, runs=1, problem_file=path)
print(res)
# [[30, 19, 9, 10, 23, 16, 11, 26, 6, 21], [27, 8, 14, 18, 20, 32, 22], [7, 4, 3, 24, 5, 12, 29, 15], [25, 28], [13, 2, 17, 31]]
# [[30, 21, 76, 58, 20, 27, 36, 66, 70, 57, 48, 16, 34, 65], [41, 22, 8, 2], [39, 73, 55, 10, 56, 42, 26, 47], [63, 13, 45, 6, 60, 28, 32, 18], [50, 74, 37, 68, 67, 54, 43], [35, 3, 38, 9, 69, 44, 17, 62, 79, 31], [72, 15, 49, 19, 80, 29, 53], [11, 64, 12, 25, 7, 24], [52, 78, 4, 40, 61, 75, 14], [71, 77, 51, 46, 23, 5, 33, 59]]


