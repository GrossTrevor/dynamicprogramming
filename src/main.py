import hvlcs

def main():
    run_tests = True

    K, vals, A, B = parse('data/example.in')
    max_value, lcs = hvlcs.hvlcs(K, vals, A, B)
    with open('data/output.out', 'w') as file:
        file.write(f'{max_value}\n{lcs}')

    # Tests
    if run_tests:
        test_cases = 13
        for i in range(1, test_cases + 1):
            K, vals, A, B = parse(f'tests/test_{i}.in')
            max_value, lcs = hvlcs.hvlcs(K, vals, A, B)
            with open(f'tests/test_{i}.out', 'w') as file:
                file.write(f'{max_value}\n{lcs}')
    return 0

def parse(file_path):
    with open(file_path, 'r') as f:
        K = int(f.readline().strip())
        vals = []
        for _ in range(K):
            line = f.readline().strip().split()
            vals.append((line[0], int(line[1])))
        A = f.readline().strip()
        B = f.readline().strip()
    return K, vals, A, B

if __name__ == '__main__':
    main()