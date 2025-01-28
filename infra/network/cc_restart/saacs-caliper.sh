#!/bin/bash
#
    docker stop peer0org1_saacs-caliper_ccaas
    docker run --rm -d --name peer0org1_saacs-caliper_ccaas                      --network fabric_test                     -e CHAINCODE_SERVER_ADDRESS=0.0.0.0:9999                     -e CHAINCODE_ID=saacs-caliper_1.0.1:d661843082c1b6d78b77a2ad1aeab6d7f4a4c318eb3d52ab823f14a2f0fcf697 -e CORE_CHAINCODE_ID_NAME=saacs-caliper_1.0.1:d661843082c1b6d78b77a2ad1aeab6d7f4a4c318eb3d52ab823f14a2f0fcf697                     -e AUTH_MODE=saacs-caliper                                          saacs_ccaas:latest

    docker stop peer0org2_saacs-caliper_ccaas
    docker run --rm -d --name peer0org2_saacs-caliper_ccaas                     --network fabric_test                     -e CHAINCODE_SERVER_ADDRESS=0.0.0.0:9999                     -e CHAINCODE_ID=saacs-caliper_1.0.1:d661843082c1b6d78b77a2ad1aeab6d7f4a4c318eb3d52ab823f14a2f0fcf697 -e CORE_CHAINCODE_ID_NAME=saacs-caliper_1.0.1:d661843082c1b6d78b77a2ad1aeab6d7f4a4c318eb3d52ab823f14a2f0fcf697                     -e AUTH_MODE=saacs-caliper                                          saacs_ccaas:latest
