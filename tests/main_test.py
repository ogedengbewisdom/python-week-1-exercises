import unittest
from typing import List, Dict, Tuple
from main import *

class TestBitcoinFunctions(unittest.TestCase):
    """Unit tests for Bitcoin-related functions."""
    
    # Constants for testing
    BTC_TO_SATS = 100_000_000
    GENESIS_BLOCK_HEIGHT = 0
    FIRST_HALVING = 210_000

    def test_calculate_total_reward(self):
        self.assertEqual(calculate_total_reward(10), 31.25)

    def test_is_valid_tx_fee(self):
        self.assertTrue(is_valid_tx_fee(0.001))
        self.assertFalse(is_valid_tx_fee(0.02))

    def test_is_large_balance(self):
        self.assertTrue(is_large_balance(100.0))
        self.assertFalse(is_large_balance(10.0))

    def test_tx_priority(self):
        self.assertEqual(tx_priority(250, 0.02), "high")
        self.assertEqual(tx_priority(1000, 0.02), "medium")
        self.assertEqual(tx_priority(10000, 0.02), "low")

    def test_is_mainnet(self):
        self.assertTrue(is_mainnet("MAINNET"))
        self.assertFalse(is_mainnet("testnet"))

    def test_is_in_range(self):
        self.assertTrue(is_in_range(150))
        self.assertFalse(is_in_range(50))

    def test_is_same_wallet(self):
        wallet = {"address": "abc"}
        self.assertTrue(is_same_wallet(wallet, wallet))
        self.assertFalse(is_same_wallet(wallet, {"address": "abc"}))

    def test_normalize_address(self):
        self.assertEqual(normalize_address("  1abcDEF  "), "1abcdef")

    def test_add_utxo(self):
        self.assertEqual(add_utxo([1, 2], 3), [1, 2, 3])

    def test_find_high_fee(self):
        self.assertEqual(find_high_fee([0.001, 0.003, 0.006]), (2, 0.006))
        self.assertIsNone(find_high_fee([0.001, 0.003]))

    def test_get_wallet_details(self):
        self.assertEqual(get_wallet_details(), ("satoshi_wallet", 50.0))

    def test_get_tx_status(self):
        tx_pool = {"abc123": "confirmed"}
        self.assertEqual(get_tx_status(tx_pool, "abc123"), "confirmed")
        self.assertEqual(get_tx_status(tx_pool, "def456"), "not found")

    def test_unpack_wallet_info(self):
        self.assertEqual(unpack_wallet_info(("alice", 75.0)), "Wallet alice has balance: 75.0 BTC")
    
    def test_calculate_sats(self):
        """Test BTC to satoshi conversion."""
        # Test with whole numbers
        self.assertEqual(calculate_sats(1), self.BTC_TO_SATS)
        self.assertEqual(calculate_sats(0.5), 50_000_000)
        
        # Test with small amounts
        self.assertEqual(calculate_sats(0.00000001), 1)
        self.assertEqual(calculate_sats(0.0001), 10_000)
        
        # Test with zero
        self.assertEqual(calculate_sats(0), 0)
        
        # Test with negative (though not realistic)
        self.assertEqual(calculate_sats(-1), -self.BTC_TO_SATS)
    
    def test_generate_address(self):
        """Test Bitcoin address generation."""
        # Default prefix (bech32)
        address = generate_address()
        self.assertTrue(address.startswith("bc1q"))
        self.assertEqual(len(address), 32)
        
        # Test different prefix
        testnet_address = generate_address("tb1q")
        self.assertTrue(testnet_address.startswith("tb1q"))
        
        # Test address contains only valid chars
        import re
        self.assertTrue(re.match(r'^[a-z0-9]+$', address[4:]))
    
    def test_validate_block_height(self):
        """Test block height validation."""
        # Valid heights
        self.assertEqual(validate_block_height(0), (True, "Valid block height"))
        self.assertEqual(validate_block_height(700_000), (True, "Valid block height"))
        
        # Invalid heights
        self.assertEqual(validate_block_height(-1), (False, "Block height cannot be negative"))
        self.assertEqual(validate_block_height(1_000_000), (False, "Block height seems unrealistic"))
        
        # Wrong type
        self.assertEqual(validate_block_height(123.5), (False, "Block height must be an integer"))
        self.assertEqual(validate_block_height("100"), (False, "Block height must be an integer"))
    
    def test_halving_schedule(self):
        """Test block reward halving calculations."""
        # Test genesis block
        self.assertEqual(halving_schedule([self.GENESIS_BLOCK_HEIGHT]), {0: 50 * self.BTC_TO_SATS})
        
        # Test first halving
        self.assertEqual(
            halving_schedule([self.FIRST_HALVING - 1, self.FIRST_HALVING, self.FIRST_HALVING + 1]),
            {
                209_999: 50 * self.BTC_TO_SATS,
                210_000: 25 * self.BTC_TO_SATS,
                210_001: 25 * self.BTC_TO_SATS
            }
        )
        
        # Test multiple halvings
        self.assertEqual(
            halving_schedule([420_000, 630_000]),
            {
                420_000: 12.5 * self.BTC_TO_SATS,
                630_000: 6.25 * self.BTC_TO_SATS
            }
        )
    
    def test_find_utxo_with_min_value(self):
        """Test UTXO selection logic."""
        utxos = [
            {"txid": "abc", "value": 10_000},
            {"txid": "def", "value": 25_000},
            {"txid": "ghi", "value": 5_000},
            {"txid": "jkl", "value": 50_000}
        ]
        
        # Find exact match
        self.assertEqual(
            find_utxo_with_min_value(utxos, 25_000),
            {"txid": "def", "value": 25_000}
        )
        
        # Find smallest above target
        self.assertEqual(
            find_utxo_with_min_value(utxos, 15_000),
            {"txid": "def", "value": 25_000}
        )
        
        # No UTXO large enough
        self.assertEqual(find_utxo_with_min_value(utxos, 100_000), {})
        
        # Empty UTXO list
        self.assertEqual(find_utxo_with_min_value([], 10_000), {})

