import sys
import os
from common import *
from const import *
from string import Template
import getpass
import sys

# socket with bob, pretending to be alice.
# via fake buffer file
fake_BUFFER_FILE_NAME = 'buffer_new'
os.rename(BUFFER_DIR+BUFFER_FILE_NAME, BUFFER_DIR+fake_BUFFER_FILE_NAME)
dialog = Dialog('print')
socket_b, aes_b = setup('alice', BUFFER_DIR, fake_BUFFER_FILE_NAME)

#--------------------------------------------------------
# socket with alice, pretending to be bob
dialog = Dialog('print')
socket_a, aes_a = setup('bob', BUFFER_DIR, BUFFER_FILE_NAME)
#---------------------------------------------------------

####################
#--RELAY
####################

if len(sys.argv) == 2:
    if sys.argv[1] == '--relay':

        #receive and decrypt from alice first
        received_a = receive_and_decrypt(aes_a, socket_a)
        dialog.chat('Eve heard Alice said: "{}"'.format(received_a))

        #encrpyt then send to bob
        encrypt_and_send(received_a, aes_b, socket_b)
        dialog.info('Eve relayed to Bob!')

        #receive and decrypt from bob
        received_b = receive_and_decrypt(aes_b, socket_b)
        dialog.chat('Eve heard Bob said: "{}"'.format(received_b))

        #encrypt and send to alice
        encrypt_and_send(received_b, aes_a, socket_a)
        dialog.info('Eve relayed to Alice!')

#---------------------------------------------------------

####################
#--BREAK-HEART
####################

    if sys.argv[1] == '--break-heart':

        #receive and decrypt from alice first
        received_a = receive_and_decrypt(aes_a, socket_a)
        dialog.chat('Eve heard Alice said: "{}"'.format(received_a))

        #encrpyt then send to bob
        #altered alice's msg
        encrypt_and_send(BAD_MSG['alice'], aes_b, socket_b)
        dialog.info('Eve DESTROYED Bob!')

        #receive and decrypt from bob
        received_b = receive_and_decrypt(aes_b, socket_b)
        dialog.chat('Eve heard Bob said: "{}"'.format(received_b))

        #encrypt and send to alice
        encrypt_and_send(received_b, aes_a, socket_a)
        dialog.info('Eve CONFUSED Alice?')

#---------------------------------------------------------

####################
#--CUSTOM
####################

    if sys.argv[1] == '--custom':

        #receive and decrypt from alice first
        received_a = receive_and_decrypt(aes_a, socket_a)
        dialog.chat('Eve heard Alice said: "{}"'.format(received_a))

        #prompt user input
        dialog.prompt('Please input message to send to Bob...')
        send_to_bob = input()

        #encrpyt then send to bob
        #not alice's msg, but user input
        encrypt_and_send(send_to_bob, aes_b, socket_b)
        dialog.info('Eve sent random message to Bob!')

        #receive and decrypt from bob
        received_b = receive_and_decrypt(aes_b, socket_b)
        dialog.chat('Eve heard Bob said: "{}"'.format(received_b))

        #prompt user input
        dialog.prompt('Please input message to send to Alice...')
        send_to_alice = input()

        #encrypt and send to alice
        encrypt_and_send(send_to_alice, aes_a, socket_a)
        dialog.info('Eve CONFUSED Alice?')
