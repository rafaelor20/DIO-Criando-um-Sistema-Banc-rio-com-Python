class BankAccount:
    def __init__(self):
        self.balance = 0
        self.deposits = []
        self.withdrawals = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.deposits.append(amount)
            print(f'Deposit of ${amount:.2f} successful.')
        else:
            print('The deposit amount must be positive.')

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount and len(self.withdrawals) < 3 and amount <= 500:
                self.balance -= amount
                self.withdrawals.append(amount)
                print(f'Withdrawal of ${amount:.2f} successful.')
            elif len(self.withdrawals) >= 3:
                print('Daily withdrawal limit reached. Unable to withdraw more today.')
            elif amount > 500:
                print('The maximum withdrawal limit per transaction is $500.00.')
            else:
                print('Insufficient balance to make the withdrawal.')
        else:
            print('The withdrawal amount must be positive.')

    def statement(self):
        print('Transaction History:')
        if not self.deposits and not self.withdrawals:
            print('No transactions have been made.')
        else:
            for deposit in self.deposits:
                print(f'Deposit: ${deposit:.2f}')
            for withdrawal in self.withdrawals:
                print(f'Withdrawal: ${withdrawal:.2f}')
        print(f'Current balance: ${self.balance:.2f}')


def main():
    account = BankAccount()

    while True:
        print('\n=== Available Operations ===')
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Statement')
        print('4. Exit')

        option = int(input('Enter the number of the desired operation: '))

        if option == 1:
            deposit_amount = float(input('Enter the deposit amount: ').replace(',', '.'))
            account.deposit(deposit_amount)
        elif option == 2:
            withdrawal_amount = float(input('Enter the withdrawal amount: ').replace(',', '.'))
            account.withdraw(withdrawal_amount)
        elif option == 3:
            account.statement()
        elif option == 4:
            print('Exiting the program...')
            break
        else:
            print('Invalid option. Please try again.')


if __name__ == "__main__":
    main()
