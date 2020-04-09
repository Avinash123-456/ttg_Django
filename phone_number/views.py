from django.shortcuts import render
from django .http import HttpResponse
import ttg
def index(request):
    return render(request,'index.html')

# def tt(request):
#     a = ttg.Truths(['p','q','r'])
#     b = ttg.Truths(['p', 'q', 'r'], ['p and q and r', 'p or q or r', '(p or (~q)) => r'])
#     variable_1 = request.GET.get('var1')
#     variable_2 = request.GET.get('var2')
#     condition_1 = request.GET.get('cond1')
#     condition_2 = request.GET.get('cond1')
#     variables = [variable_1,variable_2]
#     conditions = [condition_1,condition_2]
#     truth_table = ttg.Truths(variables,conditions)
#     print(truth_table)
#     data = {'truth_tables' : truth_table}
#     return render(request,'truth_table.html',data)

def tt(request):
    vars = request.POST.get('var')
    conds = request.POST.get('cond')
    option = request.POST.get('options')
    
    if(vars == '' or conds == ''):
        data = {'truth' : 'Please Fill the necessary filled...'}
        return render(request,'truth_table.html',data)
    else:
        variable_list = []
        for i in range(int(vars)):
            temp = request.POST.get(f"number_of_var{i}")
            variable_list.append(temp)

        condition_list = []
        for i in range(int(conds)):
            temp = request.POST.get(f"number_of_cond{i}")
            condition_list.append(temp)
        
        if option == 'False':
            truth = ttg.Truths(variable_list,condition_list,ints=False)
        else:
            truth = ttg.Truths(variable_list,condition_list,ints=True)

        valuation = truth.valuation()

        data = {'truth' : truth,'check' : valuation}
        
        return render(request,'truth_table.html',data)
