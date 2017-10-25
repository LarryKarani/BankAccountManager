from account import Account

def test_check_code():
	Larry = Account()
 
	assert Larry.check_code(100) == False

