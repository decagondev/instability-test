import unittestimport jsonfrom app_unstable import app
class TestTriageConsistency(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.ambiguous_payload = {
            "id": 402,
            "title": "Cannot access premium paid features",
            "description": "My visa card was successfully charged £15 morning, but when I click the pro checkout dashboard it still says 'Access Denied: 403 Forbidden' error."
        }

    def test_nondeterminism_leak(self):
        """Runs the exact same ticket 5 times to verify classification stability."""
        results = set()
        
        for i in range(5):
            response = self.client.post(
                '/tickets/triage', 
                data=json.dumps(self.ambiguous_payload), 
                content_type='application/json'
            )
            data = json.loads(response.data.decode('utf-8'))
            results.add(data.get('category'))
            
        print(f"\n[DEBUG] Categories observed over 5 identical trials: {list(results)}")
        
        self.assertEqual(len(results), 1, f"Nondeterminism detected! Ticket classified into multiple buckets: {results}")
if __name__ == '__main__':
    unittest.main()
