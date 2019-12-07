'''
Print Option
'''
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def print_res(result_dict, nocons = False):
    #print("\n\033[4m\tResults\t\t\033[0m\n \033[4m\t\t\t\033[0m \n ")
    print( "\n" + color.UNDERLINE + color.BOLD + color.DARKCYAN + \
        "\tResults\t\t\n" + color.END)
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    if nocons == False:
        cons = result_dict['Beta IV'][0]
        cons_se = result_dict['Standard Error'][0]
        betas = result_dict['Beta IV'][1:]
        ses = result_dict['Standard Error'][1:]
        print("Cons:\t " + str(round(float(cons), 4)))
        print("\t(" + str(round(cons_se, 5)) + ")\t")
        print("------------------------")
        for i in range(0, len(betas)):
            print("\u03B2"+ str(i).translate(SUB) + "  :    " + \
                    str(round(float(betas[i]), 4)))
            print("\t(" + str(round(float(ses[i]), 5)) + ")\t")
            print("------------------------")
    elif nocons:
        betas = result_dict['Beta IV'][0:]
        ses = result_dict['Standard Error'][0:]
        for i in range(0, len(betas)):
            print("\u03B2"+ str(i).translate(SUB) + "  :    " + \
                    str(round(float(betas[i]), 4)))
            print("\t(" + str(round(float(ses[i]), 4)) + ")")
    print("\n")
