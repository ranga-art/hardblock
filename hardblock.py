import os
global contract_name, manufacturer, distributor, consumer

contract_name="nfc"
manufacturer="manufacturer"
distributor="distributor"
consumer="consumer"
# Menu driven program for the supply blockchain
def create_wallet():
    wallet_name = str(raw_input("Enter wallet name ---> "))
    print("Command Executed ---> cleos wallet create -n "+wallet_name+" --to-console")
    os.system("cleos wallet create -n "+ wallet_name + " --to-console")

def list_wallet():
    print("Command Executed ---> cleos wallet list")
    os.system("cleos wallet list")

def import_key():
    wallet_name = str(raw_input("Enter wallet name ---> "))
    print ("eg.Private key ---> 5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3 ")
    print("Command Executed ---> cleos wallet import -n" + wallet_name)
    os.system("cleos wallet import -n" + wallet_name)

def create_account():
    print("Command Executed --->  cleos create account eosio " + contract_name + " EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV")
    os.system(" cleos create account eosio " + contract_name + " EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV")
    os.system(" cleos create account eosio " + manufacturer + " EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV")
    os.system(" cleos create account eosio " + distributor + " EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV")
    os.system(" cleos create account eosio " + consumer + " EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV")

def unlock_wallet():
    wallet_name = str(raw_input("Enter wallet name ---> "))
    password = str(raw_input("Enter password ---> "))
    print("Command Executed ---> cleos wallet unlock -n "+ wallet_name +" --password PW5K3xxxxxx")
    os.system("cleos wallet unlock -n "+ wallet_name +" --password "+ password)

def list_account():
    os.system("cleos get accounts EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV")

def create_contract():
   # contract_name=str(raw_input("Enter contract account name --->  "))
    print(" Command Executed ---> cleos set contract " +contract_name+ " ./ sealregistry.wasm sealregistry.abi ")
    #os.system(" cd /home/ubuntu/hardblock/eosio/sealregistry ")
    os.system(" cleos set contract " +contract_name+ " /home/ubuntu/hardblock/eosio/sealregistry sealregistry.wasm sealregistry.abi")

def create_id():
      #  contract_name=str(raw_input("Enter account name --->  "))
        issuerid=str(raw_input("Enter issuer_id --->  "))
       # contract_name=str(raw_input("Enter contract name --->  "))
        inpstr='['+'"'+manufacturer+'"'+','+issuerid+']'
        #inpstr=espstr.replace('\\"','"')
        print(inpstr)
        print("Command Executed ---> cleos push action "+ contract_name+" addiid "+inpstr+" -p "+manufacturer+"@active")
        os.system("cleos push action "+contract_name+ " addiid "+inpstr+" -p "+manufacturer+"@active")

def create_workflow():
       issuer_id=str(raw_input("Enter issuer_id ---> "))
       worflow=str(raw_input("Enter worflow no. ---> "))
       print("Command Executed ---> cleos push action "+contract_name+" addwflow "+ "'"+ '['+issuer_id+','+ worflow+','+'"'"Lenovo ships motherboard to Bob"'"' +','+'"'+distributor+'"'+','+ '"'+consumer+'"'+']'+"'"+" -p "+ manufacturer+"@active")
       os.system("cleos push action "+contract_name+" addwflow "+ "'"+ '['+issuer_id+','+ worflow+','+'"'"Lenovo ships motherboard to Bob"'"' +','+'"'+distributor+'"'+','+ '"'+consumer+'"'+']'+"'"+" -p "+ manufacturer+"@active")
      # os.system("cleos push action "+contract_name+" addwflow "+  '['+issuer_id+','+ worflow+','+'"'"Lenovo ships motherboard to Bob"'"' +','+'"'+distributor+'"'+','+ '"'+consumer+'"'+']'+" -p "+ manufacturer+"@active")
      # string=" , "+'"'+distributor+'"'+" , "+'"'+consumer+'"'+"]"+"'"
      # os.system("cleos push action nfccontract addwflow "+ '['+issuer_id+','+ worflow+','+'"'"Lenovo ships motherboard to Bob"'"'+ string + " -p "+ manufacturer+"@active")

def add_key():
        issuer_id=str(raw_input("Enter issuer_id ---> "))
        nfcno = str(raw_input("Enter number of NFC tags to be signed ---> "))
        print("Command Executed ---> cleos push action "+ contract_name+" addkey "+"'"+ '['+issuer_id+','+nfcno+','+ " EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV"+']'+"'"+" -p "+ manufacturer +"@active")
        os.system("cleos push action "+ contract_name+" addkey "+"'"+ '['+issuer_id+','+nfcno+','+ " EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV"+']'+"'"+" -p "+ manufacturer +"@active")

def nfc_seal():
      global issuer,seq,workflow
      issuer=str(raw_input("Enter issuer_id ---> "))
      seq=str(raw_input("Enter sequence number ---> "))
      workflow=str(raw_input("Enter workflow number ---> "))
      print("Writing NFC .....")

def add_seal():
        print("Reading from NFC.....")
        os.system("cleos push action "+contract_name+" addseal "+"'"+'['+issuer+','+seq+','+ "c86fc4a5670ea24d7f5610f08d617dfb951a004430ce4dca9c5789cf44c6977b"+','+"200"+','+workflow+','+'"'+"addseal"+'"'+']'+"'"+" -p manufacturer@active")

