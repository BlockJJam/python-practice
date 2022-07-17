from json_parsing.matcher import DbMatcher, KeyMatcher
import unittest

class TestMatcherForClientInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.db_matcher = DbMatcher
        cls.key_matcher = KeyMatcher
        cls.abc = 123
    
    def test_validate_db_keytype_in_json_Success(self):
        # given
        test_input= {
            "db":{
                "url":"mongodb://localhost:27017",
                "db_name":"mongodb"
            }
        }

        # when
        result = self.db_matcher.validate_key(test_input)

        # then
        self.assertEqual(result, True, '성공했나?')

        
