import hvlcs
import datetime
import matplotlib.pyplot as plt

def main():
    run_tests = False

    K, vals, A, B = parse('data/example.in')
    max_value, lcs = hvlcs.hvlcs(K, vals, A, B)
    with open('data/output.out', 'w') as file:
        file.write(f'{max_value}\n{lcs}')

    # Tests
    if run_tests:
        test_cases = 13
        plt.figure(figsize=(10, 5))
        times = []
        for i in range(1, test_cases + 1):
            start_time = datetime.datetime.now()
            K, vals, A, B = parse(f'tests/test_{i}.in')
            max_value, lcs = hvlcs.hvlcs(K, vals, A, B)
            end_time = datetime.datetime.now()
            times.append((end_time - start_time).total_seconds())
            with open(f'tests/test_{i}.out', 'w') as file:
                file.write(f'{max_value}\n{lcs}')
        plt.plot(range(1, test_cases + 1), times, marker='o')
        plt.title('Execution Time for Test Cases')
        plt.xlabel('Test Case')
        plt.ylabel('Time (seconds)')
        plt.xticks(range(1, test_cases + 1))
        plt.grid()
        plt.savefig('tests/execution_times.png')
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