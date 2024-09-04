import re

def convert_to_cursed_js_safe(js_code):
    symbols = ['=', ';', ',', '+', '-', '*', '/', '%', '!', '&', '|', '<', '>', '?', ':', '.']
    
    token_regex = re.compile(r'(".*?"|\'.*?\'|\d+\.\d+|\d+|[a-zA-Z_$][a-zA-Z0-9_$]*|\.\s*[a-zA-Z_$][a-zA-Z0-9_$]*|\(|\)|{|}|=|;|,|\+|\-|\*|/|%|!|&|\||<|>|\?|:)')

    result = []
    
    for line in js_code.splitlines():
        tokens = token_regex.findall(line)
        
        for token in tokens:
            result.append(token.strip())
            result.append("\n")

    return ''.join(result)

def save_cursed_js_to_file(js_code, filename='cursified.js'):
    cursed_js_code = convert_to_cursed_js_safe(js_code)
    with open(filename, 'w') as file:
        file.write(cursed_js_code)

js_code = '''
const c = console;
const a = alert;
const v = "wtf?";
function o(){
    c.log(v);
    a(v);
}
o();
'''

save_cursed_js_to_file(js_code)
