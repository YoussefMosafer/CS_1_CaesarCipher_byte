import argparse
import sys


def caesar_shift(text: str, shift: int, mode: str) -> str:
    
    if mode == "decrypt":
        shift = -shift

    shift = shift % 26

    result = []
    for char in text:
        if char.isupper():
            shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            result.append(chr(shifted))
        elif char.islower():
            shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
            result.append(chr(shifted))
        else:
            result.append(char)

    return "".join(result)


def run_interactive():
    print("=" * 50)
    print("        CAESAR CIPHER TOOL")
    print("=" * 50)

    while True:
        mode = input("\nChoose mode - (E)ncrypt / (D)ecrypt / (Q)uit: ").strip().lower()

        if mode in ("q", "quit", "exit"):
            print("Exiting. Goodbye!")
            break

        if mode not in ("e", "encrypt", "d", "decrypt"):
            print("Invalid choice. Please enter E, D, or Q.")
            continue

        mode = "encrypt" if mode.startswith("e") else "decrypt"

        text = input("Enter your text: ")

        try:
            shift = int(input("Enter shift value (e.g., 3): ").strip())
        except ValueError:
            print("Shift must be a whole number. Try again.")
            continue

        output = caesar_shift(text, shift, mode)

        print("\n--- RESULT ---")
        print(f"Mode      : {mode}")
        print(f"Shift     : {shift}")
        print(f"Input     : {text}")
        print(f"Output    : {output}")
        print("-" * 30)


def main():
    parser = argparse.ArgumentParser(
        description="Caesar Cipher - encrypt or decrypt text with a configurable shift."
    )
    parser.add_argument("--mode", choices=["encrypt", "decrypt"], help="encrypt or decrypt")
    parser.add_argument("--text", type=str, help="The text to process")
    parser.add_argument("--shift", type=int, help="Shift value (integer, can be negative)")

    args = parser.parse_args()

    if args.mode and args.text is not None and args.shift is not None:
        output = caesar_shift(args.text, args.shift, args.mode)
        print(output)
        return

    if args.mode or args.text is not None or args.shift is not None:
        print("Error: --mode, --text, and --shift must ALL be provided together.")
        sys.exit(1)

    run_interactive()


if __name__ == "__main__":
    main()
