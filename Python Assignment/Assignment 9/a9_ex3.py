import argparse
import math
import multiprocessing

def sum_of_fractions(start, end):
    total = 0.0
    for k in range(start, end + 1):
        total += 1 / k
    return total

def main():
    parser = argparse.ArgumentParser(description="Approximate the Euler-Mascheroni constant.")
    parser.add_argument("-n", "--terms", type=int, default=1000, help="Number of terms in the sum.")
    parser.add_argument("-p", "--processes", type=int, default=1, help="Number of processes.")
    args = parser.parse_args()

    terms_per_process = args.terms // args.processes
    pool = multiprocessing.Pool(processes=args.processes)

    start_indices = [i * terms_per_process + 1 for i in range(args.processes)]
    end_indices = [(i + 1) * terms_per_process for i in range(args.processes)]

    results = pool.starmap(sum_of_fractions, zip(start_indices, end_indices))
    total_sum = sum(results)

    gamma_approximation = -math.log(args.terms) + total_sum

    print(f"Euler-Mascheroni constant approximation ({args.terms} terms): {gamma_approximation:.9f}")

if __name__ == "__main__":
    main()


