from warnings import warn


def remove_characters(string, *args):
    for s in args:
        string = string.replace(s, "")
    return string


def find_element_limit(node):
    i = 0
    depth = 0
    while i < len(node):
        if node[i] in ['(', '{']:
            depth += 1
        elif node[i] in [')', '}']:
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def is_tuple_list(node):
    if len(node) > 5 and node[:5] == '((_t_':
        return True
    return False


def parse_tuples(node):
    """
    ((_t_('1: High probability (70% rejected)'), 1),(_t_('2: Intermediate probability (40% rejected)'), 2),(_t_('3: Low probability (20% rejected)'), 4),(_t_('1-2: High-inter probabilities'), 3),(_t_('1-3: All 3 probabilities thesholds'), 7)),'show_unknown', Boolean(),'nomenclature', ReadDiskItem('Nomenclature', 'Hierarchy'),'show_mesh', Boolean(),'white_mesh', ReadDiskItem('White SPAM mesh', 'anatomist mesh formats'),'mesh_TO_spam', ReadDiskItem('Transformation', 'Transformation Matrix'),)
    """
    if node[:2] == "((":
        node = node[1:]

    splits = node.split('(_t_(')[1:]
    items = []
    for split in splits:
        idx = split[:-1].rfind(',')
        items.append((
            remove_characters(split[:idx-1], "'", '"').strip(),
            split[idx+2:-2].strip()
        ))
    return items


def find_next_node_delimiter(string):
    par = string.find('(')
    vir = string.find(',')
    eg = string.find('=')
    pt = string.find(':')
    if par == -1:
        if vir == -1 and eg == -1 and pt == -1:
            return -1
        par = 100000
    if vir == -1:
        vir = 100000
    if eg == -1:
        eg = 100000
    if pt == -1:
        pt = 100000
    return min((vir, par, eg, pt))


def parse_node(node, text_elements):
    """
>$0$<,ReadDiskItem(>$1$<,>$2$<),>$3$<,Choice((_t_(>$4$<),1),(_t_(>$5$<),2),(_t_(>$6$<),4),(_t_(>$7$<),3),(_t_(>$8$<),7)),>$9$<,Boolean(),>$10$<,ReadDiskItem(>$11$<,>$12$<),>$13$<,Boolean(),>$14$<,ReadDiskItem(>$15$<,>$16$<),>$17$<,ReadDiskItem(>$18$<,>$19$<),
    """
    elements = []
    while len(node):
        idx = find_next_node_delimiter(node)

        if idx == 0:
            if node[idx] == ',':
                node = node[1:]
            if node.startswith('(_t_('):
                end = find_element_limit(node) + 1
                in_end = node[:end].rfind(',')
                id = node[in_end+1:end-1]
                elements.append(
                    (id, parse_node(node[5:in_end-1], text_elements)[0]))
                node = node[end+1:]
        elif idx == -1 or node[idx] == ",":
            # Next node is just a string
            key = node[:idx] if idx != -1 else node
            nodename = text_elements[key] if key in text_elements.keys(
            ) else key
            elements.append(nodename)
            node = node[idx+1:] if idx != -1 else ''
        elif node[idx] in ["(", "="]:
            nodename = node[0:idx]
            if node[idx] == "=":
                if node[idx+1] != '{':
                    end = node.find(',')
                    end = len(node) if end == -1 else end
                    elements.append((nodename, parse_node(
                        node[idx+1:end], text_elements)[0]))
                    node = node[end+1:]
                    continue
                else:
                    idx += 1
            end = find_element_limit(node) + 1
            # Next node is a Class
            nodename = node[0:idx]
            elements.append((nodename, parse_node(
                node[idx+1:end-1], text_elements)))
            node = node[end+1:]
        elif node[idx] == ':':
            end = node.find(',')
            if end == -1:
                end = len(node)
            elements.append(
                (text_elements[node[:idx]], text_elements[node[idx+1:end]]))
            node = node[end+1:]
        else:
            raise ValueError(
                "Delimiter was not attempted to be: {}".format(node[idx]))

        # nodename = nodename.replace("'", "").replace("(", "").replace(")", "")
    return elements


def next_text_delimiter(string):
    idx = string.find('"')
    idx2 = string.find("'")
    if idx == -1:
        return idx2
    if idx2 == -1:
        return idx
    return min((idx, idx2))


def hide_text(string):
    ostring = string
    text_elements = {}
    start = next_text_delimiter(string)
    while start > -1:
        end = string[start+1:].find(string[start]) + start + 1
        id = ">${:d}$<".format(len(text_elements))
        text_elements[id] = string[start+1:end]
        string = string[:start] + id + string[end+1:]
        start = next_text_delimiter(string)
    return string, text_elements


# def parse_node(node, go_deeper=True):
#     """

#     Signature('Commissure_coordinates', ReadDiskItem('Commissure coordinates', 'Commissure coordinates'), 'T1mri',
#             ReadDiskItem("T1 MRI", 'aims readable Volume Formats'), 'validation', Choice("Visualise", "Lock", "Unlock"),)

#     Inout string
#     'element1', [nodenameA]('elementA1', [nodenameB]('elementB1', 'elementB2'), 'elementA3'), [
#                             nodename]('elementB1', [nodenameB]('elementB1', 'elementB2'), 'elementA3'),
#     Output dict:
#     {
#         "element1": []
#         "nodenameA": [
#             "elementA1": None
#             "nodenameB": ['elementB1', 'elementB2'],
#             "elementA3": None
#     }
#     """
#     elements = []
#     while len(node):
#         par = node[1:].find('(')
#         vir = node.find(',')
#         par = par + 1 if par > -1 else 1000000
#         vir = vir if vir > -1 else 1000000
#         if par == 1000000 and vir == 1000000:
#             nodename = node
#             subelements = None
#             node = ''
#         elif vir > par:  # and not '"' in node[:par] and not '"' in node[:par]:
#             # Next node is a Class
#             nodename = node[0:par].strip()
#             end = find_element_limit(node) + 1
#             if len(nodename) == 0:
#                 warn('Empty node name')
#                 subelements = None
#             else:
#                 if is_tuple_list(node[par:end]):
#                     subelements = parse_tuples(node[par:end])
#                 elif go_deeper:
#                     subelements = parse_node(
#                         node[par:end], go_deeper=(nodename != "Choice" or node[par+1] == "("))
#                 else:
#                     subelements = node.split("','")
#                     if len(subelements) == 1:
#                         subelements = node.split('","')
#                     subelements = list(remove_characters(e, '"', "'")
#                                        for e in subelements)
#             node = node[end+2:]
#         else:
#             # Next node is just a string
#             nodename = node[:vir].strip()
#             subelements = None
#             node = node[vir+1:]
#         nodename = nodename.replace("'", "").replace("(", "").replace(")", "")
#         elements.append((nodename, subelements))
#     return elements
