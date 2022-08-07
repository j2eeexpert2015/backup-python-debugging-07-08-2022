
"""
remove_html_markup method takes a (HTML) string and returns the text without markup.
"""
def remove_html_markup(s):
    print("input,",s)
    tag = False
    out = ""

    for c in s:
        if c == '<':    # start of markup
            tag = True
        elif c == '>':  # end of markup
            tag = False
        elif not tag:
            out = out + c
    print("output:",out)
    return out

remove_html_markup("Here's some <strong>strong argument</strong>.")
remove_html_markup('<input type="text" value="<your name>">')