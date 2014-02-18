__author__ = 'dmitriy'

class StatDatum:
    def __init__(self, stat_node, parent_node, runs, recurses, total_run_time):
        self.stat_node = stat_node
        self.parent = parent_node
        self.runs = runs
        self.recurses = recurses
        self.total_run_time = total_run_time

        parent_node.add_new_child(stat_node)

    def time_per_run(self):
        return self.total_run_time/self.recurses

    def detailed_descip(self):
        return "{} -> {} -- {}(s) -- {} runs -- {}(s) per run"\
            .format(str(self.parent), str(self.stat_node),
                    self.total_run_time, self.recurses, self.time_per_run())

    def __str__(self):
        return "{}@{} -- {}(s) -- {} runs -- {}(s) per run"\
            .format(self.stat_node.name, self.parent.name,
                    self.total_run_time, self.recurses, self.time_per_run())


    def __lt__(self, other):
        priority_diff = self.stat_node.priority < other.stat_node.priority
        if priority_diff:
            return True
        else:
            if self.stat_node.priority == other.stat_node.priority:
                return self.time_per_run() > other.time_per_run()



class Function_Node:
    def __init__(self, name, origin, line, priority=0):
        self.name = name
        self.origin = origin
        self.line = line
        self.priority = priority
        self.children = []

    def __str__(self):
        return "{}[{}] - {}:{}".format(self.name, self.max_levels_below, self.origin, self.line)

    def function_id(self):
        return "{}@{}:{}".format(self.name, self.origin, self.line)

    def __eq__(self, other):
        return (self.name == other.name and
                self.origin == other.origin and
                self.line == other.line)

    def add_new_child(self, child_node):
       # / print "parent:", self.name, "--- child:", child_node.name

        self.max_levels_below = max(child_node.priority + 1, self.priority)
        self.children.append(child_node)
        # print self.max_levels_below, child_node.max_levels_below
