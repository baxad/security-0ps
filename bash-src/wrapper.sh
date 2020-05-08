#!/bin/bash -
#
#
# Description:
# Example of executing an encrypted "wrapped" script
#
# Usage:
# wrapper.sh
# Enter the password when prompted
#
# change encrypted with your value or call input file containing the 
# cypher text
encrypted='U2FsdGVkX18WvDOyPFcvyvAozJHS3tjrZIPlZM9xRhz0tuwzDrKhKBBuugLxzp7T
MoJoqx02tX7KLhATS0Vqgze1C+kzFxtKyDAh9Nm2N0HXfSNuo9YfYD+15DoXEGPd'
read -s word
innerScript=$(echo "$encrypted" | openssl aes-256-cbc -base64 -d -pass 
pass:"$word")
eval "$innerScript"
