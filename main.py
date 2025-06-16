import random
import string
from typing import Union, Tuple, List, Dict

# Name Assignment (variables and constants)
MINING_REWARD = None # TODO: Assign the current bitcoin mining reward
current_block_height = None # TODO: Assign the current block height as an integer
BTC_TO_SATS = None # TODO: Assign the number of satoshis in one Bitcoin

# Functions
def calculate_total_reward(blocks_mined) -> int:
    """Calculate the total Bitcoin reward for a given number of mined blocks.
    
    Args:
        blocks_mined: Number of mined blocks
        
    Returns:
        Total BTC reward
    """
    # TODO: Multiply blocks_mined by MINING_REWARD and return result


def is_valid_tx_fee(fee):
    """Return True if the transaction fee is within an acceptable range.
    
    Args:
        fee: Transaction fee in BTC
        
    Returns:
        Boolean indicating whether the fee is valid
    """
    # TODO: Check if fee is between 0.00001 and 0.01 BTC


def is_large_balance(balance):
    """Determine if a wallet balance is considered large.
    
    Args:
        balance: Wallet balance in BTC
        
    Returns:
        True if balance > 50.0 BTC, False otherwise
    """
    # TODO: Compare balance to 50.0 and return result


def tx_priority(size_bytes, fee_btc):
    """Return the priority of a transaction based on fee rate.
    
    Args:
        size_bytes: Size of transaction in bytes
        fee_btc: Fee of the transaction in BTC
        
    Returns:
        'high' - 0.00005, 'medium' - 0.00001, or 'low' based on fee rate
    """
    # TODO: Calculate fee rate and use if-elif-else to determine priority


def is_mainnet(network):
    """Check if the network is for Bitcoin mainnet.
    
    Args:
        network: String like 'mainnet', 'testnet', 'signet' or 'regtest'
        
    Returns:
        True if mainnet, False otherwise
    """
    # TODO: Convert network to lowercase and compare with "mainnet"


def is_in_range(value):
    """Check if a value is within the range 100 to 200 (inclusive).
    
    Args:
        value: Numeric value
        
    Returns:
        True if in range, else False
    """
    # TODO: Use comparison chaining to check if 100 <= value <= 200


def is_same_wallet(wallet1, wallet2):
    """Check if two wallet objects are the same in memory.
    
    Args:
        wallet1: First wallet object
        wallet2: Second wallet object
        
    Returns:
        True if both point to the same object, else False
    """
    # TODO: Use the 'is' keyword to compare object identity


def normalize_address(address):
    """Normalize a Bitcoin address by stripping whitespace and converting to lowercase.
    
    Args:
        address: Raw address string
        
    Returns:
        Normalized address string
    """
    # TODO: Strip leading/trailing spaces and convert to lowercase


def add_utxo(utxos, new_utxo):
    """Add a new UTXO to the list of UTXOs.
    
    Args:
        utxos: List of current UTXOs
        new_utxo: UTXO to add
        
    Returns:
        Updated list of UTXOs
    """
    # TODO: Append new_utxo to the utxos list and return it


def find_high_fee(fee_list):
    """Find the first transaction with a fee greater than 0.005 BTC.
    
    Args:
        fee_list: List of transaction fees
        
    Returns:
        Tuple of (index, fee) or None if not found
    """
    # TODO: Use a for loop with enumerate to find fee > 0.005 and return index and value


def get_wallet_details():
    """Return basic wallet details as a tuple.
    
    Returns:
        Tuple containing (wallet_name, balance)
    """
    # TODO: Return a tuple with wallet name and balance


def get_tx_status(tx_pool, txid):
    """Get the status of a transaction from the mempool.
    
    Args:
        tx_pool: Dictionary of txid -> status
        txid: Transaction ID to check
        
    Returns:
        Status string or 'not found'
    """
    # TODO: Use dict.get() to return tx status or 'not found' if missing


def unpack_wallet_info(wallet_info):
    """Unpack wallet information from a tuple and return a formatted string.
    
    Args:
        wallet_info: Tuple of (wallet_name, balance)
        
    Returns:
        Formatted string of wallet status
    """
    # TODO: Unpack wallet_info tuple into name and balance, then format the return string


def calculate_sats(btc: float) -> int:
    """Convert BTC to satoshis (1 BTC = 100,000,000 sats).
    
    Args:
        btc: Amount in Bitcoin
        
    Returns:
        Equivalent amount in satoshis
    """
    # TODO: Multiply btc by BTC_TO_SATS and return the integer value


def generate_address(prefix: str = "bc1q") -> str:
    """Generate a mock Bitcoin address with given prefix.
    
    Args:
        prefix: Address prefix (default is bech32)
        
    Returns:
        Mock address string
    """
    # TODO: Generate a suffix of random alphanumeric characters (length = 32 - len(prefix))
    # TODO: Concatenate the prefix and suffix to form the mock address


def validate_block_height(height: Union[int, float, str]) -> Tuple[bool, str]:
    """Validate a Bitcoin block height.
    
    Args:
        height: Block height to validate
        
    Returns:
        Tuple of (is_valid, message)
    """
    # TODO: Ensure height is an integer
    # TODO: Check that height is not negative
    # TODO: Check that height is within a realistic range (e.g., <= 800,000)


def halving_schedule(blocks: List[int]) -> Dict[int, int]:
    """Calculate block reward for given block heights based on halving schedule.
    
    Args:
        blocks: List of block heights
        
    Returns:
        Dictionary mapping block heights to their block reward in satoshis
    """
    # TODO: Initialize the base reward for the genesis block in sats
    # TODO: Initialize the halving interval approximately every four years in blocks
    # TODO: Iterate through each block height, compute halvings, and calculate reward
    # TODO: Store results in a dictionary


def find_utxo_with_min_value(utxos: List[Dict[str, int]], target: int) -> Dict[str, int]:
    """Find the UTXO with minimum value that meets or exceeds target.
    
    Args:
        utxos: List of UTXOs (each with 'value' key in sats)
        target: Minimum target value in sats
        
    Returns:
        UTXO with smallest value >= target, or empty dict if none found
    """
    # TODO: Filter UTXOs to those with value >= target
    # TODO: Return the one with the smallest value, or {} if none found


def create_utxo(txid: str, vout: int, **kwargs) -> Dict[str, Union[str, int]]:
    """Create a UTXO dictionary with optional additional fields."""
    # TODO: Create a base dictionary with txid and vout
    # TODO: Merge any extra keyword arguments into the base

