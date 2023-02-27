def group_by_owners(files):
    group_by = {}
    for val in files.values():
        group_by.update({val: [k for k, v in files.items() if v == val]})

    return group_by


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))
