import marshal
from StatDatum import StatDatum
from StatDatum import Function_Node

def get_data(filename):
    with open(filename,'rb') as data_file:
        data = marshal.load(data_file)

    return data


def process_data(data):
    stat_list = []
    func_list = {}
    for func in data:
        new_func = Function_Node(func[2], func[0], func[1])
        new_id = new_func.function_id()
        called_func = func_list.setdefault(new_id, new_func)

        func_data = data[func]
        call_list = func_data[4]

        for call in call_list:
            caller_func = Function_Node(call[2], call[0], call[1])
            caller_id = caller_func.function_id()
            parent_func = func_list.setdefault(caller_id, caller_func)

            call_data = call_list[call]

            stat_list.append(StatDatum(called_func, parent_func, call_data[0], call_data[1],
                                       call_data[3]))


    return stat_list


def prioritize_parents(function_list):

if __name__ == "__main__":
    data = get_data('result')
    stat_list = process_data(data)

    stat_list.sort()

    for i in xrange(len(stat_list)):
        print "{}: {}".format(i, stat_list[i])