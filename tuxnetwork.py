import hashlib
import time
import random
import threading

class Wallet:
    def __init__(self, address, tux_balance):
        self.address = address
        self.tux_balance = tux_balance

    def has_enough_stake(self, min_stake=100):
        return self.tux_balance >= min_stake

    def send_tux(self, amount, recipient):
        if self.tux_balance >= amount:
            self.tux_balance -= amount
            recipient.tux_balance += amount
            return True
        return False

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()

    def to_string(self):
        return f"{self.sender.address} envía {self.amount} TUX a {self.recipient.address}"

class Block:
    def __init__(self, previous_hash, transactions, miner_wallet, staker_wallet):
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = time.time()
        self.nonce = 0
        self.miner_wallet = miner_wallet
        self.staker_wallet = staker_wallet
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = (f"{self.previous_hash}{[tx.to_string() for tx in self.transactions]}"
                 f"{self.timestamp}{self.nonce}{self.miner_wallet.address}"
                 f"{self.staker_wallet.address}")
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        if not self.miner_wallet:
            print("Error: Se necesita un minero.")
            return False
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Bloque minado por {self.miner_wallet.address}! Hash: {self.hash}")
        return True

    def validate_stake(self, min_stake=100):
        if not self.staker_wallet or not self.staker_wallet.has_enough_stake(min_stake):
            print(f"Error: Stake insuficiente (< {min_stake} TUX).")
            return False
        print(f"Bloque validado por {self.staker_wallet.address}.")
        return True

class Node:
    def __init__(self, node_id, network):
        self.node_id = node_id
        self.network = network
        self.chain = network.chain  # Comparten la misma cadena por ahora (simulación)

    def run(self):
        print(f"Nodo {self.node_id} iniciado.")
        # Simulación simple: cada nodo intenta añadir un bloque
        miner = Wallet(f"miner_{self.node_id}", 0)
        staker = Wallet(f"staker_{self.node_id}", 150)
        transactions = [
            Transaction(Wallet(f"user_{self.node_id}a", 200), Wallet(f"user_{self.node_id}b", 50), 10),
            Transaction(Wallet(f"user_{self.node_id}b", 60), Wallet(f"user_{self.node_id}c", 30), 5),
            Transaction(Wallet(f"user_{self.node_id}c", 35), Wallet(f"user_{self.node_id}a", 100), 15)
        ]
        for tx in transactions:
            tx.sender.send_tux(tx.amount, tx.recipient)
        self.network.add_block(transactions, miner, staker)

class TUXNetwork:
    def __init__(self, difficulty=2):
        self.chain = []
        self.difficulty = difficulty  # Ajustable, te explico abajo
        self.min_stake = 100
        self.total_supply = 100_000_000

    def create_genesis_block(self):
        dev_team = Wallet("dev_team", 800_000)  # Preminado 0.8%
        miner = Wallet("genesis_miner", 0)
        staker = Wallet("genesis_staker", 100)
        genesis_tx = Transaction(dev_team, dev_team, 800_000)
        genesis = Block("0", [genesis_tx], miner, staker)
        genesis.mine_block(self.difficulty)
        genesis.validate_stake(self.min_stake)
        self.chain.append(genesis)
        print(f"Bloque génesis creado. Preminado: 800,000 TUX a {dev_team.address}")
        return dev_team

    def add_block(self, transactions, miner_wallet, staker_wallet):
        previous_block = self.chain[-1]
        new_block = Block(previous_block.hash, transactions, miner_wallet, staker_wallet)
        if new_block.mine_block(self.difficulty) and new_block.validate_stake(self.min_stake):
            self.chain.append(new_block)
            miner_wallet.tux_balance += 7
            staker_wallet.tux_balance += 2
            dev_team = Wallet("dev_team", 0)  # Simulación
            dev_team.tux_balance += 0.5
            print(f"Bloque añadido. Total bloques: {len(self.chain)}")
            return True
        return False

if __name__ == "__main__":
    # Crear la red
    network = TUXNetwork(difficulty=3)  # Dificultad inicial
    dev_team_wallet = network.create_genesis_block()
    print(f"Saldo del equipo de desarrollo: {dev_team_wallet.tux_balance} TUX")

    # Simular 3 nodos
    nodes = [Node(i, network) for i in range(3)]
    threads = []
    for node in nodes:
        t = threading.Thread(target=node.run)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Total bloques en la cadena: {len(network.chain)}")