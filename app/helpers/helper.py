import re
from datetime import datetime
import pytz


def stip_string(text:str):
    """This function is used to remove the whitespaces from the string.
        EXample: 
                str_1 = "  Hire freelance developers  "
                output = str_1.strip()
                # Output = "Hire freelance developers"
    Args:
        text (str): Text refers to the string 
                    containing the whitespaces.
    
    str: String which all the leading and trailing whitespaces removes.
    """
    text = text.strip()
    return text

def remove_spacial_chars(text:str):
    removed_space = re.sub(r"\s+", "", text)
    removed_special_chars = re.sub(r"^ [a-zA-Z0-9]+",'',removed_space)
    return removed_special_chars

def get_current_datetime():
    IND = pytz.timezone("Asia/KolKata")
    current_dt = datetime.now(IND)
    return current_dt

def convert_date_format(input_date):
    # Parse the input date using the input format
    input_format = "%d/%m/%Y %I:%M %p"
    parsed_date = datetime.strptime(input_date, input_format)
    
    # Convert the parsed date to the desired output format
    output_format = "%m-%d-%Y %H:%M:%S"
    converted_date = parsed_date.strftime(output_format)
    
    return converted_date
