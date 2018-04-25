# pam-http-2fa-demo
Very basic demo of how you could add centralised 2FA to PAM services. Not to be used as is, but could serve as inspiration for a more sophisticated design.

## Deployment

To use with `ssh` for instance, edit `/etc/pam.d/sshd` and change the top few lines to look like this:

    # Standard Un*x authentication.
    # @include common-auth
    auth  [success=1 default=ignore] pam_python.so pam_2fa.py
    auth  requisite pam_deny.so
    auth  required pam_permit.so
