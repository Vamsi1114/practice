import pytest
from app.calculations import add,subtract,multiply,divide,BankAccount,User_exception

@pytest.fixture
def zero_bank_account():
  return BankAccount()

@pytest.fixture
def bank_account():
  return BankAccount(50)

@pytest.mark.parametrize("num1,num2,expected", [(3,2 ,5),(7,2,9),(5,5,10)])

def test_add(num1,num2 ,expected):
 print("testing add function")
 assert  add(num1,num2) == expected

def test_add2():
 assert add(5,3) == 8
 
def test_subtract():
  assert subtract(9,4) == 5

def test_multiply():
  assert multiply(3,4) == 12

def test_divide():
  assert divide(10,2) == 5 
 

def test_bank_set_initial_amount(bank_account):
  assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
  
  assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
  bank_account.withdraw(20)
  assert bank_account.balance == 30

def test_deposite(bank_account):
  bank_account.deposite(20)
  assert bank_account.balance == 70

@pytest.mark.parametrize("deposite,withdraw,expected", [(200,50 ,150),(700,200,500),(5000,500,4500)])

def test_bank_transaction(zero_bank_account,deposite,withdraw,expected):
  zero_bank_account.deposite(deposite)
  zero_bank_account.withdraw(withdraw)
  assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
  with pytest.raises(User_exception):
     bank_account.withdraw(200)

