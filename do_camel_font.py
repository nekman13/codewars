def do_to_camel_text(text):
    text = text.replace("_", "-")
    lst_text = text.split("-")
    part_of_result = " ".join(lst_text[1:]).title().replace(" ", "")
    result = lst_text[0] + part_of_result
    return result


print(do_to_camel_text("Hello_world-world"))
