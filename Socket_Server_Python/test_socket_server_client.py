import socket
testinput1 = {
             'hello world!':'!dlrow olleh',
             'Python testing': 'gnitset nohtyP',
             'Teradici tech': 'chet icidareT',
          }
testinput2_withpunctuations  = {
             'Python!!': '!!nohtyP',
             'Unit Test@#': '#@tseT tinU',
          }
testinput3_casesense    = {
             'CEO and VP ': 'PV dna OEC',
             'Devops ROCKS': 'SKCOR  spoveD',
          }


def client(port, request):

    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()

    # connection to hostname on the port.
    try:
        s.connect((host, port))
    except socket.error as msg:
#        print 'Failed to Connect ' + str(msg[0]) + ' Message ' + msg[1]
        return -1

    # Receive no more than 1024
    s.senda (request.encode('ascii'))
    resp = s.recv(1024).decode('ascii').rstrip("\n")
    s.close()
    return resp

def test_port_connect():
    assert client(50007,"input") == "tupni"

def test_reverse_str():
    for str in testinput1.keys():
        assert client(50007, str) == testinput1[str]

def test_str_with_punctuations_and_spaces():
    for str in testinput2_withpunctuations.keys():
        assert client(50007, str) == testinput2_withpunctuations[str]

def test_str_for_case_sense():
    for str in testinput3_casesense.keys():
        assert client(8888, str) == testinput3_casesense[str]