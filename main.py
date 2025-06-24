from mod_fsm import compute_binary_mod



def main():
    
    input_sequence = "110"
    fsm = compute_binary_mod(3)
    print(fsm.is_accepted(input_sequence))  # if the remainder is 0(state : {S0}) return True else False


if __name__ == "__main__":
    main()

