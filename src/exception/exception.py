import sys


class CustomException(Exception):
    def __init__(self, error_msg, error_details: sys):
        self.error_msg = error_msg
        _, _, self.exc_tb = error_details.exc_info()
        self.line_no = self.exc_tb.tb_lineno
        self.fine_name = self.exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error [{self.error_msg}] occured at line no. [{self.line_no}] in file [{self.fine_name}]"


if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e:
        print(CustomException(e, sys))
