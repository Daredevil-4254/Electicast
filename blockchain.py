import hashlib

def hashGenerator(data):
    result=hashlib.sha256(data,encode())
    return result.hexdigit()

class Block:
    def _init_(self,data,hash,prev_hash):
        self.data=data
        self.hash=hash
        self.prev_hash=prev_hash


class Blockchain:
    def _init_(self):
        hashlast=hashGenerator('gen_last')
        hashStart=hashGenerator('gen_hash')

        genesis=Block('gen-dada' ,hashStart , hashLast)
        self.chain=(genesis)

    def add_block(self,data):
        prev_hash=self.chain[-1].hash
        hash=hashGenerator(data+prev_hash)
        block=Block(data,hash,prev_hash)
        self.chain.append(block)


bc=Blockhain()
bc.add_block('1')
bc.add_block('2')
bc.add_block('3')
bc.add_block('4')
bc.add_block('5')
bc.add_block('6')
bc.add_block('7')