import json
import requests

z = 0
i = 0
firstpart = "https://blockchain.info/rawaddr/"
initialinput = input("please type the 'seed' address: ")
initialreq = firstpart + initialinput

firstjson = (requests.get(initialreq)).json()
graphvizlines = []

addresslist = []
usedaddresslist = []
transactionlist = []

addresslist.append(initialinput)
usedaddresslist.append(initialinput)

while i < 3:
    if z is 1:
        print(i)
        print(addresslist[i])
        initialreq = firstpart + addresslist[i]
        firstjson = (requests.get(initialreq)).json()
    
    for transaction in firstjson["txs"]:
        payerlist = []
        recipientlist = []
        txhsh = str(transaction["hash"])
        transactionlist.append('"' + txhsh + '" [shape=rect];')
        
        for item in transaction["inputs"]:
            payerlist.append(item["prev_out"]["addr"])

        for target in transaction["out"]:
            holderlist = []
            addy = target["addr"]
            valint = str((int(target["value"])/100000000))
            holderlist.append(addy)
            holderlist.append(valint)
            recipientlist.append(holderlist)

        for payer in payerlist:
            newline = '"' + payer + '"->"' + txhsh + '";'
            graphvizlines.append(newline)
            if payer not in addresslist:
                addresslist.append(payer)

        for recipient in recipientlist:
            newline2 = '"' + txhsh + '"->"' + recipient[0] + '" [label="' + recipient[1] + '"];'
            graphvizlines.append(newline2)
            if recipient not in addresslist:
                addresslist.append(recipient[0])

            
    i = i + 1    
    z = 1
        
for tt in transactionlist:
    print(tt)
for t in graphvizlines:
    print(t)
