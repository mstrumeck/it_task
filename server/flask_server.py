from flask import Flask, request

from server.fib import fib_sequence

app = Flask(__name__)


@app.route('/')
def main_view():
    """
    View with basic informations about application.
    :return: text with greetings and information about single endpoint
    """
    return f"""
    <h1>Welcome in Fibonaci Sequencer program!</h1>
    <p>Endpoint with sequencer are available from <b>{request.url}fib/<num></b> url,
     where 'num' is your number to transform</p>
    """


@app.route('/fib/<num>', methods=['GET', 'POST'])
def fib_sequence_view(num: int):
    """
    View with implemented fibbonaci sequence logic.
    :param num: the user number to calculate.
    :return: calculated number in string format.
    """
    if type(num) is int:
        return str(fib_sequence(num))
    return "Wrong value passed - the 'num' must be integer."


if __name__ == '__main__':
    app.run()