def distributor_status_update():
     issuer_id=str(raw_input("Enter issuer_id ---> "))
     seq=str(raw_input("Enter sequence number ---> "))
     os.system("cleos get table "+contract_name+" 0 seals")
     print("Command Executed ---> cleos push action "+ contract_name+" setstatus "+"'"+ '['+'"'+distributor+'"'+' ,'+issuer_id+' ,'+seq+','+'"'+ "checkpoint1"+'"'+','+'"'+ "Shipping container 23124134533"+'"'+']'+"'"+" -p "+distributor+"@active")
     os.system("cleos push action "+ contract_name+" setstatus "+"'"+ '['+'"'+distributor+'"'+' ,'+issuer_id+' ,'+seq+','+'"'+ "checkpoint1"+'"'+','+'"'+ "Shipping container 23124134533"+'"'+']'+"'"+" -p "+distributor+"@active")

def consumer_status_update():
    issuer_id=str(raw_input("Enter issuer_id ---> "))
    seq=str(raw_input("Enter a sequence number ---> "))
    os.system("cleos get table "+contract_name+" 0 seals")
    print("Command Executed ---> cleos push action "+ contract_name+" setstatus "+"'"+ '['+'"'+consumer+'"'+' ,'+issuer_id+' ,'+seq+','+'"'+ "received"+'"'+','+'"'+ "goods received"+'"'+']'+"'"+" -p "+consumer+"@active")
    os.system("cleos push action "+ contract_name+" setstatus "+"'"+ '['+'"'+consumer+'"'+' ,'+issuer_id+' ,'+seq+','+'"'+ "received"+'"'+','+'"'+ "goods received"+'"'+']'+"'"+" -p "+consumer+"@active")

def del_seal():
    global choice1
    choice1=str(raw_input("Do you want to delete the seal yes or no ---> "))
    if choice1=="yes":
         issuer_id=str(raw_input("Enter issuer_id ---> "))
         seq=str(raw_input("Enter sequence number ---> "))
         print("Command Executed ---> cleos push action "+contract_name+" delseal "+"'"+ '['+issuer_id+","+seq+","+'"'+"done"+'"'+']'+"'"+" -p "+consumer+"@active")
         os.system("cleos push action "+contract_name+" delseal "+"'"+ '['+issuer_id+","+seq+","+'"'+"done"+'"'+']'+"'"+" -p "+consumer+"@active")

def del_workflow():
    global choice1
    choice1=str(raw_input("Do you want to delete the workflow yes or no ---> "))
    if choice1=="yes":
        issuer_id=str(raw_input("Enter issuer_id ---> "))
        workflow=str(raw_input("Enter Workflow no. ---> "))
        print("command executed ---> cleos push action "+ contract_name+" delwflow "+"'"+'['+issuer_id+','+workflow+']'+"'"+" -p "+manufacturer+"@active")
        os.system("cleos push action "+ contract_name+" delwflow "+"'"+'['+issuer_id+','+workflow+']'+"'"+" -p "+manufacturer+"@active")

def del_accounts():
    os.system('sudo rm -rf ~/.local/share/eosio/nodeos/data')
    os.system('pkill nodeos')
    os.system('nodeos -e -p eosio --plugin eosio::producer_plugin --plugin eosio::producer_api_plugin --plugin eosio::chain_api_plugin --plugin eosio::http_plugin --plugin eosio::history_plugin --plugin eosio::history_api_plugin --filter-on="*" --access-control-allow-origin="*" --contracts-console --http-validate-host=false --verbose-http-errors >> nodeos.log 2>&1 &')
    print(" Accounts deleted Succesfully")
while(1):
        print('\33[0m'+'\nThe following options are available to the user: ')
        print('1.  Create wallet  ')
        print('2.  List wallet ')
        print('3.  Import private key to wallet ')
        print('4.  Create account ')
        print('5.  List existing accounts ')
        print('6.  Create contract in blockchain')
        print('7.  Create an ID for the issuer')
        print('8.  Create Workflow in blockchain')
        print('9.  Add public key for signing the seal')
        print('10. Write Label in NFC Tag')
        print('11. Publish the Seal details to blockchain')
        print('12. Status update by the distributor')
        print('13. Status update by the consumer')
        print('14. Delete seal in blockchain')
        print('15. Delete workflow in blockchain')
        print('16. Unlock Wallet')
        print('17. Delete Accounts')
        print('18. Exit')
        print('\33[92m')
        choice = int(input('Enter your choice: '))

        if(choice == 1):
                create_wallet()
        elif(choice == 2):
                list_wallet()
        elif(choice == 3):
                import_key()
        elif(choice == 4):
                create_account()
        elif(choice == 5):
                list_account()
        elif(choice == 6):
                create_contract()
        elif(choice == 7):
                create_id()
        elif(choice == 8):
                create_workflow()
        elif(choice == 9):
                add_key()
        elif(choice == 10):
                nfc_seal()
        elif(choice == 11):
                add_seal()
        elif(choice == 12):
                distributor_status_update()
        elif(choice == 13):
                consumer_status_update()
        elif(choice == 14):
                del_seal()
        elif(choice == 15):
                del_workflow()
        elif(choice == 16):
                unlock_wallet()
        elif(choice == 17):
                del_accounts()
        elif(choice == 18):
                break
        else:
                print('\33[92m'+('This is an invalid option.'))
