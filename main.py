def main():
    """
    ##################################################
    # Complete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """

    celcius = int(input("Enter Temperature in Celcius:"))
    fahrenheit = celcius*9/5 +32

    print(f"Celsius: {celcius}")
    print(f"Fahrenheit: {fahrenheit:.2f}")
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