class TestBitcoinDataStructures(unittest.TestCase):
    """Tests for Bitcoin-related data structure operations."""
    
    def test_string_methods(self):
        """Test string operations with Bitcoin data."""
        txid = "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890"
        
        # Test string length (64 chars for txid)
        self.assertEqual(len(txid), 64)
        
        # Test hexadecimal characters only
        self.assertTrue(txid.isalnum())
        self.assertTrue(all(c in "0123456789abcdef" for c in txid))
        
        # Test case conversion
        upper_txid = txid.upper()
        self.assertEqual(upper_txid, "ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890")
    
    def test_list_methods(self):
        """Test list operations with Bitcoin data."""
        block_heights = [600_000, 600_001, 600_002]
        
        # Test list modification
        block_heights.append(600_003)
        self.assertEqual(block_heights[-1], 600_003)
        
        # Test list slicing
        last_two = block_heights[-2:]
        self.assertEqual(last_two, [600_002, 600_003])
        
        # Test list sorting
        unsorted_heights = [600_002, 600_000, 600_001]
        self.assertEqual(sorted(unsorted_heights), [600_000, 600_001, 600_002])
    
    def test_dict_methods(self):
        """Test dictionary operations with Bitcoin data."""
        utxo = {
            "txid": "abcd1234",
            "vout": 0,
            "value": 12_345,
            "address": "bc1qxyz"
        }
        
        # Test dict access
        self.assertEqual(utxo["value"], 12_345)
        
        # Test dict methods
        keys = utxo.keys()
        self.assertIn("address", keys)
        
        # Test dict update
        utxo.update({"confirmed": True})
        self.assertTrue(utxo["confirmed"])
    
    def test_unpacking(self):
        """Test unpacking with Bitcoin data."""
        # Multiple assignment
        tx_details = ("abcd1234", 1, 50_000)
        txid, vout, value = tx_details
        self.assertEqual(txid, "abcd1234")
        self.assertEqual(value, 50_000)
        
        # Dictionary unpacking
        def create_utxo(txid: str, vout: int, **kwargs):
            base = {"txid": txid, "vout": vout}
            base.update(kwargs)
            return base
            
        utxo = create_utxo("tx123", 0, value=10_000, address="bc1qtest")
        self.assertEqual(utxo["address"], "bc1qtest")

class TestBitcoinControlFlow(unittest.TestCase):
    """Tests for control flow with Bitcoin concepts."""
    
    def test_loops(self):
        """Test loops with Bitcoin data."""
        # Test for loop with range
        block_rewards = []
        for height in range(0, 210_000, 52_500):  # Every quarter of halving epoch
            reward = 50 // (2 ** (height // 210_000))
            block_rewards.append(reward)
        
        self.assertEqual(block_rewards, [50, 50, 50, 50])
        
        # Test while loop
        target_diff = 1_000_000
        current_hash = 0
        attempts = 0
        while current_hash < target_diff:
            current_hash += 200_000
            attempts += 1
            if attempts > 10:
                break
                
        self.assertEqual(attempts, 5)
        
        # Test list comprehension
        tx_values = [10_000, 25_000, 5_000, 50_000]
        large_txes = [v for v in tx_values if v > 20_000]
        self.assertEqual(large_txes, [25_000, 50_000])
        
        # Test enumerate
        txids = ["tx1", "tx2", "tx3"]
        for i, txid in enumerate(txids, start=1):
            self.assertEqual(txid, f"tx{i}")
    
    def test_comparisons(self):
        """Test comparison operations with Bitcoin data."""
        # Numeric comparisons
        block_time_1 = 12.5
        block_time_2 = 10.0
        self.assertTrue(block_time_1 > block_time_2)
        self.assertFalse(block_time_1 == block_time_2)
        
        # String comparisons (lexicographical)
        address1 = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"  # Genesis address
        address2 = "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy"
        self.assertTrue(address1 < address2)  # '1' < '3' in ASCII
        
        # Comparison chaining
        block_height = 700_000
        self.assertTrue(600_000 < block_height < 800_000)
        
        # Identity comparison
        a = b = "bitcoin"
        c = "".join(["bit", "coin"])
        self.assertTrue(a is b)
        self.assertFalse(a is c)  # Same value but different objects

if __name__ == "__main__":
    unittest.main()
