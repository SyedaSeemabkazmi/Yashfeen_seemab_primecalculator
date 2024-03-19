
import streamlit as st

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    st.title("Prime or Composite Number Checker")
    num = st.number_input("Enter a number:")
    if st.button("Check"):
        if is_prime(num):
            st.write(f"{num} is a prime number.")
        else:
            st.write(f"{num} is a composite number.")

if __name__ == "__main__":
    main()
