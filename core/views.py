from django.shortcuts import render

from escpos.printer import Network

# Replace '192.168.0.100' with your printer's IP address
PRINTER_IP = "192.168.178.177"


def print_receipt():
    """Print a simple receipt."""
    try:
        # Initialize the printer
        printer = Network(PRINTER_IP)

        # Print a test receipt6
        printer.text("\n\n\n\n\n\n\n")
        printer.text("001\n")
        printer.text("Cola!\n")
        printer.text("Hamburger\n")
        printer.cut()

        # Close the connection
        printer.close()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    print_receipt()
