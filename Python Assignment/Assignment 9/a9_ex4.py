import argparse
import subprocess

def run_program(program, args, timeout):
    try:
        print(f"Running program '{program}' with arguments {args} with a {timeout}s timeout")
        result = subprocess.run([program] + args, text=True, timeout=timeout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"The '{program}' finished with exit code {result.returncode}")

        if result.stdout:
            print(f"The '{program}' produced the following standard output:")
            print(result.stdout)

        if result.stderr:
            print(f"The '{program}' produced the following error output:")
            print(result.stderr)

    except FileNotFoundError:
        print(f"The specified program '{program}' could not be found")
    except subprocess.TimeoutExpired:
        print("The program execution timed out")

def main():
    parser = argparse.ArgumentParser(description="Run a program with arguments and handle exceptions.")
    parser.add_argument("-p", "--program", required=True, type=str, help="Name of the program to be executed.")
    parser.add_argument("-a", "--args", nargs="+", default=[], type=str, help="Arguments to be passed to the program.")
    parser.add_argument("-t", "--timeout", type=float, default=60, help="Timeout in seconds for the execution of the program.")
    args = parser.parse_args()

    run_program(args.program, args.args, args.timeout)

if __name__ == "__main__":
    main()


