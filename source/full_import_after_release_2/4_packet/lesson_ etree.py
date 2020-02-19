# from functools import reduce
#
# print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))

from lxml import etree

def create_sample_element() -> etree._Element:
    '''
     - 3 ways of adding
    '''
    parent = etree.Element("parent")
    parent.append(etree.Element("child_0"))
    child2 = etree.SubElement(parent, "child_2")
    parent.insert(1, etree.Element("child_1"))

    ##<parent>
    ##  <child_0/>
    ##  <child_1/>
    ##  <child_2/>
    ##</parent>
    return parent

def print_formatted(element: etree._Element) -> None:
    print(
        etree.tostring(element, pretty_print=True).decode("utf-8")
    )

'''#########################
Pretty print 
#########################'''
# sample_element = create_sample_element()
# print_formatted(sample_element)


'''#########################
Creation 
#########################'''
# sample_element = create_sample_element()
# print_formatted(sample_element)


'''#########################
Navigation on element
#########################'''
# sample_element = create_sample_element()
# child_0_ref = sample_element[0]
# # WARNING! syntax incosistenccy
# print_formatted(sample_element)
# sample_element[0] = sample_element[1]
# print_formatted(sample_element)


'''#########################
Tag, attribute, innerHTML
#########################'''
# sample_element = create_sample_element()
# child_0_ref = sample_element[0]
# print_formatted(sample_element)
#
# child_0_ref.tag = "new_tag"                             # ~attribute
# child_0_ref.text = "new \"innerHTML\""                  # ~attribute
#
# child_0_ref.set("first_attribute", "some_value")        # setter
# attribute_value = child_0_ref.get("first_attribute")    # getter
#
# attributes_as_dict = child_0_ref.attrib                 # without setter/getter
# attributes_as_dict["second_attribute"] = "some_value"   #
#
# print_formatted(sample_element)


'''#########################
File - loading from
#########################'''
# path = "some_path"
# text_from_file = """<parent>
#   <child_0/>
#   <child_1/>
#   <child_2/>
# </parent>"""
#
# """1 way"""
# root = etree.XML(text_from_file)
# tree = etree.ElementTree(root)
# print_formatted(root)
#
# """2 way"""
# tree = etree.parse(path) # invalid path ehere
# root = tree.getroot()
# print_formatted(root)

