class Node:
    def __init__(self, color, number=0):
        self.color = color
        self.number = int(number)

    def __str__(self):
        return f"{self.color} - {self.number}"

class Color:
    def __init__(self, name, parents=None, childs=None):
        self.name = name
        self.parents = []
        if parents:
            for parent in parents:
                self.add_parent(parent=parent)
        self.childs = []
        if childs:
            for child in childs:
                self.add_child(child=child)

    def add_parent(self, parent):
        self.parents.append(parent)

    def add_child(self, child):
        self.childs.append(child)

def parse_childs(line):
    if "no" in line:
        return None
    else:
        colors_splitted = line.split(",")
        colors=[]
        for color in colors_splitted:
            color_object = Node(
                color=color.strip().split(" ")[1] + " " +color.strip().split(" ")[2],
                number=color.strip().split(" ")[0]
            )
            colors.append(color_object)
        return colors
    # elif

def create_colors(lines):
    colors={}
    for line in lines:
        line=line.strip("\n")
        main_color = line.split(" bags contain")[0]
        if main_color not in colors.keys():
            color = Color(name=main_color)
            colors[main_color]=color
    return colors

def fill_parents_childs(line, colors):
    main_color = line.split(" bags contain")[0]
    child_colors = parse_childs(line=line.split(" bags contain")[1])
    if child_colors:
        for child_color in child_colors:
            if child_color.color in colors.keys():
                colors[child_color.color].add_parent(parent=main_color)
            colors[main_color].add_child(child=child_color)
    return colors

def get_parents(childs, colors):
    parents = []
    for child in childs:
        parents += colors[child].parents
    return parents

def get_childs(parents, colors):
    childs = []
    for parent in parents:
        childs += colors[parent.color].childs
    return childs


file1 = open('input.txt', 'r')
Lines = file1.readlines()

# Fill the tree of colors
colors = create_colors(lines=Lines)
for line in Lines:
    line = line.strip("\n")
    colors_temp = fill_parents_childs(line=line, colors=colors)
    colors = colors_temp

# Part 1
parents = get_parents(childs = ["shiny gold"], colors=colors)
total_parents = parents

while len(parents) != 0:
    parents = get_parents(childs=parents, colors=colors)
    total_parents += parents

print(f"--------Number of parents (Result First Part) {len(set(total_parents))}")

# Part 2
total_bags = 0
parent_node = Node(
    color="shiny gold",
    number=1
)
childs = get_childs(parents=[parent_node], colors=colors)

multiplier = 1
while(len(childs)>0):
    new_childs = []
    for child in childs:
        total_bags+=child.number
        grand_childs = get_childs(parents=[child], colors=colors)
        for grand_child in grand_childs:
            new_child=Node(
                color=grand_child.color,
                number=grand_child.number*child.number
            )
            new_childs.append(new_child)
    childs = new_childs

print(f"--------Total number of bags (Result Second Part) {total_bags}")

