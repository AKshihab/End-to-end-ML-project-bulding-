import os
import sys

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(file_name, line_number, str(error))
    return error_message

class UsvisaException(Exception):
    def __init__(self, error, error_detail: sys):
        # Initialize the parent Exception class with the error message
        super().__init__(error)
        
        # Generate the custom error message using the error_message_detail function
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self):
        # Return the custom error message
        return self.error_message