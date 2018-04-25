#!/usr/bin/python

"""
This is an example of how you could call out to a central service to add 2FA to applications secured by PAM.
The most common example of this would be SSH.

There is a lot of room to improve on this script, don't use it in production as it stands.

Michael Fincham <michael@hotplate.co.nz>
"""

import requests

DEFAULT_USER    = "nobody"

def pam_sm_authenticate(pamh, flags, argv):
  try:
    user = pamh.get_user(None)
  except pamh.exception, e:
    return e.pam_result
  if user == None:
    pam.user = DEFAULT_USER

  try:
    user_status = requests.get('https://accounts.example.com/pam/new/%s on %s as %s' % (pamh.service, pamh.rhost, user)).json()
    pamh.conversation(pamh.Message(pamh.PAM_PROMPT_ECHO_OFF,"\nVerify 2FA at https://accounts.example.com/pam/verify/%s\nPress enter once verification is complete.\n" % (str(user_status['key']), )))

    while True:
      checked = requests.get('https://accounts.example.com/pam/check/%s' % str(user_status['key'])).json()
      if checked['user'] == user:
        return pamh.PAM_SUCCESS
      else:
        resp=pamh.conversation(
          pamh.Message(pamh.PAM_PROMPT_ECHO_OFF,"Verification not complete. Check your web browser and press enter to try again.")
        )
  
  except:
    resp=pamh.conversation(
      pamh.Message(pamh.PAM_PROMPT_ECHO_OFF,"Couldn't verify your 2FA due to a server error. Press enter to continue.\n")
    )
    return pamh.PAM_SUCCESS

  return pamh.PAM_SUCCESS

def pam_sm_setcred(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_acct_mgmt(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_open_session(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_close_session(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_chauthtok(pamh, flags, argv):
  return pamh.PAM_SUCCESS
