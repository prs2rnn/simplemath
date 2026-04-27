import pytest
from src.simplemath import LogicChecker


class TestLogicChecker:

    @pytest.fixture
    def checker(self):
        return LogicChecker()

    def test_and_operation(self, checker):
        assert checker.and_operation(True, True) is True
        assert checker.and_operation(True, False) is False

    def test_or_operation(self, checker):
        assert checker.or_operation(True, True) is True
        assert checker.or_operation(True, False) is True
        assert checker.or_operation(False, False) is False

    def test_not_operation(self, checker):
        assert checker.not_operation(True) is False
        assert checker.not_operation(False) is True

    def test_implication(self, checker):
        assert checker.implication(True, True) is True
        assert checker.implication(False, False) is True
        assert checker.implication(False, True) is True
        assert checker.implication(True, False) is False

    def test_equivalence(self, checker):
        assert checker.equivalence(True, True) is True
        assert checker.equivalence(False, False) is True
        assert checker.equivalence(True, False) is False

    def test_check_type(self, checker):
        with pytest.raises(TypeError):
            checker.and_operation(1, bool)
            checker.and_operation('False', str)
            checker.and_operation(False, bool)

    def test_xor_operation(self, checker):
        assert checker.xor_operation(True, True) is False
        assert checker.xor_operation(False, False) is False
        assert checker.xor_operation(True, False) is True
        assert checker.xor_operation(False, True) is True

    def test_nand_operation(self, checker):
        assert checker.nand_operation(True, True) is False
        assert checker.nand_operation(False, False) is True
        assert checker.nand_operation(False, True) is True
        assert checker.nand_operation(True, False) is True

    def test_nor_operation(self, checker):
        assert checker.nor_operation(True, True) is False
        assert checker.nor_operation(False, False) is True
        assert checker.nor_operation(False, True) is False
        assert checker.nor_operation(True, False) is False
