def generate_diff(file1, file2):
    def replace_boll(text):
        result = text.replace("True", "true").replace("False", "false")
        return result
    result = ''
    for key in sorted(set(file1.keys()) | set(file2.keys())):
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                result += f'  {key}: {file1[key]}\n'
            else:
                result += f'- {key}: {file1[key]}\n'
                result += f'+ {key}: {file2[key]}\n'
        elif key in file1:
            result += f'- {key}: {file1[key]}\n'
        else:
            result += f'+ {key}: {file2[key]}\n'
    return replace_boll(result).strip()
