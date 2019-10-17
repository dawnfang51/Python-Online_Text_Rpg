import socket
import pickle
import time
import pickle

def send_data(conn, session):
    data = pickle.dumps(session)
    conn.send(data)
    

def host():
    port = 4579
    host = "127.0.0.1"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s1 = socket.socket()
    s1.bind((host, port))
    s.bind((host, port))
    session_list=[]

    BUFFER_SIZE = 100
    while True:
        print session_list
        session = ""
        session = s.recvfrom(BUFFER_SIZE)
        session_name = session[0]
        conn = session[1]
        print session
        print session_name
        
        if session_name == "Connect":
            s1.listen(1)
            conn, addr = s1.accept() 
            print conn
            send_data(conn, session_list)
            conn.close()
        else:
            session1 = list(pickle.loads(session[0]))
            print session1
            if session1[0][0] == "Disconnect":
                print session1[1][0]
                print session_list
                for session in session_list:
                    if session[0] == session1[1][0] and session[1] == session1[1][1]:
                        session1[1] = list(session)
                print session1[1] 
                session_list.remove(session1[1])
            elif session1[0][0] == "Full":
                for session in session_list:
                    if session == session1[1]:
                        session.append("Full")
            else:
                print session1
                print pickle.loads(session[0])
                session = pickle.loads(session[0])
                session_list.append(session)
        print session_list

                
if __name__ == "__main__":
    host()


