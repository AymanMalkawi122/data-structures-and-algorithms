from ..stack_and_queue.stack import Stack

def collapse(stack, bracket_map):
    closing_bracket = stack.pop()
    open_brackets = bracket_map.keys()
    while not stack.is_empty():
        char = stack.pop()
        if char in open_brackets:
            if bracket_map[char] == closing_bracket:
                return False
            return True
    return True

def validate_brackets(string):
    brackets = {
    "(": ")",
    "{": "}",
    "[": "]"
    }
    close_brackets = brackets.values()
    stack = Stack()
    unhandled_chars = False

    for char in string:
        stack.push(char)
        if char in close_brackets:
            unhandled_chars = collapse(stack, brackets)
            if unhandled_chars == True:
                print("unhandaled")
                return False
            
    if stack.is_empty():
        return True #valid
    return False #invalid
