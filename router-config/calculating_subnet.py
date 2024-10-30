import math
def take_input():
    while True:
        try:
            subnets = int(input("How many subnets do u need?"))
            return math.ceil(math.log2(subnets))
        except ValueError as e:
            print(f"exception: {e}")
            continue
def calculate_mask(bits):
    return 2**(8 - bits)
def calculate_ip(bits):
    return 2**(8 - bits)
def display_results(mask, bits):
    # Calculate amount of hosts per subnet (minus 2 for network- and broadcastaddress)
    hosts_per_subnet = (2 ** (8 - bits)) - 2
    
    # Display subnets and amount of loaned bits
    print(f"You loaned {bits} bit(s), your new subnet mask ends with /{24 + bits}!")
    print(f"Each subnet can have {hosts_per_subnet} usable hosts.")
    subnet_size = 2 ** (8 - bits)
    counter = 0
    for i in range(0, 256, subnet_size):
        # IP-range for each subnet
        print(f"Range {counter}: {i} - {i + subnet_size - 1}")
        counter += 1
        
        # Limit each subnet to stay within 255
        if i + subnet_size >= 256:
            break
def main():
    bits = take_input()
    mask = calculate_mask(bits)
    display_results(mask, bits)
if __name__ == "__main__":
    main()