#!/bin/bash
#
    docker stop peer0org1_saacs-caliper_ccaas
    docker run --rm -d --name peer0org1_saacs-caliper_ccaas                      --network fabric_test                     -e CHAINCODE_SERVER_ADDRESS=0.0.0.0:9999                     -e CHAINCODE_ID=saacs-caliper_1.0.1:1207969f913c6c4c5797e783ad3fe56ebdccde9c705e692efc14e233aea91b29 -e CORE_CHAINCODE_ID_NAME=saacs-caliper_1.0.1:1207969f913c6c4c5797e783ad3fe56ebdccde9c705e692efc14e233aea91b29                     -e AUTH_MODE=saacs-caliper                                          saacs_ccaas:latest

    docker stop peer0org2_saacs-caliper_ccaas
    docker run --rm -d --name peer0org2_saacs-caliper_ccaas                     --network fabric_test                     -e CHAINCODE_SERVER_ADDRESS=0.0.0.0:9999                     -e CHAINCODE_ID=saacs-caliper_1.0.1:1207969f913c6c4c5797e783ad3fe56ebdccde9c705e692efc14e233aea91b29 -e CORE_CHAINCODE_ID_NAME=saacs-caliper_1.0.1:1207969f913c6c4c5797e783ad3fe56ebdccde9c705e692efc14e233aea91b29                     -e AUTH_MODE=saacs-caliper                                          saacs_ccaas:latest
