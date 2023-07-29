# hardblock
Installation process :
cd /tmp/
wget https://github.com/eosio/eosio.cdt/releases/download/v1.8.0/eosio.cdt_1.8.0-1-ubuntu-18.04_amd64.deb
sudo apt install ./eosio.cdt_1.8.0-1-ubuntu-18.04_amd64.deb

wget https://github.com/eosio/eos/releases/download/v2.1.0/eosio_2.1.0-1-ubuntu-18.04_amd64.deb
sudo apt install  ./eosio_2.1.0-1-ubuntu-18.04_amd64.deb



# install nodejs 12.x
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install -y nodejs

# additional packages
sudo apt-get install -y git libpcsclite1 libpcsclite-dev pcscd make gcc g++



~/hardblock/eosio/sealregistry
make -f Makefile

Start NodeOS process:
----------------------
keosd &
nodeos -e -p eosio \
--plugin eosio::producer_plugin \
--plugin eosio::producer_api_plugin \
--plugin eosio::chain_api_plugin \
--plugin eosio::http_plugin \
--plugin eosio::history_plugin \
--plugin eosio::history_api_plugin \
--filter-on="*" \
--access-control-allow-origin='*' \
--contracts-console \
--http-validate-host=false \
--verbose-http-errors >> nodeos.log 2>&1 &


ps -ef |grep nodeos

1.cleos wallet list
2.cleos wallet create -n hardblock --to-console
3. Import EOSIO private key
cleos wallet import -n hardblock
Private Key - 5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3
4. Create account using EOSIO Public key
 
cleos create account eosio nfccontract EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV
cleos create account eosio manufacturer EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV
cleos create account eosio distributor EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV
cleos create account eosio consumer EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV

5.1  cleos get table nfccontract 0 issuerids

6.cleos push action nfccontract addiid '["manufacturer", 11]' -p manufacturer@active
7.cleos push action nfccontract addwflow '[11, 55, "Lenovo ships motherboard to Bob", "distributor", "consumer"]' -p manufacturer@active
8. cleos push action nfccontract addkey '[11, 10000, "EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV"]' -p manufacturer@active
9.~/nfc-seal/nodejs/bin/eosio_publish   --url=https://127.0.0.1:8888 --account=manufacturer --key=5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3 contract=nfccontract  --workflow=55 --loop
9. cleos push action nfccontract addseal '[11, 10, c86fc4a5670ea24d7f5610f08d617dfb951a004430ce4dca9c5789cf44c6977b,200,55,"addseal"]' -p manufacturer@active


10.cleos push action nfccontract setstatus '["distributor", 11, 10, "checkpoint1", "Shipping container 23124134533"]' -p distributor@active

11.cleos push action nfccontract setstatus '["consumer", 11, 10, "received", "goods received"]' -p consumer@active

12. cleos push action nfccontract delseal '[11, 10, "done"]' -p consumer@active

13. cleos push action nfccontract delwflow '[11, 55]' -p manufacturer@active 




Data Location:
sudo rm ~/.local/share/eosio/nodeos/data
