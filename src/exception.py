import sys

def error_message_details(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in file: [{0}] on line number [{1}] with error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        self.error_message = error_message

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":
    try:
        raise CustomException("This is a test error message", sys)
    except CustomException as e:
        print(e)
        print(error_message_details(e, sys))