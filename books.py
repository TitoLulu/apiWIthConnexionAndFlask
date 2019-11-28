from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
BOOKS = {
    "The Alchemist": {
        "btitle": "The Alchemist",
        "bauthor": "Paulo Cuelho",
        "timestamp": get_timestamp()
    },
    "The Zahir": {
        "btitle": "The Zahir",
        "bauthor": "Paulo Cuelho",
        "timestamp": get_timestamp()
    },
    "Aleph": {
        "btitle": "Aleph",
        "bauthor": "Paulo Cuelho",
        "timestamp": get_timestamp()
    }
}

# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [BOOKS[key] for key in sorted(BOOKS.keys())]