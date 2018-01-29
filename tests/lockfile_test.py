from kutils.lockfile import pidlock, release_lock, LockHeld
import os
import unittest




class LockFileTest(unittest.TestCase):
    def test_pidlock(self):
        try:
            lock_path = 'test'
            pidlock(lock_path)
            self.assertTrue(os.path.exists(lock_path))
            release_lock(lock_path)
            self.assertFalse(os.path.exists(lock_path))
        except LockHeld:
            self.assertFalse(True)

    def test_pidlock_locked(self):
        try:
            lock_path = 'test'
            pidlock(lock_path)
            self.assertTrue(os.path.exists(lock_path))
            pidlock(lock_path)
            self.assertFalse(True)
            release_lock(lock_path)
        except LockHeld:
            self.assertTrue(True)
        finally:
            release_lock(lock_path)


if __name__ == "__main__":
    unittest.main()