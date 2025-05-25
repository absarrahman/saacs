#!/usr/bin/env python3
import os
import sys

def pem_to_escaped_string(path):
  with open(path, 'r') as f:
    text = f.read()
    return text.replace('\n', '\\n')

class User:
  def __init__(self, name, private_key, certificate):
    self.name = name
    self.private_key = private_key
    self.certificate = certificate

def main():
  users = [
      User(
        name='User5',
        private_key='/home/padlock/Desktop/Absar/saacs-clean/infra/network/organizations/peerOrganizations/org1.example.com/users/User5@org1.example.com/msp/keystore/priv_sk',
        certificate='/home/padlock/Desktop/Absar/saacs-clean/infra/network/organizations/peerOrganizations/org1.example.com/users/User5@org1.example.com/msp/signcerts/cert.pem'),
      User(
        name='User4',
        private_key='/home/padlock/Desktop/Absar/saacs-clean/infra/network/organizations/peerOrganizations/org1.example.com/users/User4@org1.example.com/msp/keystore/priv_sk',
        certificate='/home/padlock/Desktop/Absar/saacs-clean/infra/network/organizations/peerOrganizations/org1.example.com/users/User4@org1.example.com/msp/signcerts/cert.pem'),
      User(
        name='User3',
        private_key='/home/padlock/Desktop/Absar/saacs-clean/infra/network/organizations/peerOrganizations/org1.example.com/users/User3@org1.example.com/msp/keystore/priv_sk',
        certificate='/home/padlock/Desktop/Absar/saacs-clean/infra/network/organizations/peerOrganizations/org1.example.com/users/User3@org1.example.com/msp/signcerts/cert.pem'),
      User(
        name='User2',
        private_key='/home/padlock/Desktop/Absar/saacs-clean/infra/network/organizations/peerOrganizations/org1.example.com/users/User2@org1.example.com/msp/keystore/priv_sk',
        certificate='/home/padlock/Desktop/Absar/saacs-clean/infra/network/organizations/peerOrganizations/org1.example.com/users/User2@org1.example.com/msp/signcerts/cert.pem'),
      User(
        name='Admin',
        private_key='/home/padlock/Desktop/Absar/saacs-clean/infra/network/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp/keystore/priv_sk',
        certificate='/home/padlock/Desktop/Absar/saacs-clean/infra/network/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp/signcerts/cert.pem'),
      User(
        name='User1',
        private_key='/home/padlock/Desktop/Absar/saacs-clean/infra/network/organizations/peerOrganizations/org1.example.com/users/User1@org1.example.com/msp/keystore/priv_sk',
        certificate='/home/padlock/Desktop/Absar/saacs-clean/infra/network/organizations/peerOrganizations/org1.example.com/users/User1@org1.example.com/msp/signcerts/cert.pem')
      ]

  file_path = 'users_info.txt'
  # check whether file exists. If exists, remove it
  if os.path.exists(file_path):
    os.remove(file_path)
  with open(file_path, 'w', encoding='utf-8') as target:
    for user in users:
      priv_key = pem_to_escaped_string(user.private_key)
      cert = pem_to_escaped_string(user.certificate)
      target.write(f"Name: {user.name}\nPrivate key:\n{priv_key}\nCertificate:\n{cert}\n\n=============\n\n")

if __name__ == "__main__":
  main()
